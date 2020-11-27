from page_objects.base_page import BasePage
from .properties.locators import BandejaTramitesLocators
from generated_data.data_manager import DataManager
import time
from config.data.db_utils import DBConnection
from config.data.db_utils import QuerySinResultadosException
from config.parameters import Parameters
from selenium.common.exceptions import TimeoutException
from config.queries import GET_FIRMANTES_AVISO, GET_ID_PUBLICACION
import pdf_utils
import re
import json
from utils.file_utils import FileUtils


NOMBRE_BASE = "BoraAdminProd_20200217"


class BandejaTramites(BasePage):
    def __init__(self, driver, id_aviso, aviso_erroneo, aviso, tipo_aviso):
        super().__init__(driver)
        self.id_aviso = id_aviso
        self.aviso_erroneo = aviso_erroneo
        self.aviso = aviso
        self.tipo_aviso = tipo_aviso

    def estado_aviso(self):
        formatter = {'id_aviso': self.id_aviso}
        locator = BandejaTramitesLocators.ESTADO_AVISO_TEMP.formatear_locator(formatter)
        return self.find_element(locator).text

    # Verifico que el firmante que me da la advertencia realmente resuelva el problema de que el aviso fue rechazado
    def firmante_inexistente(self):
        formatter = {'id_aviso': self.id_aviso}
        locator = BandejaTramitesLocators.ESTADO_AVISO_TEMP.formatear_locator(formatter)
        self.find_element(locator).click()
        self.find_element(BandejaTramitesLocators.MODAL_AVISO_DIV)
        self.scroll_to_element(BandejaTramitesLocators.motivo_rechazo_TXT)
        texto = self.driver.find_element(*BandejaTramitesLocators.motivo_rechazo_TXT).text
        DataManager.set_firmante(
            texto[texto.find("Los firmantes: ") + len("Los firmantes: "):texto.find("estan inactivos")])
        self.find_element(BandejaTramitesLocators.cierre_ventana_BTN).click()
        self.find_element(BandejaTramitesLocators.titulo_bandeja_LBL)

    def reprocesar_aviso(self):
        formatter = {'id_aviso': self.id_aviso}
        locator = BandejaTramitesLocators.REPROCESAR_AVISO_TEMP.formatear_locator(formatter)
        self.find_element(locator).click()
        self.find_element(BandejaTramitesLocators.motivo_rechazo_INP).send_keys("Reprocesado por la automatizacion")
        self.find_element(BandejaTramitesLocators.reprocesar_BTN).click()

    def reproceso_correctamente(self):
        time.sleep(2)
        return self.find_element(BandejaTramitesLocators.mensaje_MSJ).text


    def visualizar_aviso(self):
        formatter = {'id_aviso': self.id_aviso}
        locator = BandejaTramitesLocators.ESTADO_AVISO_TEMP.formatear_locator(formatter)
        self.find_element(locator).click()
        self.find_element(BandejaTramitesLocators.AVISO_LBL)

    # Con la configuracion de parametros (que aca la colocamos en el json inicial), el orden de los firmantes
    # de la base, y los firmantes de la creacion del aviso, debe coindicir y estar en orden
    #  por ej: si la configuracion e MMACRI, MICCHETTI y PEÑA y le enviamos pepito-Micchetti-Macri
    # en la base el orden debe ser Macri-Micchetti-pepito
    def verificar_orden_firmantes(self):
        formatter = {'id_aviso': self.id_aviso}
        locator = BandejaTramitesLocators.ESTADO_AVISO_TEMP.formatear_locator(formatter)
        self.find_element(locator).click()
        # Conexiones de db no es muy recomendable abrirlas en los page objects
        conexion = DBConnection("{MySQL ODBC 8.0 Unicode Driver}", "10.2.1.112", "root", None, NOMBRE_BASE)
        firmantes_aviso = self.aviso['firmantes']
        lista_firmantes_ordenada = Parameters.get_ambiente()["ordenFirmante"]

        try:
            id_aviso = str(self.id_aviso)
            resultado = conexion.execute_query_and_return_rows(GET_FIRMANTES_AVISO, id_aviso)
            print(resultado)
            lista_firmantes_aviso = [v for d in resultado for k, v in d.items()]
            if len(firmantes_aviso) == len(firmantes_aviso.split("-")):
                return False

            lista_intersectada_db = [firmante for firmante in lista_firmantes_aviso if
                                     firmante in lista_firmantes_ordenada]
            lista_intersectada_parametros = [firmante for firmante in lista_firmantes_ordenada if
                                             firmante in lista_intersectada_db]
            configurarcion_firmantes_aviso = [firmante for firmante in lista_firmantes_ordenada if firmante in
                                              lista_firmantes_aviso]

            if len(configurarcion_firmantes_aviso) != len(lista_intersectada_db):
                return False
            return lista_intersectada_db == lista_intersectada_parametros
        except QuerySinResultadosException as e:
            print("Error en la query, no hubo resultados", e)
            return False

    # Solo se usa para actas, pero no para presidencia por que no tiene dependencia
    def titulo_texto_organismo_sub(self, nombre_organismo, nombre_subdependencia):
        titulo = nombre_organismo + " - " + nombre_subdependencia
        contenido_text = pdf_utils.procesar_archivo()
        return contenido_text.find(titulo) >= 0

    # Sino existe el documento se abre una pantalla html de error, trata de encontrarla
    def verificar_existencia_documentos(self):
        self.wait_and_switch_to_new_window(1)
        try:
            self.find_element(BandejaTramitesLocators.doc_no_existe_LBL)
            self.switch_to_default_content()
            return False
        except TimeoutException:
            pass
        self.wait_and_switch_to_new_window(2)
        try:
            self.find_element(BandejaTramitesLocators.doc_no_existe_LBL)
            self.switch_to_default_content()
            return False
        except TimeoutException:
            pass
        self.switch_to_default_window()
        return True

    def descargar_pdf_documento(self):
        self.find_element(BandejaTramitesLocators.decargar_doc_BTN, 30).click()
        i = FileUtils.aumentar_contador("contador_archivos")
        FileUtils.wait_for_pdf_to_download(number_of_files=i)
        time.sleep(2)

    # Siempre agarra el ultimo descargado
    def verificar_existencia_pdf_documento(self, resumen_contenido):
        contenido_text = pdf_utils.procesar_archivo()
        print(contenido_text)
        return contenido_text.find(resumen_contenido) >= 0

    # El numero de publicaciones debe ser el mismo que el pdf del texto
    def verificar_texto_pdf(self):
        self.find_element(BandejaTramitesLocators.documento_aviso_LBL)
        try:
            regex = re.compile(r"N° [0-9]{1,8}/[0-9]{4}")
            contenido_texto = pdf_utils.procesar_archivo()
            match = regex.search(contenido_texto)
            match = match[0].replace("N° ", "")
            numero_publicacion = match.split('/')[0]
            conexion = DBConnection("{MySQL ODBC 8.0 Unicode Driver}", "10.2.1.112", "root", None,
                                    NOMBRE_BASE)

            resultado = conexion.execute_query_and_return_rows(GET_ID_PUBLICACION, self.id_aviso)
            metadata = resultado[0]["metadata"]
            metadata_dict = json.loads(metadata)
            numero_publicacion_base = (metadata_dict[0]["publicaciones_numero_anio"]).split("/")[0]
        except Exception as e:
            print(e)
            raise e
        print("numeros", numero_publicacion_base, numero_publicacion)
        return numero_publicacion_base == numero_publicacion

    # Por ser un escenario outline siempre llama a lo mismo y de acuerdo al campo realiza las acciones, y lo modifica
    # A un valor que termine dando error, para luego verificar si da las advertencias correctas
    def modificar_campo_error(self, campo):
        if campo == "dias":
            time.sleep(5)
            self.find_element(BandejaTramitesLocators.dias_INP).clear()
            self.find_element(BandejaTramitesLocators.dias_INP).send_keys(self.aviso_erroneo['cantDias'])
            time.sleep(2)
        if campo == "fecha":
            time.sleep(2)
            self.driver.execute_script('$("#AvisoVerificacionType_fechaPublicacion").val("")')
            time.sleep(2)
        if campo == "firma":
            time.sleep(2)
            self.driver.execute_script('$("#AvisoVerificacionType_fechaFirmaActoAdministrativo").val("")')
            time.sleep(2)

    def guardar_aviso(self):
        time.sleep(4)
        self.scroll_to_element(BandejaTramitesLocators.guardar_Pend_PUB_BTN)
        self.find_element(BandejaTramitesLocators.guardar_Pend_PUB_BTN).click()

    def guardo_correctamente(self):
        time.sleep(2)
        return self.find_element(BandejaTramitesLocators.mensaje_MSJ).text == "Se edito con éxito el aviso"

    # Por ser un escenario outline siempre llama a lo mismo y de acuerdo al campo tiene diferentes advertencias
    def verificar_advertencia(self, campo):
        locator = {
            "dias": BandejaTramitesLocators.texto_dias_LBL,
            "fecha": BandejaTramitesLocators.texto_fecha_LBL,
            "firma": BandejaTramitesLocators.texto_firma_LBL,
            "anio expediente": BandejaTramitesLocators.anio_exp_jub_LBL,
            "nro expediente": BandejaTramitesLocators.nro_exp_jud_LBL
        }
        try:
            self.find_element(locator[campo])
            return True
        except TimeoutException:
            return False

    # Por ser un escenario outline siempre llama a lo mismo y de acuerdo al campo realiza las acciones
    def modificar_campo_bien(self, campo):
        if campo == "dias":
            self.find_element(BandejaTramitesLocators.dias_INP).clear()
            self.find_element(BandejaTramitesLocators.dias_INP).send_keys(self.aviso['cantDias'])
        if campo == "fecha":
            self.find_element(BandejaTramitesLocators.fecha_publicar_INP).send_keys(self.aviso_erroneo['fechaPublicacion'])
            time.sleep(2)
        if campo == "firma":
            time.sleep(2)
            self.find_element(BandejaTramitesLocators.fecha_firma_INP).send_keys(self.aviso_erroneo['fechaFirma'])
            time.sleep(3)

    def apruebo_req_aprobacion(self):
        self.find_element(BandejaTramitesLocators.apruebo_BTN).click()

    def descargar_pdf_texto(self):
        time.sleep(3)
        self.scroll_to_element(BandejaTramitesLocators.decargar_doc_BTN)
        self.find_element(BandejaTramitesLocators.descargar_texto_BTN).click()
        i = FileUtils.aumentar_contador("contador_archivos")
        FileUtils.wait_for_pdf_to_download(number_of_files=i)

    def agrego_avisos_oa(self, oa_sup):
        for x in oa_sup["id_avisos"].split(","):
            self.id_aviso = x
            self.visualizar_aviso()
            self.agrego_aviso_oa(oa_sup["nombre"])
            self.guardar_aviso()
            self.guardo_correctamente()
            self.visualizar_aviso()
            self.apruebo_req_aprobacion()
            self.guardo_correctamente()

    def agrego_aviso_oa(self, nombre):
        self.find_select(BandejaTramitesLocators.suplemento_SEL).select_by_visible_text(nombre)







