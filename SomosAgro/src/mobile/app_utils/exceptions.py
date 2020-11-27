"""
Este archivo es de excepciones del framework de automatización mobile. Se sugiere no modificar las clases que ya
existen
"""


class CysAppium(Exception):
    def __init__(self, mensaje, activity=None, stack=None, *args):
        self.mensaje = mensaje
        self.activity = activity
        self.stack = stack
        self.args = args

    def __str__(self):
        informe = "Hubo un error durante la ejecución: {0}\n".format(self.mensaje)
        if self.activity is not None:
            informe += "El error ocurrió en el activity: {0}\n".format(self.activity)
        if self.stack is not None:
            informe += "¡**Stacktrace**!:\n{0}".format(self.stack)
        return informe


class ElementoNoVisible(CysAppium):
    pass


class ElementoNoEncontrado(CysAppium):
    pass
