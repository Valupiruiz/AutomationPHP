from page_objects.base_page import BasePage
from .properties.locators import MenuLocators
from page_objects.CREAR_AVISO.Nuevo_aviso_acta import NuevoAviso
from page_objects.ORGANISMOS.ABMSOrganismos import OrganismoSimple
from page_objects.CREAR_AVISO.Nuevo_aviso_api import NuevoAvisoAPI
from page_objects.VERIFICACION_AVISO.Verificar_aviso import Verificacion
from page_objects.CREAR_AVISO_CUARTA.Crear_aviso_cuarta import NuevoAvisoCuarta
from page_objects.BANDEJA_TRAMITES.Bandeja_tramites import BandejaTramites
from page_objects.FIRMANTES.Nuevo_firmante import NuevoFirmante
from page_objects.ORGANISMOS_JUDICIALES.Organismo_Judicial import OrganismoJudicial
from page_objects.ORGANISMOSNEW.ABMSOgarnismosNew import Organismo
from page_objects.OA_SUPLEMENTOS.OA_suplementos import OASuplemento
from generated_data.data_manager import DataManager


class Menu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Se ingresa al menu, y se carga la pagina basica de ese menu, con todos los datos de tipo de aviso y de datos erroneos
    def click_menu(self, menu1, menu2, *parametros):
        self.find_element(self.locator_menu(menu1)).click()
        self.find_element(self.locator_menu(menu2)).click()
        return self.pagina_basica(menu2, *parametros)

    def locator_menu(self, menu1):
        indices = {
            "Avisos": MenuLocators.avisos_BTN,
            "Cierre de edicion": MenuLocators.cierre_edicion_BTN,
            "Administracion": MenuLocators.administracion_BTN,
            "Ingreso Manual": MenuLocators.ingreso_manual_BTN,
            "Organismos": MenuLocators.organismos_BTN,
            "Organismos Nuevo": MenuLocators.organismos_new_BTN,
            "Verificacion": MenuLocators.verificacion_BTN,
            "Firmantes": MenuLocators.firmantes_BTN,
            "Cuarta": MenuLocators.cuarta_BTN,
            "Cargar aviso cuarta": MenuLocators.cuarta_aviso_BTN,
            "Bandeja de Tramites": MenuLocators.bandeja_tramites_BTN,
            "Organismos Judiciales": MenuLocators.organismo_judicial_BTN,
            "Cierre de edición": MenuLocators.cierre_edicion_BTN,
            "Orden de armado suplementos": MenuLocators.oa_suplementos_BTN
        }
        return indices[menu1]

    def pagina_basica(self, menu2, parametros):
        pagina = {
            "Ingreso Manual": NuevoAviso(self.driver, parametros["aviso"]),
            "Organismos": OrganismoSimple(self.driver, parametros["organismo"]),
            "Ingreso API": NuevoAvisoAPI(self.driver),
            "Verificacion": Verificacion(self.driver, DataManager.get_id_aviso(),
                                         parametros[DataManager.get_tipoAviso() + "Erroneo"],
                                         parametros[DataManager.get_tipoAviso()], DataManager.get_tipoAviso()),
            "Cargar aviso cuarta": NuevoAvisoCuarta(self.driver),
            "Bandeja de Tramites": BandejaTramites(self.driver, DataManager.get_id_aviso(),
                                                   parametros[DataManager.get_tipoAviso() + "Erroneo"],
                                                   parametros[DataManager.get_tipoAviso()],
                                                   DataManager.get_tipoAviso()),
            "Firmantes": NuevoFirmante(self.driver),
            "Organismos Judiciales": OrganismoJudicial(self.driver, parametros["orgaJudicial"]),
            "Organismos Nuevo": Organismo(self.driver, parametros["organismo"]),
            "Orden de armado suplementos": OASuplemento(self.driver, parametros["oa_sup"])
        }
        return pagina[menu2]
