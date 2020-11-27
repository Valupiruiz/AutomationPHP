from config.parameters import Parameters
from page_objects.base_page import BasePage
from .properties.locators import OA_Suplementos_locators
import re
import time
from utils.file_utils import FileUtils
from config.data.utils import Utils
import pdf_utils


utils = Utils()


class OASuplemento(BasePage):
    def __init__(self, driver, oa_sup):
        super().__init__(driver)
        self.oa_sup = oa_sup

    def crear_orden(self):
        self.find_element(OA_Suplementos_locators.fecha_publicacion_INP).send_keys(self.oa_sup["fecha"])
        self.find_element(OA_Suplementos_locators.crear_oa_BTN).click()
        # Guardo el nombre de la orden para luego poder buscarlo
        titulo = self.find_element(OA_Suplementos_locators.titulo_LBL).text
        regex = re.compile(r"Suplemento [0-9]")
        match = regex.search(titulo)
        print('match: ', match)
        Parameters.set_nombre_oa_sup(match[0])

    def visualizar_orden_sup(self):
        formatter = {"fecha": self.oa_sup["fecha"],
                     "nombre": self.oa_sup["nombre"]}
        locator = OA_Suplementos_locators.visualizar_oa_TEMP.formatear_locator(formatter)
        self.find_element(locator).click()

    def cambio_nro_edicion(self):
        self.find_element(OA_Suplementos_locators.nro_edicion_INP).clear()
        self.find_element(OA_Suplementos_locators.nro_edicion_INP).send_keys(self.oa_sup["nro_edicion"])

    def guardar_orden(self):
        self.find_element(OA_Suplementos_locators.guardar_BTN).click()
        return self.find_element(OA_Suplementos_locators.alert_LBL).text

    def descargar_pdf_oa(self):
        self.find_element(OA_Suplementos_locators.ver_pdf_BTN, 30).click()
        i = FileUtils.aumentar_contador("contador_archivos")
        FileUtils.wait_for_pdf_to_download(number_of_files=i)
        time.sleep(2)

    def verificar_contenido_oa(self):
        contenido_text = pdf_utils.procesar_archivo()
        for x in self.oa_sup["textos"].split(","):
            if not contenido_text.find(x) >= 0:
                return False
        nro_edicion = "{:,}".format(int(self.oa_sup["nro_edicion"])).replace(',','~').replace('.',',').replace('~','.')
        return contenido_text.find(nro_edicion) >= 0

