import pytest
from appium import webdriver
from subprocess import check_output, call
from src.mobile.user_interface.activities.main_activity import MainActivity
from pytest_bdd import given, when, then, parsers
from src.utils.file_utils import project_path, project_src_path
import yaml
from src.mobile.user_interface.activities.login_activity import LoginActivity


@pytest.fixture(scope='session')
def context():
    caps = desired_caps()
    with open(str(project_path.joinpath("tests", "mobile", "config.yml"))) as f:
        cfg_data = yaml.load(f, Loader=yaml.FullLoader)
    path_imagen = str(project_path.joinpath(project_src_path, cfg_data["path_to_media"], "test.jpg"))
    img_test = f"{cfg_data['android_media']}//test.jpg"
    # call(['adb', 'push', str(project_path.joinpath(cfg_data["path_to_media"])), "/storage"])
    config_dict = {"driver": webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=caps)}
    config_dict["driver"].push_file(img_test, source_path=path_imagen)
    yield config_dict
    check_output(['adb', 'shell', 'rm', img_test])
    config_dict["driver"].quit()
    config_dict.clear()


# region Steps comunes
# noinspection PyTypeChecker
@given("ingreso a la aplicacion")
def ingreso_aplicacion(context, usuario_prueba_fbapp):
    context["act"] = LoginActivity(context['driver'])
    context["user"] = usuario_prueba_fbapp


# noinspection PyTypeChecker
@given("me encuentro en la pantalla principal")
def gi_instance_pantalla_principal(context):
    context["act"] = MainActivity(context["driver"])


# noinspection PyTypeChecker
@then("se muestra la pantalla principal")
def th_instance_pantalla_principal(context):
    context["act"] = MainActivity(context["driver"])


# noinspection PyTypeChecker
@then("me deslogueo")
def desloguearse(context):
    context["act"] = MainActivity(context["driver"])
    context["act"] = context["act"].ir_a_tab("usuario")
    context["act"].desloguearse()


@given("ingreso con Facebook")
def gi_ingresar_con_facebook(context):
    context["act"].ingresar_con_facebook()


@when("ingreso con Facebook")
def wh_ingresar_con_facebook(context):
    context["act"].ingresar_con_facebook()


@given(parsers.parse("me dirijo a tab {nombre_tab}"))
def dirigirse_a_tab(context, nombre_tab):
    context["act"] = context["act"].ir_a_tab(nombre_tab)



# endregion


# region Auxiliares
def get_device_info():
    """
    Función que devuelve el nombre y la versión de Android de un dispositivo conectado.
    En caso de haber más de uno conectado, devuelve el primero que encuentra.
    Returns: info - dict()
    El diccionario info contiene dos pares clave-valor, siendo uno "device_name" y el otro "device_version"
    """
    info = {}
    # region Nombre dispositivo
    adb_output = str(check_output(['adb', 'devices']))
    adb_output = adb_output.replace('b\'List of devices attached\\r\\n', '')
    device = adb_output.replace('\\tdevice\\r\\n\\r\\n\'', '')
    adb_output = str(check_output(['adb', '-s', str(device), "shell", "getprop", "ro.product.model"]))
    adb_output = adb_output.replace('b\'', '')
    adb_output = adb_output.replace('\\r\\n\'', '')
    info["device_name"] = str(adb_output)
    # endregion
    # region Version android

    adb_out_version = str(check_output(['adb', '-s', f'{device}', 'shell', 'getprop', 'ro.build.version.release']))
    adb_out_version = adb_out_version.replace('b\'', '')
    adb_out_version = adb_out_version.replace('\\r\\n\'', '')
    info["device_version"] = str(adb_out_version)

    # endregion
    return info


def desired_caps():
    info = get_device_info()
    return {
        "platformName": "Android",
        "platformVersion": info["device_version"],
        "deviceName": info["device_name"],
        "noReset": "true",
        "appPackage": "com.somosagro",
        "appActivity": "com.somosagro.MainActivity",
        "automationName": "UiAutomator2",
        "uiautomator2ServerInstallTimeout": 200000,
    }
# endregion


pytest_plugins = [
    "tests.mobile.fixtures.usuarios",
    "tests.mobile.fixtures.intereses",
    "tests.mobile.fixtures.zonas",
    "tests.mobile.fixtures.publicaciones"
]
