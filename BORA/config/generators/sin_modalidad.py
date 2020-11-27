import os
import json
from config.data.enums import *


"""Archivo de configuración para un Proceso de Compras sin modalidad."""

__data = {
    "ambiente":
        {
            "url": "http://10.2.1.124:8190/",
            "estadosPliego": "PLIEGO/_estadosPliego.aspx"
        },
    "usuarios":
        {
            "proveedor": ["cimes", "nesdar", "fischetti", "federico"],
            "comprador": {
                "adminRIUPP": "AdminRIUPP",
                "adminUCA": "AdminUCA{UOA}".format(UOA=601),
                "analistaOGEPU": "AnalistaOGEPU",
                "analistaOGESE": "AnalistaOGESE{UOA}".format(UOA=6001),
                "analistaSG": "AnalistaSG{UE}".format(UE=623),
                "autorizadorOGEPU": "AutorizadorOGEPU",
                "autorizadorPL": "AutorizadorPL{UE}".format(UE=623),
                "autorizadorSG": "AutorizadorSG{UE}".format(UE=623),
                "coordinadorSubasta": "CoordinadorSubasta{UOA}".format(UOA=601),
                "evaluador1": "Evaluador1_{UE}".format(UE=623),
                "evaluador2": "Evaluador2_{UE}".format(UE=623),
                "evaluador3": "Evaluador3_{UE}".format(UE=623),
                "evaluadorCAP": "EvaluadorCAP",
                "evaluadorFinal": "EvaluadorFinal",
                "gestor": "Gestor{UE}".format(UE=623),
                "opMesaAyuda": "OPMesaAyuda{UOA}".format(UOA=601),
                "recepcionista": "Recepcionista{UE}".format(UE=623),
                "solicitanteSG": "SolicitanteSG{UE}".format(UE=623),
                "subsecretarioOGEPU": "SubsecretarioOGEPU",
                "supervisor": "Supervisor{UE}".format(UE=623)
            },
            "contrasena": "12345678"
        },
    "documento":
        {
            "adjunto": "C:\\Users\\vruiz\Downloads\\primera.pdf"
        },
    "SG":
        {
            "tipoUrgencia": TipoUrgencia.normal.value,
            "esJuegosOlimpicos": True,
            "tieneAnticipoFinanciero": False,
            "items": ["08.01.002.0006.1", "18.10.002.0006.1", "08.03.002.0002.5", "08.03.002.0002.6",
                      "08.03.002.0003.3", "06.03.001.0002.17", "08.03.002.0002.1", "06.03.001.0002.8",
                      "06.03.001.0003.3", "06.03.002.0003.1"],
            "cantidadItems": 2,
            "cantidadItemsEntrega": 9,
            "tipoEmpaquetamiento": "UNIDADES",
            "cantidadEmpaquetamiento": "11",
            "precioUnitario": 137.69
        }
}

try:
    with open(os.path.join(os.path.dirname(__file__), r'JSONS\sin_modalidad.json'), 'w', encoding='utf-8') as file:
        json.dump(__data, file, indent=4, ensure_ascii=False)
        print("El archivo 'sin_modalidad.json' generado correctamente.")
except Exception as e:
    print("Error al intentar ejectuar 'sin_modalidad.py':", e)
