from selenium.common.exceptions import TimeoutException

from page_objects.base_page import BasePage
from .properties.locators import VerificarAvisoLocators
from config.parameters import Parameters
import requests
import json
from config.data.utils import Utils
import time
from selenium.webdriver.common.keys import Keys
import pdf_utils
import re
from utils.file_utils import FileUtils

utils = Utils()


class Verificacion(BasePage):
    def __init__(self, driver, id_aviso, aviso_erroneo, aviso, tipo_aviso):
        super().__init__(driver)
        self.id_aviso = id_aviso
        self.aviso_erroneo = aviso_erroneo
        self.aviso = aviso
        self.tipo_aviso = tipo_aviso

    def apruebo_aviso(self):
        self.find_element(VerificarAvisoLocators.aprobar_BTN).click()

    def apruebo_decreto(self):
        time.sleep(10)
        self.find_element(VerificarAvisoLocators.titulo_INP).clear()

    def apruebo_sucesion(self):
        try:
            self.find_element(VerificarAvisoLocators.sin_valor_subtipo_SPAN)
            self.find_element(VerificarAvisoLocators.subtipo_SEL).click()
            self.find_element(VerificarAvisoLocators.opcion_subtipo_LBL).click()
            self.find_element(VerificarAvisoLocators.causante_INP).send_keys(self.aviso['causante'])
            self.find_element(VerificarAvisoLocators.fechalimitepago_INP).send_keys(self.aviso['fechaLimite'])
        except TimeoutException:
            return

    def correcta_verificacion(self):
        return self.find_element(VerificarAvisoLocators.mensaje_MSJ).text

    def informo_publicacion(self):
        api = Parameters.get_ambiente()["urlAPI"] + "/api/v1/aviso/informar_publicacion"
        fecha_publicacion = self.aviso_erroneo["fechaPublicacion"].split("-")
        utils = Utils(dia=fecha_publicacion[2], mes=fecha_publicacion[1], anio=fecha_publicacion[0])
        r = requests.post(url=api, data=json.dumps(
            {"id": self.id_aviso, "publicaciones_id": "", "fecha_publicacion": utils.fecha_hoy_guion_invertida()}))
        print(r.json())
        return r.json()["status"]

    def cerrar_sesion(self):
        time.sleep(5)
        self.find_element(VerificarAvisoLocators.cerrar_sesion).click()

    def apruebo_aviso_manual(self):
        self.find_element(VerificarAvisoLocators.lupa_ult_aviso_BTN).click()
        self.find_element(VerificarAvisoLocators.aprobar_BTN).click()

    def estado_aviso(self):
        formatter = {"id_aviso": self.id_aviso}
        locator = VerificarAvisoLocators.TEMP_LOCATOR_ESTADO.formatear_locator(formatter)
        return self.find_element(locator).text

    def cierro_ventana(self):
        self.find_element(VerificarAvisoLocators.cierre_ventana_BTN).click()

    def modificar_campo_error(self, campo):
        func = "apruebo_" + self.tipo_aviso
        try:
            metodo = getattr(self, func)
            metodo()
        except AttributeError:
            print("No hay funcion especifica para aprobar este aviso")
        if campo == "dias":
            self.find_element(VerificarAvisoLocators.dias_INP).clear()
            self.find_element(VerificarAvisoLocators.dias_INP).send_keys(self.aviso_erroneo['cantDias'])
        if campo == "fecha":
            self.driver.execute_script('$("#AvisoVerificacionType_fechaPublicacion").val("")')
            time.sleep(2)
        if campo == "firma":
            time.sleep(2)
            self.driver.execute_script('$("#AvisoVerificacionType_fechaFirmaActoAdministrativo").val("")')
            time.sleep(2)
        if campo == "anio expediente":
            self.find_element(VerificarAvisoLocators.anio_exepdiente_INP).clear()
        if campo == "nro expediente":
            self.find_element(VerificarAvisoLocators.nro_expediente_INP).clear()

    def click_fecha(self):
        time.sleep(2)
        self.find_element(VerificarAvisoLocators.fecha_publicar_INP).click()
        time.sleep(1)

    def modificar_fecha(self):
        self.find_element(VerificarAvisoLocators.dia_31_BTN).click()


    def modificar_campo_bien(self, campo):
        if campo == "dias":
            self.find_element(VerificarAvisoLocators.dias_INP).clear()
            self.find_element(VerificarAvisoLocators.dias_INP).send_keys(self.aviso['cantDias'])
        if campo == "fecha":
            self.find_element(VerificarAvisoLocators.fecha_publicar_INP).send_keys(self.aviso_erroneo[
                                                                                       'fechaPublicacion'])
            time.sleep(2)
        if campo == "firma":
            time.sleep(2)
            self.find_element(VerificarAvisoLocators.fecha_firma_INP).send_keys(self.aviso_erroneo['fechaFirma'])
            time.sleep(3)
        if campo == "anio expediente":
            self.find_element(VerificarAvisoLocators.anio_exepdiente_INP).send_keys(self.aviso[
                                                                                        "anioExpedienteJudicial"])
        if campo == "nro expediente":
            self.find_element(VerificarAvisoLocators.nro_expediente_INP).send_keys(self.aviso["nroExpedienteJudicial"])

    # La bandeja de verificacion es previo a enviarlo a publicaciones, y el numero de publicacion debe ser 0
    def verificar_texto_pdf(self):
        time.sleep(2)
        regex = re.compile(r"N° [0-9]{1,8}/[0-9]{4}")
        contenido_text = pdf_utils.procesar_archivo()
        match = regex.search(contenido_text)
        match = match[0].replace("N° ", "")
        numero_publicacion = int(match.split('/')[0])
        return numero_publicacion == 0

    # Solo se usa para actas, pero no para presidencia por que no tiene dependencia
    def titulo_texto_organismo_sub(self, nombre_organismo, nombre_subdependencia):
        titulo = nombre_organismo + " - " + nombre_subdependencia
        contenido_text = pdf_utils.procesar_archivo()
        return contenido_text.find(titulo) >= 0

    def guardar_aviso(self):
        time.sleep(4)
        self.find_element(VerificarAvisoLocators.guardar_BTN).click()
        time.sleep(2)

    def visualizar_aviso(self):
        # self.find_element(VerificarAvisoLocators.verificacion_aviso(self.id_aviso)).click()
        formatter = {"id_aviso": self.id_aviso}
        locator = VerificarAvisoLocators.TEMP_VISUALIZAR_AVISO.formatear_locator(formatter)
        self.find_element(locator).click()
        time.sleep(2)

    def verificar_advertencia(self, campo):
        locator = {
            "dias": VerificarAvisoLocators.texto_dias_LBL,
            "fecha": VerificarAvisoLocators.texto_fecha_LBL,
            "firma": VerificarAvisoLocators.texto_firma_LBL,
            "anio expediente": VerificarAvisoLocators.anio_exp_jub_LBL,
            "nro expediente": VerificarAvisoLocators.nro_exp_jud_LBL
        }
        try:
            self.find_element(locator[campo])
            return True
        except TimeoutException:
            return False

    def aprobar_aviso(self):
        self.find_element(VerificarAvisoLocators.aprobar_BTN).click()

    def aprobar_aviso_error(self):
        time.sleep(3)
        self.find_element(VerificarAvisoLocators.aprobar_BTN).click()
        time.sleep(2)

    def aprobo_exito(self):
        time.sleep(10)
        return self.find_element(VerificarAvisoLocators.mensaje_MSJ).text

    def descargar_pdf_texto(self):
        time.sleep(4)
        self.scroll_to_element(VerificarAvisoLocators.descargar_texto_BTN)
        self.find_element(VerificarAvisoLocators.descargar_texto_BTN).click()
        i = FileUtils.aumentar_contador("contador_archivos")
        FileUtils.wait_for_pdf_to_download(number_of_files=i)

    def agrego_aviso_oa(self, nombre):
        time.sleep(2)
        self.find_select(VerificarAvisoLocators.suplemento_SEL).select_by_visible_text(nombre)

    def cambio_rubro(self, rubro):
        self.find_select(VerificarAvisoLocators.rubro_SEL).select_by_visible_text(rubro)