import pytest
from filelock import FileLock

from src.config.config import LOCKS


@pytest.fixture
def lock_boveda():
    # la boveda es unica, asique no se podrian correr test en los cuales se la involucre de manera paralela.
    # Lo hago como fixture porque si bien puede que no sea la mejor herramienta,
    # es mas limpio que agregar el with en el test propiamente dicho

    with FileLock(LOCKS.BOVEDA):
        yield
