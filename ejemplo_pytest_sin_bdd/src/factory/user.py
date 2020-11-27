from src.dominio.usuario import TiposUsuario, Usuario
from src.utils.db_utils import QueryResultNotFoundException


class CajerosBuilder:

    def __init__(self, num_worker):
        self._tipo = TiposUsuario.CAJERO
        self._template_nombre = "Cajero {numero}"
        self._apellido = f"de {num_worker}"
        self._template_mail = f"jrodriguez+cajero{{numero}}{num_worker}@cys.com.ar"
        self._template_dni = 10000000 + num_worker
        self._password = "12345678"

    def build(self, cantidad):
        cajeros = []
        for i in range(1, cantidad + 1):
            cajeros.append(Usuario(self._template_nombre.format(numero=i),
                                   self._apellido,
                                   self._template_mail.format(numero=i),
                                   self._template_dni + i,
                                   self._password,
                                   self._tipo))
        return cajeros


class UserFactory:

    def __init__(self, db, num_worker):
        self._db = db
        self.cajeros_builder = CajerosBuilder(num_worker)

    def build_cajeros(self, cantidad):
        return [self._create_user(user) for user in self.cajeros_builder.build(cantidad)]

    def build_administrador(self):
        return self._create_user(Usuario("Administrador", "Test", "jrodriguez@cys.com.ar",
                                         123456789, "12345678", TiposUsuario.ADMINISTRADOR))

    def build_operador_boveda(self):
        return self._create_user(Usuario("Operador boveda", "Test", "jrodriguez+boveda@cys.com.ar",
                                         "012345678", "12345678", TiposUsuario.OPERADOR_BOVEDA))

    def build_operaciones(self):
        return self._create_user(Usuario("Usuario", "Operaciones", "jrodriguez+operaciones@cys.com.ar",
                                         "123456789", "12345678", TiposUsuario.OPERACIONES))

    def _create_user(self, user):
        try:
            self._db.get_usuario(user)
        except QueryResultNotFoundException:
            user_id = self._db.crear_usuario(user)
            user.id = user_id
        return user
