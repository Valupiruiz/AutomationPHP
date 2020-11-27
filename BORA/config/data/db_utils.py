import pyodbc
from pyodbc import OperationalError as OperationalError
import re
from .exceptions import *


class DBConnection:
    def __init__(self, driver, ip, usuario, contrasenia, db):
        """
        :param driver: parametro de tipo string con el motor de base de datos/driver
        :param ip: parametro de tipo string con la IP del servidor
        :param usuario: usuario de tipo string
        :param contrasenia: contrasenia de tipo string
        :param db: base de datos a consultar, tipo string
        """
        try:
            self.validar_driver(driver)
            self.handler = pyodbc.connect(f'DRIVER={driver};SERVER={ip};port=3318;DATABASE={db};UID={usuario};')
        except DriverNoExistenteException as de:
            print(de)
        except OperationalError as oe:
            print("No se pudo conectar con la base de datos, revisar los parámetros de conexión", oe)

    def execute_query_and_return_rows(self, query, *args):
        """
        :param query: recibe un string con la query a querer consultar
        :return: una lista con tuplas, donde cada elemento de la tupla es el dato de una columna
        y la lista devuelve las filas
        """
        cursor = self.handler.cursor()
        cursor.execute(query, *args)
        print("query", query)
        columnas = [column[0] for column in cursor.description]
        rows = list()

        for row in cursor.fetchall():
            rows.append(dict(zip(columnas, row)))
        cursor.close()
        del cursor
        if not rows:
            raise QuerySinResultadosException(
                "No hubo resultados para la query, revisar las condiciones "
                "del where/having y si el dato a buscar existe")
        return rows

    def close_connection(self):
        self.handler.close()

    @staticmethod
    def validar_driver(driver):
        driver_validator = re.sub('[{|}]', "", driver)
        if driver_validator not in pyodbc.drivers():
            raise DriverNoExistenteException(
                "No se encontro el driver para conectarse con la DB. Revise la sintaxis o instalelo")
