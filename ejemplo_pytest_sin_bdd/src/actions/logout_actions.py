from src.actions.base.base_action import BaseAction
import time

class LogoutAction(BaseAction):

    def verify_state(self, usuario):
        self.page.menu_roles()
        rol_actual = self.page.rol_actual()
        self._assert.that(usuario.rol).equals(rol_actual)
        return self

    def do(self):
        self.page.cerrar_sesion()
        return self

    def success(self):
        self.page.validar_usuario_sin_sesion()

    def failure(self):
        pass
