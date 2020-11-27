"""
En este archivo están las excepciones generales para las dos aplicaciones, tanto web como mobile
"""


class DominioException(Exception):
    pass


class CabeceraInvalidaException(DominioException):
    pass


class CantidadDiasNoValidosException(DominioException):
    pass

