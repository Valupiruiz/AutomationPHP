from src.mobile.user_interface.base_screen import UiLocator, MobileBy


class NuevaPublicacionLocators:
    SELECCIONAR_TIPO_TEMP = UiLocator(
        MobileBy.XPATH, "//android.view.ViewGroup[android.widget.TextView[@text='{texto}']]"
                        "//android.view.ViewGroup"
    )
