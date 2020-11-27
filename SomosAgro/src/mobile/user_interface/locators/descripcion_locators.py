from src.mobile.user_interface.base_screen import UiLocator, MobileBy


class DescripcionLocators:
    TITULO_ETXT = UiLocator(MobileBy.XPATH, "(//android.view.ViewGroup[android.widget.TextView[@text='Título']]"
                                            "/android.view.ViewGroup/android.widget.EditText)[1]")
    SINTESIS_ETXT = UiLocator(MobileBy.XPATH, "(//android.view.ViewGroup[android.widget.TextView[@text='Título']]"
                                              "/android.view.ViewGroup/android.widget.EditText)[2]")
    DESCRIPCION_ETXT = UiLocator(MobileBy.XPATH, "(//android.view.ViewGroup[android.widget.TextView[@text='Título']]"
                                                 "/android.view.ViewGroup/android.widget.EditText)[3]")
