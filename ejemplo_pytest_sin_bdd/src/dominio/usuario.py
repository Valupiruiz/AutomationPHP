class Usuario:

    def __init__(self, nombre, apellido, mail, dni, password, rol):
        self.tipo = rol
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.dni = dni
        self.password = password
        self.id = None

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    @property
    def rol(self):
        return self.tipo['front']


class TiposUsuario:
    CAJERO = {"db": "OPERADOR_CAJA", "front": "Rol Operador caja"}
    ADMINISTRADOR = {"db": "ADMINISTRACION", "front": "Rol Administracion"}
    OPERADOR_BOVEDA = {"db": "OPERADOR_BOVEDA", "front": "Rol Operador boveda"}
    OPERACIONES = {"db": "OPERACIONES", "front": "Rol Operaciones"}
