from abc import ABC
import abc
from decimal import Decimal, ROUND_HALF_UP
import math


class RedondeoStrategy:
    """
    Clase de tipo Strategy para redondear según un tipo de redondeo
    """
    def __init__(self, tipo: "Redondeo"):
        self.tipo = tipo

    def redondear(self):
        self.tipo.redondear()


class Redondeo(ABC):
    """
    Clase abstracta para tratar de igual forma los tipos de redondeo
    """
    @abc.abstractmethod
    def redondear(self, numero: Decimal):
        raise NotImplementedError


class CuarentaNueveArriba(Redondeo):
    def redondear(self, numero: Decimal):
        parte_entera = Decimal(math.modf(numero)[1])
        parte_decimal = Decimal(math.modf(numero)[0]).quantize(Decimal('0.01'))
        return parte_entera + 1 if parte_decimal >= Decimal('0.49') else parte_entera


class CincuentaArriba(Redondeo):
    def redondear(self, numero: Decimal):
        return numero.quantize(Decimal('1'), rounding=ROUND_HALF_UP)


class Truncar(Redondeo):
    def redondear(self, numero: Decimal):
        return numero
