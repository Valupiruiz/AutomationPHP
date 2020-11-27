from config.parameters import Parameters
import json
from generated_data.data_manager import DataManager
from config.data.utils import Utils
import requests
from pathlib import Path

utils = Utils()


class NuevoAvisoAPI:
    def __init__(self, tipo, *parametros):
        self.tipo = tipo
        self.__parametros = parametros

    def envio_informacion(self):
        api = self.__parametros[1]["urlAPI"] + "/api/v1/aviso/crear"
        data = self.__parametros[0]
        r = requests.post(url=api, data=json.dumps(data))
        DataManager.set_id_aviso(r.json()["idAviso"])
        return r.json()["status"]

    # Tengo un pdf valido para crear un documento
    def creo_documento(self):
        path = str(Path(__file__).parents[2]) + '\\generated_data\\pdf.txt'
        api = self.__parametros[1]["urlAPI"] + "/api/v1/aviso/crear_documento"
        archivo = open(path, "r")
        r = requests.post(url=api, data=json.dumps(
            {"nombreDoc": "documento.pdf", "documento": archivo.read(), "id": DataManager.get_id_aviso()}))
        archivo.close()
        print(r.json())
        return r.json()["status"]

    # Se pueden enviar n anexos y cada uno debe tener un pdf valido
    def creo_anexos(self):
        aviso = Parameters.get_aviso_api(self.tipo)
        api = Parameters.get_ambiente()["urlAPI"] + "/api/v1/aviso/crear_anexo"
        path = str(Path(__file__).parents[2]) + '\\generated_data\\pdf.txt'
        archivo = open(path, "r")
        content = archivo.read()
        archivo.close()
        try:
            if aviso["nombresAnexos"] is None:
                print("No hay anexos")
            else:
                for x in aviso["nombresAnexos"].split(","):
                    r = requests.post(url=api, data=json.dumps(
                        {"id": DataManager.get_id_aviso(), "nombreAnexo": x, "anexo": content}))
                    print(r.json())
        except KeyError:
            print("No hay anexos")


    def agregar_aviso_oa_sup(self):
        Parameters.set_aviso_oa_sup(DataManager.get_id_aviso(), self._NuevoAvisoAPI__parametros[0].get('textoAPublicar'))