import json
from pathlib import Path
import os

project_path = Path(__file__).parent.parent.parent
project_src_path = Path(__file__).parent.parent

carpeta_data = "sag_data"


class FileUtils:
    @staticmethod
    def guardar_json(data, nombre_archivo):
        path_destino = str(project_path.joinpath("src", carpeta_data, "jsons"))
        if not os.path.exists(str(path_destino)):
            os.mkdir(path_destino)
        path_destino = Path(path_destino).joinpath(f"{nombre_archivo}.json")
        try:
            with open(str(path_destino), mode="w+", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(e, f"\nNo se pudo escribir el archivo {nombre_archivo}, verifique la ruta")
            print(f"RUTA: {path_destino}")

    @staticmethod
    def cargar_json(nombre_archivo):
        path_origen = str(project_path.joinpath("src", carpeta_data, "jsons", f"{nombre_archivo}.json"))
        try:
            with open(path_origen, 'r+', encoding="utf-8") as f:
                return json.load(f)
        except IOError as e:
            print(e, f"\nNo se pudo cargar el archivo {nombre_archivo}.json, verificar la ruta", )
            print(f"RUTA: {path_origen}")
        except json.JSONDecodeError as e:
            print(e, f"\nEl archivo {nombre_archivo}.json tiene un formato inválido")

    @staticmethod
    def agregar_claves_a_json(data, nombre_archivo):
        info = data
        existente = FileUtils.cargar_json(nombre_archivo)
        if existente:
            info = {**existente, **data}
        FileUtils.guardar_json(info, nombre_archivo)
