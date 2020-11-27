from appium.webdriver.common.mobileby import MobileBy
from src.mobile.user_interface.base_screen import UiLocator


class ZonasLocators:
    ZONA_VIEW_TEMP = UiLocator(
        MobileBy.XPATH,
        '//android.view.ViewGroup[android.widget.TextView[contains(@text, "{texto}")]]'
    )
