import os
import json


class DataManager:

    @staticmethod
    def load_json():
        try:
            with open(os.path.join(os.path.dirname(__file__), 'data.json'), encoding='utf-8') as file:
                return json.load(file)
        except Exception as e:
            print("Error al intentar leer 'data.json':", e)

    @staticmethod
    def save_json(data):
        try:
            with open(os.path.join(os.path.dirname(__file__), 'data.json'), 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        except Exception as e:
            print("Error al intentar guardar en 'data.json':", e)

    @staticmethod
    def set_id_aviso(numero):
        data = DataManager.load_json()
        data['idAviso'] = numero
        DataManager.save_json(data)

    @staticmethod
    def set_tipoAviso(tipo):
        data = DataManager.load_json()
        data['tipoAviso'] = tipo
        DataManager.save_json(data)

    @staticmethod
    def get_tipoAviso():
        data = DataManager.load_json()
        return data['tipoAviso']

    @staticmethod
    def get_id_aviso():
        data = DataManager.load_json()
        return data['idAviso']


    @staticmethod
    def get_documento():
        data = DataManager.load_json()
        return data['documento']

    @staticmethod
    def get_firmante():
        data = DataManager.load_json()
        return data['firmante_inactivo']

    @staticmethod
    def set_firmante(nombre):
        data = DataManager.load_json()
        data['firmante_inactivo'] = nombre
        DataManager.save_json(data)

    @staticmethod
    def get_organismo():
        data = DataManager.load_json()
        return data['organismo']
