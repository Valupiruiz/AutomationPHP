from src.config.config import RUTAS
from src.dominio.operable import Caja
from src.dominio.sucursal import Sucursal
from src.utils.db_utils import Db
from src.utils.files import get_codigo
from src.utils.requests import Request


class SucursalFactory:

    def __init__(self, db: Db, request: Request):
        self._db = db
        self._request = request

    def build(self, prefijo):
        # Solo se encarga de instanciar la sucursal
        num_suc = get_codigo(RUTAS.NUMEROS_CODIGOS, "Sucursal")
        sucursal = Sucursal(f"Argenper {num_suc:04}", f"{prefijo}{num_suc:04}")
        sucursal.provincia.id = self._db.get_provincia(sucursal.provincia.nombre)['id']
        return sucursal

    def create(self, administrador, sucursal):
        # Se encarga de crear las sucursales con sus respectivas cajas en el SUT
        response = self._request.login(administrador)
        assert response.ok, f"Hubo un problema al loguearse, {response}"
        response = self._request.crear_sucursal(sucursal)
        assert response.ok, f"Hubo un problema al crear la sucursal, {response}"
        id_suc = self._db.get_id_sucursal(sucursal.codigo)
        for c in sucursal.cajas:
            response = self._request.crear_caja(id_suc, c)
            c.id = self._db.get_id_caja(c.codigo)
            assert response.ok, f"Hubo un problema al crear la caja {response}"


class CajaFactory:

    def __init__(self, monedas):
        self._monedas = monedas

    def build(self, prefijo, cant_monedas):
        num_caja = get_codigo(RUTAS.NUMEROS_CODIGOS, "Caja")
        return Caja(f"{prefijo}{num_caja:04}", self._monedas[-cant_monedas:])
