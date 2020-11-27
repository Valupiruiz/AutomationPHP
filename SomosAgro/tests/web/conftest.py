from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pytest_bdd import given, then, parsers
import pytest


@pytest.fixture(scope='session')
def context():
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


# region Givens comunes
@given("dummy given")
def ejemplo_given(context):
    pass
# endregion


# region Whens comunes
@when("dummy when")
def ejemplo_when(context):
    pass
# endregion


# region Thens comunes
@then("dummy then")
def ejemplo_then(context):
    pass
# endregion


pytest_plugins = [

]
