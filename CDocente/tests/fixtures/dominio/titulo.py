import pytest
from tests.fixtures import *
from utils.file_utils import project_path


@pytest.fixture
def bachiller_comunicacion():
    return Titulo('Bachiller en Ciencias de la Educacion', '05/12/2014', Nivel.SECUNDARIO,
                  imagenes=[str(project_path.joinpath("cdocente_data", "img", "Manzana.jpg"))])

@pytest.fixture
def maestro_primaria():
    return Titulo('Maestro de Enseñanza Primaria', '05/12/2014', Nivel.SECUNDARIO,
                  imagenes=[str(project_path.joinpath("cdocente_data", "img", "Manzana.jpg"))], sin_secundario=True)
