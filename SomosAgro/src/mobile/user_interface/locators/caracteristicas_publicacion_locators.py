from src.mobile.user_interface.base_screen import UiLocator, MobileBy


class CaracteristicasPublicacionLocators:
    CANTIDAD_DIAS_TEMP = UiLocator(
        MobileBy.XPATH,
        '//android.view.ViewGroup[android.view.ViewGroup/android.widget.TextView[@text="{cant_dias}"]]'
    )
    PRECIO_PUBLICACION_VW = UiLocator(
        MobileBy.XPATH,
        '//android.widget.TextView[contains(@text, "$")]'
    )
