from abc import ABC

from src.page_objects.base.base_page import BasePage
from src.utils.asserts import Assert
from src.utils.db_utils import Db
from src.utils.requests import Request


class BaseAction(ABC):

    def __init__(self, context):
        self.page = context.page
        self.db: Db = context.db
        self.api: Request = context.requests
        self._assert = Assert()

    def verify_state(self, *args):
        # Verificar el estado de la aplicacion, por ejemplo,
        # validar que nos encontramos en la pantalla correcta
        raise NotImplementedError()

    def do(self, *args):
        # Realizar la accion propiamente dicha, por ejemplo,
        # completar un formulario y guardar
        raise NotImplementedError()

    def success(self, *args):
        # Validar un estado correcto luego de la accion, por ejemplo,
        # un mensaje de exito
        raise NotImplementedError()

    def failure(self, *args):
        # Validar un estado incorrecto (a nivel negocio) luego de la accion, por ejemplo,
        # un mensaje indicando que no se pudo guardar por X condicion referente al negocio
        raise NotImplementedError()
