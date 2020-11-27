from page_objects.base_page import BasePage
from config.parameters import Parameters
from config.data.utils import Utils
import time
from .properties.locators import OrganismoLocators
import random


class OrganismoSimple(BasePage):
    def __init__(self, driver, parametros):
        super().__init__(driver)
        self.__parametros = parametros

    def agregar_organismo(self):
        self.find_element(OrganismoLocators.orga_agregar_BTN).click()

    def guardar_organismo(self):
        self.find_element(OrganismoLocators.orga_guardar_BTN).click()

    def datos_organismo(self):
        self.value_complete(OrganismoLocators.orga_nombre_INP, self.__parametros["nombre_orga"])
        self.driver.execute_script(
            '$("#OrganismoGDEType_cuit").val("23-' + str(random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.orga_cuit_INP).click()
        self.find_element(OrganismoLocators.orga_sec_INP).send_keys(self.__parametros["sector_orga"])
        self.find_element(OrganismoLocators.orga_buz_gru_INP).send_keys(self.__parametros["buz_gru_orga"])
        self.value_complete(OrganismoLocators.orga_codigo_gde_INP, self.__parametros["nombre_orga"])
        self.find_element(OrganismoLocators.orga_sis_utilizar_SEL).click()
        self.find_element(OrganismoLocators.orga_sis_utilizar_op1_LB).click()
        self.find_element(OrganismoLocators.orga_sis_utilizar_op2_LB).click()
        self.find_element(OrganismoLocators.orga_sis_utilizar_op4_LB).click()

    def direccion_organismo(self):
        self.find_element(OrganismoLocators.orga_direc_calle_INP).send_keys(self.__parametros["calle_orga"])
        self.find_element(OrganismoLocators.orga_direc_numero_INP).send_keys(self.__parametros["numero_orga"])
        self.find_element(OrganismoLocators.orga_direc_cod_postal_INP).send_keys(self.__parametros["cod_postal_orga"])
        time.sleep(2)
        self.find_select(OrganismoLocators.orga_direc_prov_SEL).select_by_visible_text(
            self.__parametros["provincia_orga"])
        self.find_element(OrganismoLocators.orga_direc_partido_INP).send_keys(self.__parametros["partido_orga"])
        self.find_element(OrganismoLocators.orga_direc_localidad_INP).send_keys(self.__parametros["localidad_orga"])

    def publicador_uno_organismo(self):
        self.find_element(OrganismoLocators.orga_pub0_TAB).click()
        self.find_element(OrganismoLocators.orga_pub0_nombre_INP).send_keys(self.__parametros["pub0_nombre_orga"])
        self.find_element(OrganismoLocators.orga_pub0_apellido_INP).send_keys(self.__parametros["pub0_apellido_orga"])
        self.driver.execute_script('$("#OrganismoType_publicadores_0_cuil").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.orga_pub0_cuil_INP).click()
        self.find_element(OrganismoLocators.orga_pub0_tel_INP).send_keys(self.__parametros["pub0_tel_orga"])
        self.find_element(OrganismoLocators.orga_pub0_mail_INP).send_keys(self.__parametros["pub0_mail_orga"])
        self.find_element(OrganismoLocators.orga_pub0_usugde_INP).send_keys(self.__parametros["pub0_usuario_gde_orga"])

    def facturador_uno_organismo(self):
        self.find_element(OrganismoLocators.orga_fac0_nombre_INP).send_keys(self.__parametros["fac0_nombre_orga"])
        self.find_element(OrganismoLocators.orga_fac0_apellido_INP).send_keys(self.__parametros["fac0_apellido_orga"])
        # self.driver.execute_script('$("#OrganismoGDEType_pagadores_0_cuil").val("23-{}-4")'.format(str(random.randint(11111111, 99999999))))
        self.driver.execute_script(
            '$("#OrganismoGDEType_pagadores_0_cuil").val("23-' + str(random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.orga_fac0_cuil_INP).click()
        self.find_element(OrganismoLocators.orga_fac0_tel_INP).send_keys(self.__parametros["fac0_tel_orga"])
        self.find_element(OrganismoLocators.orga_fac0_mail_INP).send_keys(self.__parametros["fac0_mail_orga"])

    def dependencia_uno(self):
        self.find_element(OrganismoLocators.dep_agregar_BTN).click()
        self.find_element(OrganismoLocators.dep0_nombre_INP).send_keys(self.__parametros["dep0_nombre"])
        self.find_element(OrganismoLocators.dep0_codigo_gde_INP).send_keys(self.__parametros["dep0_codigo_gde"])
        self.find_element(OrganismoLocators.dep0_sec_INP).send_keys(self.__parametros["dep0_sector"])
        self.driver.execute_script(
            '$("#OrganismoGDEType_dependenciasPadre_0_cuit").val("23-' + str(
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
        self.find_element(OrganismoLocators.dep0_pub_nombre_INP).send_keys(self.__parametros["dep0_pub0_nombre"])
        self.find_element(OrganismoLocators.dep0_pub_apellido_INP).send_keys(self.__parametros["dep0_pub0_apellido"])
        self.driver.execute_script(
            '$("#OrganismoGDEType_dependenciasPadre_0_publicadores_1_cuil").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.dep0_pub_cuil_INP).click()
        self.find_element(OrganismoLocators.dep0_pub_tel_INP).send_keys(self.__parametros["dep0_pub0_tel"])
        self.find_element(OrganismoLocators.dep0_pub_mail_INP).send_keys(self.__parametros["dep0_pub0_mail"])

    def facturador_uno_dependencia_uno(self):
        self.find_element(OrganismoLocators.dep0_fac_nombre_INP).send_keys(self.__parametros["dep0_fac0_nombre"])
        self.find_element(OrganismoLocators.dep0_fac_apellido_INP).send_keys(self.__parametros["dep0_fac0_apellido"])
        self.driver.execute_script(
            '$("#OrganismoGDEType_dependenciasPadre_0_pagadores_1_cuil").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.dep0_fac_cuil_INP).click()
        self.find_element(OrganismoLocators.dep0_fac_tel_INP).send_keys(self.__parametros["dep0_fac0_tel"])
        self.find_element(OrganismoLocators.dep0_fac_mail_INP).send_keys(self.__parametros["dep0_fac0_mail"])

    def subdependencia_uno_dependencia_uno(self):
        time.sleep(3)
        self.find_element(OrganismoLocators.dep0_sub0_agregar_BTN).click()
        time.sleep(3)
        self.find_element(OrganismoLocators.dep0_sub0_nombre_INP).send_keys(self.__parametros["dep0_sub0_nombre"])
        self.find_element(OrganismoLocators.dep0_sub0_cod_gde_INP).send_keys(self.__parametros["dep0_sub0_codgde"])
        self.find_element(OrganismoLocators.dep0_sub0_sector_INP).send_keys(self.__parametros["dep0_sub0_sector"])
        self.find_element(OrganismoLocators.dep0_sub0_buz_grupal_INP).send_keys(self.__parametros["dep0_sub0_buzon"])
        self.driver.execute_script(
            '$("#OrganismoGDEType_dependencias_0_subDependencia0_cuit").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        time.sleep(2)
        self.find_element(OrganismoLocators.dep0_sub0_cuit_INP).click()
        self.find_element(OrganismoLocators.dep0_sub0_calle_INP).send_keys(self.__parametros["dep0_calle"])
        self.find_element(OrganismoLocators.dep0_sub0_num_INP).send_keys(self.__parametros["dep0_numero"])
        self.find_element(OrganismoLocators.dep0_sub0_cod_postal_INP).send_keys(self.__parametros["dep0_cod_postal"])
        self.find_select(OrganismoLocators.dep0_sub0_prov_INP).select_by_visible_text(
            self.__parametros["dep0_provincia"])
        self.find_element(OrganismoLocators.dep0_sub0_partido_INP).send_keys(self.__parametros["dep0_partido"])
        self.find_element(OrganismoLocators.dep0_sub0_localdia_INP).send_keys(self.__parametros["dep0_localidad"])
        self.find_element(OrganismoLocators.dep0_sub0_agregar_fac_BTN).click()
        self.find_element(OrganismoLocators.dep0_sub0_agregar_pub_BTN).click()

    def publicador_subdependencia_uno_dependencia_uno(self):
        self.find_element(OrganismoLocators.dep0_sub0_pub_nombre_INP).send_keys(self.__parametros["dep0_pub0_nombre"])
        self.find_element(OrganismoLocators.dep0_sub0_pub_apellido_INP).send_keys(self.__parametros
                                                                                  ["dep0_pub0_apellido"])
        self.driver.execute_script(
            '$("#OrganismoGDEType_dependenciasPadre_0_subDependencias_0_publicadores_2_cuil").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.dep0_sub0_pub_cuil_INP).click()
        self.find_element(OrganismoLocators.dep0_sub0_pub_tel_INP).send_keys(self.__parametros["dep0_pub0_tel"])
        self.find_element(OrganismoLocators.dep0_sub0_pub_mail_INP).send_keys(self.__parametros["dep0_pub0_mail"])
        self.find_element(OrganismoLocators.dep0_sub0_pub_usu_gde_INP).send_keys(self.__parametros["dep0_pub0_usu_gde"])

    def facturador_subdependencia_uno_dependencia_uno(self):
        self.find_element(OrganismoLocators.dep0_sub0_pag_nombre_INP).send_keys(self.__parametros["dep0_pub0_nombre"])
        self.find_element(OrganismoLocators.dep0_sub0_pag_apellido_INP).send_keys(self.__parametros["dep0_pub0_nombre"])
        self.driver.execute_script(
            '$("#OrganismoGDEType_dependenciasPadre_0_subDependencias_0_pagadores_2_cuil").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.dep0_sub0_pag_cuil_INP).click()
        self.find_element(OrganismoLocators.dep0_sub0_pag_tel_INP).send_keys(self.__parametros["dep0_pub0_tel"])
        self.find_element(OrganismoLocators.dep0_sub0_pag_mail_INP).send_keys(self.__parametros["dep0_pub0_mail"])

    def modifico_organismo(self):
        self.find_element(OrganismoLocators.orga_nombre_filtro_INP).send_keys(self.__parametros["nombre_orga"])
        self.find_element(OrganismoLocators.orga_buscar_BTN).click()
        time.sleep(2)
        self.find_element(OrganismoLocators.orga_una_pagina_LB)
        self.find_element(OrganismoLocators.orga_lapiz_modif_BTN).click()

    def dependencia_dos(self):
        time.sleep(2)
        self.find_element(OrganismoLocators.dep_agregar_BTN).click()
        time.sleep(2)
        self.find_element(OrganismoLocators.dep1_nombre_INP).send_keys(self.__parametros["dep1_nombre"])
        self.find_element(OrganismoLocators.dep1_codigo_gde_INP).send_keys(self.__parametros["dep1_codigo_gde"])
        self.find_element(OrganismoLocators.dep1_sec_INP).send_keys(self.__parametros["dep1_sector"])
        self.driver.execute_script(
            '$("#OrganismoGDEType_dependencias_2_cuit").val("23-' + str(random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.dep1_cuit_INP).click()
        self.find_element(OrganismoLocators.dep1_buz_gru_INP).send_keys(self.__parametros["dep1_buzon_grupal"])
        self.find_element(OrganismoLocators.dep1_direc_calle_INP).send_keys(self.__parametros["dep1_calle"])
        self.find_element(OrganismoLocators.dep1_direc_numero_INP).send_keys(self.__parametros["dep1_numero"])
        self.find_element(OrganismoLocators.dep1_cod_postal_INP).send_keys(self.__parametros["dep1_cod_postal"])
        self.find_select(OrganismoLocators.dep1_prov_SEL).select_by_visible_text(
            self.__parametros["dep1_provincia"])
        self.find_element(OrganismoLocators.dep1_partido_INP).send_keys(self.__parametros["dep1_partido"])
        self.find_element(OrganismoLocators.dep1_localidad_INP).send_keys(self.__parametros["dep1_localidad"])
        self.find_element(OrganismoLocators.dep1_act_CHK).click()

    def publicador_dependencia_dos(self):
        self.find_element(OrganismoLocators.dep1_pub_nombre_INP).send_keys(self.__parametros["dep1_pub0_nombre"])
        self.find_element(OrganismoLocators.dep1_pub_apellido_INP).send_keys(self.__parametros["dep1_pub0_apellido"])
        self.driver.execute_script(
            '$("#OrganismoGDEType_dependenciasPadre_2_publicadores_3_cuil").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.dep1_pub_cuil_INP).click()
        self.find_element(OrganismoLocators.dep1_pub_tel_INP).send_keys(self.__parametros["dep1_pub0_tel"])
        self.find_element(OrganismoLocators.dep1_pub_usugde_INP).send_keys(self.__parametros["dep1_pub0_usu_gde"])
        self.find_element(OrganismoLocators.dep1_pub_mail_INP).send_keys(self.__parametros["dep1_pub0_mail"])

    def facturador_dependencia_dos(self):
        self.find_element(OrganismoLocators.dep1_fac_nombre_INP).send_keys(self.__parametros["dep1_fac0_nombre"])
        self.find_element(OrganismoLocators.dep1_fac_apellido_INP).send_keys(self.__parametros["dep1_fac0_apellido"])
        self.driver.execute_script(
            '$("#OrganismoGDEType_dependenciasPadre_2_pagadores_3_cuil").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.dep1_fac_cuil_INP).click()
        self.find_element(OrganismoLocators.dep1_fac_mail_INP).send_keys(self.__parametros["dep1_fac0_mail"])
        self.find_element(OrganismoLocators.dep1_fac_tel_INP).send_keys(self.__parametros["dep1_fac0_tel"])

    def subdependencia_uno_dependencia_dos(self):
        self.find_element(OrganismoLocators.dep1_agregar_sub_BTN).click()
        self.find_element(OrganismoLocators.dep1_subdep0_nombre_INP).send_keys(self.__parametros["dep1_sub0_nombre"])
        self.find_element(OrganismoLocators.dep1_subdep0_codgde_INP).send_keys(self.__parametros[
                                                                                   "dep1_sub0_codigo_gde"])
        self.find_element(OrganismoLocators.dep1_subdep0_sector_INP).send_keys(self.__parametros["dep1_sub0_sector"])
        self.find_element(OrganismoLocators.dep1_subdep0_buzgrupal_INP).send_keys(self.__parametros[
                                                                                      "dep1_sub0_buzon_grupal"])
        self.driver.execute_script(
            '$("#OrganismoGDEType_dependenciasPadre_2_subDependencias_0_cuit").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismoLocators.dep1_subdep0_cuit_INP).click()
        self.find_element(OrganismoLocators.dep1_subdep0_calle_INP).send_keys(self.__parametros["dep1_sub0_calle"])
        self.find_element(OrganismoLocators.dep1_subdep0_numero_INP).send_keys(self.__parametros["dep1_sub0_numero"])
        self.find_element(OrganismoLocators.dep1_subdep0_codpostal_INP).send_keys(self.__parametros["dep1_sub0_cod_postal"])
        self.find_select(OrganismoLocators.dep1_subdep0_prov_INP).select_by_visible_text(
            self.__parametros["dep1_sub0provincia"])
        self.find_element(OrganismoLocators.dep1_subdep0_part_INP).send_keys(self.__parametros["dep1_partido"])
        self.find_element(OrganismoLocators.dep1_subdep0_localidad_INP).send_keys(self.__parametros["dep1_partido"])
        self.find_element(OrganismoLocators.dep1_subdep0_activo_CHK).click()

    def organismo_activo(self):
        self.find_element(OrganismoLocators.orga_activo_CHK).click()

    def correctoOrganismo(self):
        self.wait_for_text_in_element(OrganismoLocators.mensaje_MSJ, "Creación exitosa")
        return self.find_element(OrganismoLocators.mensaje_MSJ).text

    def seModificoCorrectamente(self):
        self.wait_for_text_in_element(OrganismoLocators.mensaje_MSJ, "Modificación exitosa")
        return self.find_element(OrganismoLocators.mensaje_MSJ).text

    def activar_organismo(self):
        self.find_element(OrganismoLocators.orga_nombre_filtro_INP).send_keys(self.__parametros["nombre_orga"])
        self.find_element(OrganismoLocators.orga_estado_SEL).click()
        self.find_element(OrganismoLocators.orga_estado_inactivo_OP).click()
        self.find_element(OrganismoLocators.orga_buscar_BTN).click()
        self.find_element(OrganismoLocators.orga_lapiz_modif_BTN).click()
        time.sleep(2)
        self.find_element(OrganismoLocators.orga_activo_CHK).click()
        self.find_element(OrganismoLocators.locator_dep_dos_btn(self.__parametros["dep1_nombre"])).click()
        time.sleep(2)
        self.find_element(OrganismoLocators.locator_dep_dos_btn(self.__parametros["dep1_sub0_nombre"])).click()
        self.find_element(OrganismoLocators.dep1_subdep0_activo_CHK).click()
