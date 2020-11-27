from page_objects.base_page import BasePage
from .properties.locators import OrganismosJudicialesLocators
from config.parameters import Parameters
from generated_data.data_manager import DataManager
import random
import time


class OrganismoJudicial(BasePage):
    def __init__(self, driver, organismo_judicial):
        super().__init__(driver)
        self.organismo_judicial = organismo_judicial

    def crear_organismo_judicial(self):
        self.find_element(OrganismosJudicialesLocators.nuevo_orga_BTN).click()
        self.value_complete(OrganismosJudicialesLocators.nombre_orga_INP, self.organismo_judicial["nombre_orga"])
        self.driver.execute_script(
            '$("#OrganismoJudicialType_cuit").val("23-' + str(
                random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismosJudicialesLocators.cuit_orga_INP).click()
        self.find_element(OrganismosJudicialesLocators.calle_orga_INP).send_keys(self.organismo_judicial['calle_orga'])
        self.find_element(OrganismosJudicialesLocators.num_orga_INP).send_keys(self.organismo_judicial[
                                                                                   'cod_postal_orga'])
        self.find_element(OrganismosJudicialesLocators.cod_postal_orga_INP).send_keys(self.organismo_judicial[
                                                                                          'cod_postal_orga'])
        self.find_element(OrganismosJudicialesLocators.provincia_orga_SPAN).click()
        self.find_element(OrganismosJudicialesLocators.op_1_PROV_ORGA).click()
        self.find_element(OrganismosJudicialesLocators.partido_orga_INP).send_keys(self.organismo_judicial[
                                                                                       'partido_orga'])
        self.find_element(OrganismosJudicialesLocators.localidad_orga_INP).send_keys(self.organismo_judicial[
                                                                                         'localidad_orga'])
    def crear_secretaria(self):
        self.find_element(OrganismosJudicialesLocators.secretaria_BTN).click()
        self.find_element(OrganismosJudicialesLocators.nombre_SEC_INP).send_keys(self.organismo_judicial[
                                                                                     'nombre_secre'])
        self.driver.execute_script('$("#OrganismoJudicialType_secretarias_0_cuit").val("23-' + str(
            random.randint(11111111, 99999999)) + '-4")')
        self.find_element(OrganismosJudicialesLocators.cuit_SEC_INP).click()
        self.find_element(OrganismosJudicialesLocators.activo_SEC_CHK).click()
        self.find_element(OrganismosJudicialesLocators.calle_SEC_INP).send_keys(self.organismo_judicial['calle_secre'])
        self.find_element(OrganismosJudicialesLocators.numero_SEC_INP).send_keys(self.organismo_judicial['num_secre'])
        self.find_element(OrganismosJudicialesLocators.cod_postal_SEC_INP).send_keys(self.organismo_judicial[
                                                                                         'cod_postal_secre'])
        self.find_select(OrganismosJudicialesLocators.provincia_SEC_SEL).select_by_value(
            self.organismo_judicial['prov_op'])
        self.find_element(OrganismosJudicialesLocators.partido_SEC_INP).send_keys(self.organismo_judicial[
                                                                                      'partido_sec'])
        self.find_element(OrganismosJudicialesLocators.localidad_SEC_INP).send_keys(self.organismo_judicial[
                                                                                        'localidad_sec'])

    def crear_representante_secretaira(self):
        self.find_element(OrganismosJudicialesLocators.nuevo_repres_BTN).click()
        self.find_element(OrganismosJudicialesLocators.nombre_REP_INP).send_keys(self.organismo_judicial['nombre_rep'])
        self.find_element(OrganismosJudicialesLocators.apellido_REP_INP).send_keys(self.organismo_judicial[
                                                                                       'apellido_rep'])
        self.driver.execute_script('$("#OrganismoJudicialType_secretarias_0_representantes_0_cuil").val("23-' + str(
            random.randint(11111111, 99999999)) + '-4")')
        cuit_rep = "23-" + str(random.randint(11111111, 99999999)) + "-4"
        self.driver.execute_script(
            '$("#OrganismoJudicialType_secretarias_0_representantes_0_cuil").val("' + cuit_rep + '")')
        self.find_element(OrganismosJudicialesLocators.cuit_SEC_INP).click()
        Parameters.set_cuit_sec(cuit_rep.replace("-", ""))
        self.find_element(OrganismosJudicialesLocators.cuil_REP_INP).click()
        self.find_element(OrganismosJudicialesLocators.telefono_REP_INP).send_keys(self.organismo_judicial[
                                                                                       'telefono_rep'])
        self.find_element(OrganismosJudicialesLocators.mail_REP_INP).send_keys(self.organismo_judicial['mail_rep'])
        self.find_element(OrganismosJudicialesLocators.cargo_REP_INP).send_keys(self.organismo_judicial['cargo_rep'])
        self.find_element(OrganismosJudicialesLocators.usuario_REP_INP).send_keys(self.organismo_judicial[
                                                                                      'usuario_rep'])
        self.find_element(OrganismosJudicialesLocators.activo_REP_CHK).click()
        time.sleep(5)

    def guardar_secretaria(self):
        self.find_element(OrganismosJudicialesLocators.guardar_BTN).click()


    def correcto_organismo(self, mensaje):
        self.wait_for_text_in_element(OrganismosJudicialesLocators.mensaje_MSJ, mensaje)
        return self.find_element(OrganismosJudicialesLocators.mensaje_MSJ).text
