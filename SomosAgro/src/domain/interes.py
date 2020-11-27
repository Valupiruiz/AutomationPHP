from typing import List


class Interes:
    def __init__(self, nombre, subintereses: List[str]):
        self.nombre = nombre
        self.subintereses = subintereses

    @classmethod
    def from_json(cls, data):
        return cls(**data)
