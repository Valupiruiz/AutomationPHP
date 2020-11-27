from src.mobile.user_interface.base_screen import UiLocator, MobileBy


class FotografiasLocators:
    IMAGEN_TEST_IMVW = UiLocator(MobileBy.XPATH, "(//android.view.ViewGroup[android.view.ViewGroup/android.widget.ImageView])")
    CROP_EDITAR_TXVW = UiLocator(MobileBy.ACCESSIBILITY_ID, "Crop")
