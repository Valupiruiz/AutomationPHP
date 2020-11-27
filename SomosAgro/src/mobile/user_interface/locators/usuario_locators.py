from src.mobile.user_interface.base_screen import UiLocator, MobileBy


class UsuarioLocators:
    ENGRANAJE_BTN = UiLocator(MobileBy.XPATH, "//android.view.ViewGroup[android.widget.TextView[@text='']]")
    OPCION_CONFIGURACION = UiLocator(MobileBy.XPATH, "//android.view.ViewGroup[android.widget.TextView[@text='{opc}']]")
    PUBLICACIONES_VIGENTES = UiLocator(MobileBy.XPATH, "//android.view.ViewGroup[android.widget.TextView"
                                                       "[@text='PUBLICACIONES VIGENTES']]")
    PUBLICACION_TEMP = UiLocator(MobileBy.XPATH, "//android.widget.ScrollView//android.widget.ScrollView"
                                                 "[//android.widget.TextView[@text='{titulo}']]")
    OPCIONES_PUBLICACION_BURGER = UiLocator(MobileBy.XPATH, "(//android.widget.ScrollView//android.view.ViewGroup"
                                                            "//android.widget.ScrollView//android.view.ViewGroup"
                                                            "[android.widget.TextView[@text='']])[1]")
    ELIMINAR_BTN = UiLocator(MobileBy.ID, "android:id/button1")
