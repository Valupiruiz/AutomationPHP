from pathlib import Path
import time
import json
import os


project_path = Path(__file__).parent.parent
carpeta_data = "config"


class FileUtils:
    @staticmethod
    def guardar_json(data, nombre_archivo):
        path_destino = str(project_path.joinpath(carpeta_data, "jsons"))
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
        path_origen = str(project_path.joinpath(carpeta_data, "jsons", f"{nombre_archivo}.json"))
        try:
            with open(path_origen, 'r+', encoding="utf-8") as f:
                return json.load(f)
        except IOError as e:
            print(f"\nEl archivo {nombre_archivo}.json no existía. Creando...")
            f = open(path_origen, 'w', encoding="utf-8")
            f.close()
            return {}
        except json.JSONDecodeError as e:
            print(e, f"\nEl archivo {nombre_archivo}.json tiene un formato inválido")

    @staticmethod
    def agregar_claves_a_json(data, nombre_archivo):
        info = data
        existente = FileUtils.cargar_json(nombre_archivo)
        if existente:
            info = {**existente, **data}
        FileUtils.guardar_json(info, nombre_archivo)

    @staticmethod
    def wait_for_pdf_to_download(timeout=45, number_of_files=None):
        path_to_pdf = Path.joinpath(project_path, 'PDFs')
        end_time = time.time() + timeout
        seguir_esperando = True
        while seguir_esperando:
            seguir_esperando = False
            p = path_to_pdf.glob('**/*')
            files = [f for f in p if f.is_file()]
            if number_of_files and number_of_files is not len(files):
                seguir_esperando = True
                continue
            for file in files:
                if str(file).endswith('.crdownload'):
                    seguir_esperando = True
                    if time.time() > end_time:
                        break

    @staticmethod
    def aumentar_contador(clave):
        data_actual = FileUtils.cargar_json("contador")
        contador = int(data_actual[clave]) + 1
        data_actual[clave] = contador
        FileUtils.guardar_json(data_actual, "contador")
        return contador
