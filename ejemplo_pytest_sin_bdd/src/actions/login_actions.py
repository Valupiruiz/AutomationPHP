from src.actions.base.base_action import BaseAction
from src.dominio.usuario import TiposUsuario


class LoginAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._usuario = None

    def verify_state(self):
        self.page.validar_usuario_sin_sesion()
        return self

    def do(self, usuario, operable=None):
        _login(self, usuario, operable)
        return self

    def success(self, pagina):
        self.page.redirigir(pagina)

    def failure(self):
        pass


# Esto podria ser un failure del LoginAction, pero el metodo del loginpage tendria que aceptar None
# o modificar de algun tipo de manera el do para que no ingrese el usuario :shrug:
class LoginIncorrectoAction(BaseAction):

    def verify_state(self):
        self.page.validar_usuario_sin_sesion()
        return self

    def do(self):
        self.page.click_login()
        return self

    def success(self):
        self.page.validar_campos_obligatorios()

    def failure(self):
        pass


class OperadorSinOperableLoginAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._usuario = None

    def verify_state(self):
        self.page.validar_usuario_sin_sesion()
        return self

    def do(self, usuario, desasignar_cajero=True):
        if desasignar_cajero:
            self.db.desasignar_cajero(usuario)
        self.page.iniciar_sesion(usuario)
        self._usuario = usuario
        return self

    def success(self):
        if self._usuario.tipo == TiposUsuario.CAJERO:
            mensaje = "No tiene cajas asociadas."
            pagina = "Caja no asociada"
        else:
            mensaje = "No tiene bóveda asociada."
            pagina = "Boveda no asociada"

        self.page.redirigir(pagina)
        self._assert.that(mensaje).equals(self.page.titulo_operable_sin_asignar())

    def failure(self):
        pass


class OperadorSinAccionesLoginAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._usuario = None
        self._caja = None

    def verify_state(self, caja):
        self._caja = caja
        self.page.validar_usuario_sin_sesion()
        self._assert.that(len(caja.monedas_permitidas)).equals(0)
        return self

    def do(self, usuario):
        _login(self, usuario, self._caja)
        return self

    def success(self):
        self.page.redirigir("Apertura Caja")
        self._assert.that(f"La {self._caja.tipo.lower()} {self._caja.codigo} no posee operaciones habilitadas") \
            .equals(self.page.alerta_sin_operaciones())
        self._assert.that(f"No podrá operar con esta {self._caja.tipo.lower()}.") \
            .equals(self.page.mensaje_sin_operaciones())
        self._assert.that("Para habilitarlas comuníquese con el área correspondiente al 1234-1234") \
            .equals(self.page.mensaje_habilitar_operaciones_caja())
        self.page.mensaje_habilitar_operaciones_caja()

    def failure(self):
        pass


def _login(self, usuario, operable=None):
    if operable is not None:
        self.db.asignar_operador(usuario, operable.codigo)
    self.page.iniciar_sesion(usuario)
    self._usuario = usuario
