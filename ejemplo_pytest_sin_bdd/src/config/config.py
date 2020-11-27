from os.path import join
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent


class RUTAS:
    NUMEROS_CODIGOS = join(ROOT, 'src/config/numeros_codigos.json')


class LOCKS:
    CONFTEST = join(ROOT, "conftest.lock")
    DRIVER = join(ROOT, "driver.lock")
    FIXTURE = join(ROOT, "fixture.lock")
    DB = join(ROOT, "db.lock")
    BOVEDA = join(ROOT, "boveda.lock")