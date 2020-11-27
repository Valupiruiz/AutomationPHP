from page_objects.base_page import BasePage
from config.parameters import Parameters
from config.data.utils import Utils
import time
from .properties.locators import OrganismoLocators
import random


class Organismo(BasePage):
    def __init__(self, driver, parametros):
        super().__init__(driver)
        self.__parametros = parametros

    def agregar_organismo(self):
        self.find_element(OrganismoLocators.orga_agregar_BTN).click()
        self.find_element(OrganismoLocators.nuevo_organismo_LBL)

    def datos_organismo(self):
        self.value_complete(OrganismoLocators.orga_nombre_INP, self.__parametros["nombre_orga"])
        self.driver.execute_script(
            '$("#OrganismoType_cuit").val("23-' + str(random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.orga_cuit_INP).click()
        self.find_element(OrganismoLocators.orga_sec_INP).send_keys(self.__parametros["sector_orga"])
        self.find_element(OrganismoLocators.orga_buz_gru_INP).send_keys(self.__parametros["buz_gru_orga"])
        self.value_complete(OrganismoLocators.orga_codigo_gde_INP, self.__parametros["nombre_orga"])
        self.find_element(OrganismoLocators.orga_sis_utilizar_SEL).click()
        self.find_element(OrganismoLocators.orga_sis_utilizar_op1_LB).click()
        self.find_element(OrganismoLocators.orga_sis_utilizar_op2_LB).click()
        self.find_element(OrganismoLocators.orga_sis_utilizar_op4_LB).click()
        self.find_element(OrganismoLocators.orga_activo_CHK).click()

    def direccion_organismo(self):
        self.find_element(OrganismoLocators.orga_direc_calle_INP).send_keys(self.__parametros["calle_orga"])
        self.find_element(OrganismoLocators.orga_direc_numero_INP).send_keys(self.__parametros["numero_orga"])
        self.find_element(OrganismoLocators.orga_direc_cod_postal_INP).send_keys(self.__parametros["cod_postal_orga"])
        time.sleep(2)
        self.scroll_to_element(OrganismoLocators.orga_direc_prov_SEL)
        self.find_select(OrganismoLocators.orga_direc_prov_SEL).select_by_visible_text(
            self.__parametros["provincia_orga"])
        self.find_element(OrganismoLocators.orga_direc_partido_INP).send_keys(self.__parametros["partido_orga"])
        self.find_element(OrganismoLocators.orga_direc_localidad_INP).send_keys(self.__parametros["localidad_orga"])
        self.find_element(OrganismoLocators.orga_pub0_TAB)

    def publicador_uno_organismo(self):
        self.find_element(OrganismoLocators.orga_pub0_TAB).click()
        self.find_element(OrganismoLocators.orga_pub0_nombre_INP).send_keys(self.__parametros["pub0_nombre_orga"])
        self.find_element(OrganismoLocators.orga_pub0_apellido_INP).send_keys(self.__parametros["pub0_apellido_orga"])
        self.driver.execute_script(
            '$("#OrganismoType_publicadores_0_cuil").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.orga_pub0_cuil_INP).click()
        self.find_element(OrganismoLocators.orga_pub0_tel_INP).send_keys(self.__parametros["pub0_tel_orga"])
        self.find_element(OrganismoLocators.orga_pub0_mail_INP).send_keys(self.__parametros["pub0_mail_orga"])
        self.find_element(OrganismoLocators.orga_pub0_usugde_INP).send_keys(self.__parametros["pub0_usuario_gde_orga"])

    def facturador_uno_organismo(self):
        self.find_element(OrganismoLocators.orga_fac0_TAB).click()
        self.find_element(OrganismoLocators.orga_fac0_nombre_INP).send_keys(self.__parametros["fac0_nombre_orga"])
        self.find_element(OrganismoLocators.orga_fac0_apellido_INP).send_keys(self.__parametros["fac0_apellido_orga"])
        # self.driver.execute_script('$("#OrganismoGDEType_pagadores_0_cuil").val("23-{}-4")'.
        # format(str(random.randint(11111111, 99999999))))
        self.driver.execute_script(
            '$("#OrganismoType_pagadores_0_cuil").val("23-' + str(random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.orga_fac0_cuil_INP).click()
        self.find_element(OrganismoLocators.orga_fac0_tel_INP).send_keys(self.__parametros["fac0_tel_orga"])
        self.find_element(OrganismoLocators.orga_fac0_mail_INP).send_keys(self.__parametros["fac0_mail_orga"])

    def guardar_organismo(self):
        self.find_element(OrganismoLocators.orga_guardar_BTN).click()

    def guardar_dependencia(self):
        self.find_element(OrganismoLocators.dep_guardar_BTN).click()

    def dependencia_uno(self):
        # self.wait_for_staleness(OrganismoLocators.dep_agregar_BTN)
        self.scroll_to_element(OrganismoLocators.dep_agregar_BTN)
        self.find_element(OrganismoLocators.dep_agregar_BTN).click()
        # time.sleep(3)
        self.value_complete(OrganismoLocators.dep0_nombre_INP, self.__parametros["dep0_nombre"])
        self.find_element(OrganismoLocators.dep0_codigo_gde_INP).send_keys(self.__parametros["dep0_codigo_gde"])
        self.find_element(OrganismoLocators.dep0_sec_INP).send_keys(self.__parametros["dep0_sector"])
        self.driver.execute_script(
            '$("#DependenciaOrganismoGDEType_cuit").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.dep0_cuit_INP).click()
        self.find_element(OrganismoLocators.dep0_buz_gru_INP).send_keys(self.__parametros["dep0_buzon_grupal"])
        self.find_element(OrganismoLocators.dep0_direc_calle_INP).send_keys(self.__parametros["dep0_calle"])
        self.find_element(OrganismoLocators.dep0_direc_numero_INP).send_keys(self.__parametros["dep0_numero"])
        self.find_element(OrganismoLocators.dep0_cod_postal_INP).send_keys(self.__parametros["dep0_cod_postal"])
        self.find_select(OrganismoLocators.dep0_prov_SEL).select_by_visible_text(
            self.__parametros["dep0_provincia"])
        self.find_element(OrganismoLocators.dep0_partido_INP).send_keys(self.__parametros["dep0_partido"])
        self.find_element(OrganismoLocators.dep0_localidad_INP).send_keys(self.__parametros["dep0_localidad"])

    def publicador_uno_dependencia_uno(self):
        self.find_element(OrganismoLocators.dep0_pub_TAB).click()
        self.find_element(OrganismoLocators.dep0_pub_nombre_INP).send_keys(self.__parametros["dep0_pub0_nombre"])
        self.find_element(OrganismoLocators.dep0_pub_apellido_INP).send_keys(self.__parametros["dep0_pub0_apellido"])
        self.driver.execute_script(
            '$("#DependenciaOrganismoGDEType_publicadores_0_cuil").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.dep0_pub_cuil_INP).click()
        self.find_element(OrganismoLocators.dep0_pub_tel_INP).send_keys(self.__parametros["dep0_pub0_tel"])
        self.find_element(OrganismoLocators.dep0_pub_mail_INP).send_keys(self.__parametros["dep0_pub0_mail"])
        self.find_element(OrganismoLocators.dep0_pub_usuario_gde_INP).send_keys(self.__parametros["dep0_pub0_usu_gde"])
        self.find_element(OrganismoLocators.dep_pub_activo_CHK).click()

    def facturador_uno_dependencia_uno(self):
        self.find_element(OrganismoLocators.dep0_fac_TAB).click()
        self.find_element(OrganismoLocators.dep0_fac_nombre_INP).send_keys(self.__parametros["dep0_fac0_nombre"])
        self.find_element(OrganismoLocators.dep0_fac_apellido_INP).send_keys(self.__parametros["dep0_fac0_apellido"])
        self.driver.execute_script(
            '$("#DependenciaOrganismoGDEType_pagadores_0_cuil").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.dep0_fac_cuil_INP).click()
        self.find_element(OrganismoLocators.dep0_fac_tel_INP).send_keys(self.__parametros["dep0_fac0_tel"])
        self.find_element(OrganismoLocators.dep0_fac_mail_INP).send_keys(self.__parametros["dep0_fac0_mail"])

    def subdependencia_uno_dependencia_uno(self):
        time.sleep(2)
        self.find_element(OrganismoLocators.dep0_sub0_agregar_BTN).click()
        self.find_element(OrganismoLocators.titulo_sub_LBL)
        self.value_complete(OrganismoLocators.dep0_nombre_INP, self.__parametros["dep1_sub0_nombre"])
        self.find_element(OrganismoLocators.dep0_codigo_gde_INP).send_keys(self.__parametros["dep1_sub0_codigo_gde"])
        self.find_element(OrganismoLocators.dep0_sec_INP).send_keys(self.__parametros["dep1_sub0_sector"])
        self.find_element(OrganismoLocators.dep0_buz_gru_INP).send_keys(self.__parametros["dep1_sub0_buzon_grupal"])
        self.driver.execute_script(
            '$("#DependenciaOrganismoGDEType_cuit").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        time.sleep(2)
        self.find_element(OrganismoLocators.dep0_cuit_INP).click()
        self.find_element(OrganismoLocators.dep0_direc_calle_INP).send_keys(self.__parametros["dep1_sub0_calle"])
        self.find_element(OrganismoLocators.dep0_direc_numero_INP).send_keys(self.__parametros["dep1_sub0_numero"])
        self.find_element(OrganismoLocators.dep0_cod_postal_INP).send_keys(self.__parametros["dep1_sub0_cod_postal"])
        self.find_select(OrganismoLocators.dep0_prov_SEL).select_by_visible_text(
            self.__parametros["dep1_sub0provincia"])
        self.find_element(OrganismoLocators.dep0_partido_INP).send_keys(self.__parametros["dep0_partido"])
        self.find_element(OrganismoLocators.dep0_localidad_INP).send_keys(self.__parametros["dep0_localidad"])
        self.find_element(OrganismoLocators.agregar_publicador_dep_BTN).click()
        self.find_element(OrganismoLocators.agregar_facturador_dep_BTN).click()

    def publicador_subdependencia_uno_dependencia_uno(self):
        self.find_element(OrganismoLocators.dep0_pub_nombre_INP).send_keys(self.__parametros["dep0_pub0_nombre"])
        self.find_element(OrganismoLocators.dep0_pub_apellido_INP).send_keys(self.__parametros["dep0_pub0_apellido"])
        self.driver.execute_script(
            '$("#DependenciaOrganismoGDEType_publicadores_0_cuil").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.dep0_pub_cuil_INP).click()
        self.find_element(OrganismoLocators.dep0_pub_tel_INP).send_keys(self.__parametros["dep0_pub0_tel"])
        self.find_element(OrganismoLocators.dep0_pub_mail_INP).send_keys(self.__parametros["dep0_pub0_mail"])
        usuario_gde = self.__parametros["dep0_pub0_usu_gde"] + str(random.randint(1, 6000))
        Parameters.set_usu_pub(usuario_gde)
        self.find_element(OrganismoLocators.dep0_pub_usuario_gde_INP).send_keys(usuario_gde)
        self.find_element(OrganismoLocators.dep_pub_activo_CHK).click()

    def facturador_subdependencia_uno_dependencia_uno(self):

        self.find_element(OrganismoLocators.dep0_fac_nombre_INP).send_keys(self.__parametros["dep0_fac0_nombre"])
        self.find_element(OrganismoLocators.dep0_fac_apellido_INP).send_keys(self.__parametros["dep0_fac0_apellido"])
        self.driver.execute_script(
            '$("#DependenciaOrganismoGDEType_pagadores_0_cuil").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.dep0_fac_cuil_INP).click()
        self.find_element(OrganismoLocators.dep0_fac_tel_INP).send_keys(self.__parametros["dep0_fac0_tel"])
        self.find_element(OrganismoLocators.dep0_fac_mail_INP).send_keys(self.__parametros["dep0_fac0_mail"])

    def correcto_organismo(self, mensaje):
        formatter = {"mensaje": mensaje}
        locator = OrganismoLocators.TEMP_LOCATOR_MENSAJE.formatear_locator(formatter)
        try:
            self.find_element(locator)
            return True
        except Exception as e:
            print(e)
            return False

    def activar_organismo(self):
        self.find_element(OrganismoLocators.orga_nombre_filtro_INP).send_keys(self.__parametros["nombre_orga"])
        self.find_element(OrganismoLocators.orga_estado_SEL).click()
        self.find_element(OrganismoLocators.orga_estado_inactivo_OP).click()
        self.find_element(OrganismoLocators.orga_buscar_BTN).click()
        self.find_element(OrganismoLocators.orga_lapiz_modif_BTN).click()
        self.find_element(OrganismoLocators.orga_activo_CHK).click()

        # self.find_element(OrganismoLocators.orga_lapiz_modif_BTN).click()
        # time.sleep(2)
        # self.find_element(OrganismoLocators.orga_activo_CHK).click()
        # self.find_element(OrganismoLocators.locator_dep_dos_btn(self.__parametros["dep1_nombre"])).click()
        # time.sleep(2)
        # self.find_element(OrganismoLocators.locator_dep_dos_btn(self.__parametros["dep1_sub0_nombre"])).click()
        # self.find_element(OrganismoLocators.dep1_subdep0_activo_CHK).click()

    def se_modifico_correctamente(self):
        return self.find_element(OrganismoLocators.mensaje_MSJ).text
