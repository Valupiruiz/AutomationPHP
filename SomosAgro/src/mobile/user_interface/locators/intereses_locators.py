from src.mobile.user_interface.base_screen import UiLocator
from appium.webdriver.common.mobileby import MobileBy


class InteresesLocators:
    INTERES_TEMP_VIEW = UiLocator(
        MobileBy.XPATH,
        '//android.view.ViewGroup[android.widget.TextView[contains(@text, "{texto}")]]'
    )
    INTERES_SUBCATEGORIA_TEMP = UiLocator(
        MobileBy.XPATH,
        '//android.widget.ScrollView//android.view.ViewGroup//android.view.ViewGroup[android.widget.TextView'
        '[contains(@text, "{texto}")]]'
    )
    ACEPTAR_BTN = UiLocator(
        MobileBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").childSelector('
        'new UiSelector().className("android.widget.TextView").text("Aceptar")'
        ')'
    )
    INTERES_SELECCIONADO = UiLocator(
        MobileBy.XPATH,
        "//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[android.widget.TextView[@text='1']]"
    )
