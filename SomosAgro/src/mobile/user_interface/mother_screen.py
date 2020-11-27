from src.mobile.user_interface.base_screen import BaseScreen, UiLocator, MobileBy


_DEFAULT_TIMEOUT = 10


class MotherScreen(BaseScreen):
    def __init__(self, driver):
        super().__init__(driver)

    def continuar(self):
        continuar_btn = UiLocator(
            MobileBy.XPATH,
            '//android.view.ViewGroup[android.widget.TextView[@text="Continuar"]]'
        )
        self.t_single_tap(continuar_btn)

    def aceptar_y_continuar(self):
        aceptar_y_continuar_btn = UiLocator(
            MobileBy.XPATH,
            '//android.view.ViewGroup[android.widget.TextView[@text="Aceptar y continuar"]]'
        )
        self.t_single_tap(aceptar_y_continuar_btn)

    def aceptar(self):
        aceptar_btn = UiLocator(
            MobileBy.XPATH,
            '//android.view.ViewGroup[android.widget.TextView[@text="Aceptar"]]'
        )
        self.t_single_tap(aceptar_btn)

    def guardar(self):
        guardar_btn = UiLocator(
            MobileBy.XPATH,
            '//android.view.ViewGroup[android.widget.TextView[@text="Guardar"]]'
        )
        self.t_single_tap(guardar_btn)
