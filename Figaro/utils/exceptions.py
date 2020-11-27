class Custom(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return f"Hubo un error en una función interna. Mensaje:\n {self.mensaje}"


class FormatoDeFechaInvalida(Custom):
    def __init__(self):
        Custom.__init__(self, "Se esperaba una fecha con formato DD/MM/AAAA, pero se encontró otra")

