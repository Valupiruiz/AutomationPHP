import allure
import pytest
from filelock import FileLock
from selenium.webdriver.chrome.options import Options

from src.config.config import LOCKS, RUTAS
from src.dominio.operable import Boveda
from src.factory.driver.factory import LocalDriverFactory, RemoteDriverFactory
from src.factory.driver.manager import DriverManager
from src.factory.monedas import MonedasFactory
from src.factory.page.factory import PageFactory
from src.factory.user import UserFactory
from src.page_objects.base.page_manager import PageManager
from src.utils.db_utils import Db
from src.utils.files import grabar, leer
from src.utils.requests import Request

lock = FileLock(LOCKS.CONFTEST)
_AMBIENTE = "localhost"

_PREFIJO_CAJA = "CA"
_PREFIJO_SUCURSAL = "SU"


@pytest.fixture
def prefijo_sucursal():
    return _PREFIJO_SUCURSAL


@pytest.fixture
def prefijo_caja():
    return _PREFIJO_CAJA


# region context
# noinspection PyTypeChecker
@pytest.fixture
def context(request, target, worker_id, cant_cajeros):
    class Context:
        pass

    context = Context()

    front, api, db = target
    context.requests = Request(api)
    context.db = Db(db)

    context.headless = request.config.getoption("headless", default=False)

    def get_options():
        options = Options()
        options.headless = context.headless
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--lang=es_AR")
        options.set_capability("name", request.node.name)
        options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
        options.set_capability('version', "83.0.4103.39")
        options.set_capability('enableLog', True)
        return options.to_capabilities()

    command_executor = request.config.getoption("--remote-server")
    if command_executor is None:
        driver_factory = LocalDriverFactory(get_options(), "Chrome")
    else:
        driver_factory = RemoteDriverFactory(get_options(), command_executor)

    context.driver_manager = DriverManager(front, driver_factory)
    context.page = PageManager(PageFactory())

    init_data(context, worker_id, cant_cajeros)

    yield context

    try:
        if request.node.rep_call.failed:
            for driver in context.driver_manager:
                url = driver.current_url.replace(front, '')
                allure.attach(driver.get_screenshot_as_png(),
                              name=f'screenshot {context.driver_manager.drivers.index(driver)} - {url}',
                              attachment_type=allure.attachment_type.PNG)
    except AttributeError as e:
        print(f"No se pudo sacar una screenshot, posiblemente haya fallado en el setup, {e}")

    for driver in context.driver_manager:
        print("\n")
        for entry in driver.get_log('browser'):
            print(entry)
        print("\n")
    context.driver_manager.quit()


def pytest_unconfigure(config):
    # esto claramente no va a aca pero xdist no cuenta con la posibilidad de hacer session teardowns
    if leer(RUTAS.NUMEROS_CODIGOS, "Fetched"):
        grabar(RUTAS.NUMEROS_CODIGOS, {"Fetched": False})


# endregion

# region init_data
def init_data(context, worker_id, cant_cajeros):
    if worker_id == 'master':
        num_worker = 1
    else:
        num_worker = int(f"{int(worker_id[-1]) + 1:02}")

    with lock:
        print(f"Empiezo el lock de {worker_id}")
        if not leer(RUTAS.NUMEROS_CODIGOS, "Fetched"):
            num_sucursal = context.db.numero_sucursal_por_subfijo(_PREFIJO_SUCURSAL) + 1
            num_caja = context.db.numero_caja_por_subfijo(_PREFIJO_CAJA) + 1
            grabar(RUTAS.NUMEROS_CODIGOS, {"Sucursal": num_sucursal, "Caja": num_caja, "Fetched": True})

        user_factory = UserFactory(context.db, num_worker)
        context.cajeros = user_factory.build_cajeros(cant_cajeros)
        context.administrador = user_factory.build_administrador()
        context.operador_remesas = user_factory.build_operador_boveda()
        context.operaciones = user_factory.build_operaciones()

        context.monedas = MonedasFactory(context.db).build()
        context.boveda = Boveda("BV0001", context.monedas)

    context.driver_manager.build_main_driver()
    context.page.set_active_driver(context.driver_manager.main_driver)
    print(f"Termina el lock de {worker_id}")


@pytest.fixture
def cant_cajeros():
    return 1


# endregion

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_addoption(parser):
    help_ambiente = "Ambiente sobre el cual se van a ejecutar las pruebas"
    help_headless = "Si esta presente, el driver se va a instanciar en modo headless"
    help_remote = "Si esta presente, se utilizara el driver remoto, en caso contrario se utilizara Chromedriver"
    parser.addoption('--ambiente', default=_AMBIENTE, action='store', dest='ambiente', help=help_ambiente)
    parser.addoption('--localhost', action='store_true', dest='localhost')
    parser.addoption('--headless', action='store_true', dest='headless', help=help_headless)
    parser.addoption('--remote-server', default=None, action='store', dest='remote', help=help_remote)


def pytest_collection_modifyitems(items):
    for item in items:
        if 'lock_boveda' in getattr(item, 'fixturenames', ()):
            item.add_marker("slow")

@pytest.fixture
def target(request):

    if request.config.getoption("localhost", default=False):
        front = "http://localhost:3000/login"
        api = "http://localhost:5000/api"
        db = "localhost"
    else:
        target = request.config.getoption("ambiente")
        front = f"https://{target}/login"
        api = f"https://{target}/api"
        db = target

    return front, api, db


pytest_plugins = [
    "fixtures.crear_sucursal",
    "fixtures.lock_boveda",
]

