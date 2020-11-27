from src.mobile.user_interface.base_screen import UiLocator, MobileBy


class VistaPreviaLocators:
    TITULO_TXTVW = UiLocator(MobileBy.XPATH, "//android.widget.HorizontalScrollView/"
                                             "following-sibling::android.widget.TextView[1]")
    USUARIO_TXTVW = UiLocator(MobileBy.XPATH, "(//android.widget.ScrollView//android.view.ViewGroup//android.view.ViewGroup//android.widget.TextView)[3]")
    ETIQUETA_TXTVW = UiLocator(MobileBy.XPATH, "(//android.widget.ScrollView//android.view.ViewGroup//android.view.ViewGroup//android.widget.TextView)[5]")
    ZONA_TXTVW = UiLocator(MobileBy.XPATH, "(//android.widget.ScrollView//android.view.ViewGroup//android.view.ViewGroup//android.widget.TextView)[7]")
    SINTESIS_TXTVW = UiLocator(MobileBy.XPATH, "(//android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView)[2]")
    DESCRIPCION_TXTVW = UiLocator(MobileBy.XPATH, "(//android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView)[3]")
    PAGAR_BTN_TEMP = UiLocator(MobileBy.XPATH, "//android.view.ViewGroup[android.widget.TextView[@text='{modo}']]")
