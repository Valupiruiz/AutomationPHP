from src.mobile.user_interface.base_screen import UiLocator
from appium.webdriver.common.mobileby import MobileBy


class RegistroInfoLocators:
    USUARIO_EDITTEXT = UiLocator(
        MobileBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)'
    )
    NOMBRE_EMPRESA_EDITTEXT = UiLocator(
        MobileBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)'
    )
    EMAIL_EDITTEXT = UiLocator(
        MobileBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)'
    )
    TELEFONO_EDITTEXT = UiLocator(
        MobileBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(3)'
    )
