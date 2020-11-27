from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pytest_bdd import given, then, parsers, when
import pytest
from page_objects.pagina_principal.pagina_principal import PaginaPrincipal
from page_objects.menu.menu import Menu
from page_objects.principal_backend.principal_backend import PrincipalBackend
from page_objects.principal_docente.principal_docente import PrincipalDocente
from selenium.common.exceptions import TimeoutException
from page_objects.login_backend.login_backend import LoginBackend
import time


@pytest.fixture(scope='session')
def context():
    # TODO: logica de cargar parametros de secundarios solamente
    conf = {}
    driver = webdriver.Chrome(options=get_options())
    conf['driver'] = driver
    yield conf
    conf['driver'].quit()
    conf.clear()


def get_options():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    return options


# noinspection PyTypeChecker
@given("me encuentro en la pagina principal")
def pagina_principal_giv(context):
    context["driver"].get("http://cdocentep1.cysonline.com.ar:10001/index.php/")
    context["page"] = PaginaPrincipal(context["driver"])

@when("me encuentro en la pagina principal")
def pagina_principal_when(context):
    context["driver"].get("http://cdocentep1.cysonline.com.ar:10001/index.php/")
    context["page"] = PaginaPrincipal(context["driver"])



@given("ingreso con usuario docente")
def ingresar_al_sistema(context, docente_test5):
    context["user"] = docente_test5
    context["page"] = context["page"].loguearse_con_cuentabue()
    context["page"] = context["page"].realizar_proceso_de_logueo(docente_test5)
    try:
        context["page"] = context["page"].loguearse_con_cuentabue()
        context["page"] = context["page"].elegir_cuenta(docente_test5)
    except TimeoutException:
        pass

@given("ingreso con usuario administrador")
def ingresar_al_sistema_admin_given(context, admin):
    context["user"] = admin
    context["page"] = context["page"].loguearse_con_cuentabue()
    try:
        context["page"] = context["page"].realizar_proceso_de_logueo(admin)
        context["page"] = context["page"].loguearse_con_cuentabue()
        context["page"] = context["page"].elegir_cuenta(admin)
    except TimeoutException:
        pass

@when("ingreso con usuario administrador")
def ingresar_al_sistema_admin_when(context, admin):
    context["user"] = admin
    context["page"] = context["page"].loguearse_con_cuentabue()
    try:
        context["page"] = context["page"].realizar_proceso_de_logueo(admin)
        context["page"] = context["page"].loguearse_con_cuentabue()
        context["page"] = context["page"].elegir_cuenta(admin)
    except TimeoutException:
        pass


# noinspection PyTypeChecker
@then("cierro sesion")
def cierro_sesion(context):
    print("cierro sesion")
    context["page"] = Menu(context["driver"])
    context["page"].cierro_sesion(context["user"].nombre, context["user"].apellido)


@given(parsers.parse('me encuentro en principal {pagina}'))
def pag_principal_given(context, pagina):
    if pagina == 'docente':
        context["page"] = PrincipalDocente(context["driver"])
    if pagina == 'backend':
        context["driver"].get("http://cdocentep1.cysonline.com.ar:10001/backend.php/")
        context["page"] = PrincipalBackend(context["driver"])
        try:
            context["page"].me_encuentro_en_pag_backend()
        except TimeoutException:
            context["page"] = LoginBackend(context["driver"])
            context["page"] = context["page"].ingresar()
            context["page"].elegir_cuenta(context["user"])
            context["page"] = PrincipalBackend(context["driver"])

@when(parsers.parse('me encuentro en principal {pagina}'))
def pag_principal_when(context, pagina):
    if pagina == 'docente':
        context["page"] = PrincipalDocente(context["driver"])
    if pagina == 'backend':
        context["driver"].get("http://cdocentep1.cysonline.com.ar:10001/backend.php/")
        context["page"] = PrincipalBackend(context["driver"])
        try:
            context["page"].me_encuentro_en_pag_backend()
        except TimeoutException:
            context["page"] = LoginBackend(context["driver"])
            context["page"] = context["page"].ingresar()
            context["page"].elegir_cuenta(context["user"])
            context["page"] = PrincipalBackend(context["driver"])


@given(parsers.parse('me dirijo a {menues}'))
def me_dirijo_given(context, menues):
    menues = menues.split("->")
    context["page"].me_dirijo(menues)


@when(parsers.parse('me dirijo a {menues}'))
def me_dirijo_when(context, menues):
    menues = menues.split("->")
    context["page"].me_dirijo(menues)


pytest_plugins = [
    "tests.fixtures.dominio.usuarios",
    "tests.fixtures.dominio.titulo",
    "tests.fixtures.dominio.inscripciones",
    "tests.fixtures.dominio.cursos"
]
