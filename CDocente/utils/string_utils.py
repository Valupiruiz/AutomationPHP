from typing import List
from utils.exceptions import FormatoDeFechaInvalida
import random



class StringUtils:
    @staticmethod
    def descomponer_fecha_en_atomos(fecha: str) -> List[str]:
        """
        Dada una fecha en formato DD/MM/AAAA, la descompongo en una tupla de año, mes y dia
        Args:
            fecha: contiene la fecha en formato DD/MM/AAAA

        Returns:
            Tuple[str, str, str]

        """
        lista_componentes: List[str] = fecha.split("/")
        if len(lista_componentes) is not 3:
            raise FormatoDeFechaInvalida
        return lista_componentes

    @staticmethod
    def generate_word():
        c = 'bcdfghjklmnpqrstvwxyzaeiou'
        palabra = ''
        for i in range(10):
            palabra = palabra + random.choice(c)
        return palabra

    @staticmethod
    def generate_num(cant):
        c = '123456789'
        numeros = ''
        for i in range(cant):
            numeros = numeros + random.choice(c)
        return numeros
