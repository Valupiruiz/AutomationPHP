import pytest
from filelock import FileLock

from src.config.config import RUTAS, LOCKS
from src.dominio.operable import Caja
from src.dominio.sucursal import Sucursal
from src.factory.sucursal import SucursalFactory, CajaFactory
from src.utils.files import get_codigo

lock = FileLock(LOCKS.FIXTURE)


@pytest.fixture
def crear_sucursal():
    # se utiliza para indicar si se debe crear en el sistema el dominio instanciado
    return True


@pytest.fixture
def cant_cajas():
    # se utiliza para indicar la cantidad de cajas que se van a crear
    return 1


@pytest.fixture
def cant_monedas():
    # se utiliza para indicar la cantidad de monedas con las que se van a crear las cajas
    return 3


@pytest.fixture
def cant_sucursales():
    # se utiliza para indicar la cantidad de sucursales que se van a crear
    return 1


@pytest.fixture
def generar_sucursal(context, worker_id, crear_sucursal,
                     cant_cajas, prefijo_sucursal, prefijo_caja,
                     cant_monedas, cant_sucursales):

    sucursal_factory = SucursalFactory(context.db, context.requests)
    caja_factory = CajaFactory(context.monedas)
    context.sucursales = []
    context.cajas = []
    with lock:
        print(f"\nInicio el thread {worker_id}")
        for _ in range(cant_sucursales):
            sucursal = sucursal_factory.build(prefijo_sucursal)
            cajas_temp = [caja_factory.build(prefijo_caja, cant_monedas) for _ in range(cant_cajas)]

            if crear_sucursal:
                print("Empiezo a crear una sucursal para ", worker_id)
                sucursal.agregar_cajas(*cajas_temp)
                sucursal_factory.create(context.administrador, sucursal)
                print("Termino de crear una sucursal para ", worker_id)
            else:
                context.cajas.append(cajas_temp)
            context.sucursales.append(sucursal)
    context.sucursal = context.sucursales[0]
