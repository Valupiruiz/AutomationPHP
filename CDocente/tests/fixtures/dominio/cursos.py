import pytest
from tests.fixtures import *
from utils.file_utils import project_path



@pytest.fixture
def tecnologia():
    return Curso('Educar con las nuevas tecnologías', '05/12/2014',
                 imagenes=[str(project_path.joinpath("cdocente_data", "img", "Manzana.jpg"))])


