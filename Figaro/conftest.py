from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pytest_bdd import given, then
import pytest
from page_objects.common.login.login import Login
from page_objects.common.navbar.navbar import Navbar


@pytest.fixture(scope='session')
def driver():
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
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    return options


@given('ingreso al sistema con usuario <usuario>')
def ingreso_al_sistema(driver, usuario):
    driver["user_actual"] = next(u for u in driver["usuarios"] if u.username == usuario)
    driver["page"] = Login(driver['driver'])
    driver["page"].loguearse(driver["user_actual"])


pytest_plugins = [
    "tests.fixtures.crear_evaluaciones",
    "tests.fixtures.dominio.usuarios",
    "tests.fixtures.dominio.instituciones",
    "tests.fixtures.calificar_evaluaciones"
]


@then('salgo')
def salir_del_sistema(driver):
    driver["page"] = Navbar(driver["driver"])
    driver["page"].desloguearse()
