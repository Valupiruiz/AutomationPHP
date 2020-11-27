from src.utils.exceptions import CabeceraInvalidaException, CantidadDiasNoValidosException
from src.domain.interes import Interes
import random
import unidecode


class Publicacion:
    def __init__(self, tipo: str, cantidad_dias: int, cabecera: "CabeceraPublicacion", interes: Interes, zona: str):
        self.tipo = tipo
        if tipo == TipoPublicacion.GRATUITA and cabecera.descripcion is not None:
            raise CabeceraInvalidaException("Si la publicación es gratuita, no puede tener descripción")
        if cantidad_dias > 15 and tipo == TipoPublicacion.GRATUITA:
            raise CantidadDiasNoValidosException("Si la publicación es gratuita no puede ser de más de 15 días")
        self.cabecera = cabecera
        self.cantidad_dias = cantidad_dias
        self.interes = interes
        self.subinteres = random.choice(interes.subintereses)
        self.zona = zona

    @classmethod
    def from_json(cls, data):
        cabecera = CabeceraPublicacion.from_json(data["cabecera"])
        interes = Interes.from_json(data["interes"])
        return cls(data["tipo"], data["cantidad_dias"], cabecera, interes, data["zona"])

    @property
    def ipseudonimo(self):
        subinteres = self.subinteres
        subinteres = unidecode.unidecode(subinteres)
        subinteres = subinteres.lower().replace(" ", "-")
        return subinteres if self.subinteres is not "Otros" else \
            f"{subinteres}-{unidecode.unidecode(self.interes.nombre)}"


class CabeceraPublicacion:
    def __init__(self, titulo: str, sintesis: str, descripcion: str = None):
        self.titulo = titulo
        self.sintesis = sintesis
        self.descripcion = descripcion

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class TipoPublicacion:
    GRATUITA = "Gratuita"
    PREMIUM = "Premium"
