from src.mobile.user_interface.base_screen import UiLocator
from appium.webdriver.common.mobileby import MobileBy


class LoginStrategies:
    FACEBOOK_LOGIN_TEXTVIEW = UiLocator(
        MobileBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").childSelector('
        'new UiSelector().className("android.widget.TextView").text("Continuar con Facebook")'
        ')'
    )
    GOOGLE_LOGIN_TEXTVIEW = UiLocator(
        MobileBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").childSelector('
        'new UiSelector().className("android.widget.TextView").text("Continuar con Google")'
        ')'
    )
