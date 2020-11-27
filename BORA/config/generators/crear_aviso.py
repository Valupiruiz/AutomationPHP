import os
import json
from config.data.enums import *


"""Archivo de configuración para un Proceso de Compras sin modalidad."""

__data = {
    "ambiente":
        {
            "url": "http://10.2.1.112:8081",
        },
    "usuarios":
        {
            "administrador": ["admin"],
            "contrasena": "1234"
        },
    "aviso":
        {
            "seccion": "26",
            "rubro": "472",
            "tipoAviso": 2506,
            "diasPublicar": 3,
            "formaPago": 26,
            "archivo": "C:\\Users\\vruiz\Downloads\\primera.pdf",
            "dia": "02/05/2019"
        }}


try:
    with open(os.path.join(os.path.dirname(__file__), r'JSONS\crear_aviso.json'), 'w', encoding='utf-8') as file:
        json.dump(__data, file, indent=4, ensure_ascii=False)
        print("El archivo 'sin_modalidad.json' generado correctamente.")
except Exception as e:
    print("Error al intentar ejectuar 'Crear_aviso.py':", e)
