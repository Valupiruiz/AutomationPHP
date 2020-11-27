import datetime
import os
from pdf_utils import RUTA_ARCHIVO
from selenium import webdriver
from behave.model import Status
from config import screenshot
from config.parameters import Parameters
from page_objects.COMMON.Login.Login import Login
from selenium.webdriver.chrome.options import Options
import shutil
from utils.file_utils import FileUtils


def before_all(context):
    options = Options()
    prefs = {"plugins.always_open_pdf_externally": True,
             "download.prompt_for_download": False,
             "download.default_directory": str(RUTA_ARCHIVO)}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--start-maximized")
    context.driver = webdriver.Remote('http://localhost:8002/wd/hub', options=options)
    context.driver.set_window_size(1366, 768)
    # context.driver.execute_script("document.body.style.transform='scale(0.8)';")
    # context.driver.maximize_window()
    Parameters.execute_file("Datos")
    context.page = Login(context.driver)
    context.data = Parameters.get_data()
    context.driver.get(context.data["ambiente"]["url"])
    context.tipo = None
    context.firmante = None
    context.status = None


def before_feature(context, feature):
    context.tipo_aviso = None
    context.id_aviso = None
    FileUtils.agregar_claves_a_json({"contador_archivos": 0}, "contador")


def after_feature(context, feature):
    shutil.rmtree(RUTA_ARCHIVO)


def after_step(context, step):
    if step.status is Status.failed:
        test_method_name = step.name.replace(' ', '_')
        test_datetime = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        screenshot.fullpage_screenshot(context.driver,
                                       os.path.join(os.path.dirname(__file__),
                                                    "screenshots\\{name}_{datetime}.png"
                                                    .format(name=test_method_name,
                                                            datetime=test_datetime)))
        print("TEST FAILED: " + context.driver.current_url)


def after_all(context):
    shutil.rmtree(RUTA_ARCHIVO)
