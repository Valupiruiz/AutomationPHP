import pytest
from tests.fixtures import *
from utils.string_utils import StringUtils
from utils.file_utils import project_path

utils = StringUtils()



@pytest.mark.usefixtures('media_mate_basico', 'bachiller_comunicacion', 'tecnologia')
@pytest.fixture
def docente_test5(maestro_primaria, maestro_grado, tecnologia):
    return Docente('valentina', 'ruiz', fecha_nacimiento='04/11/1996', sexo='masculino', tipo_dni='DNI', nro_dni='34303777',
                   cuil='20343037776', provincia='CABA', localidad='CABA', calle='Miller 2552', cod_postal='1431',
                   mail_temportal=str(utils.generate_word())+'@cys.com.ar', contrasenia_temporal='Test12345678',
                   imagenes_dni=[str(project_path.joinpath("cdocente_data", "img", "Manzana.jpg"))],
                   inscripciones=[maestro_grado], titulos=[maestro_primaria], cursos=[tecnologia],
                   celular='1557675211')
@pytest.fixture
def admin():
    return Usuario('Leandro', 'Ferrigno', 'leandro.ferrigno@bue.edu.ar', 'Ampersand.14 rules', Perfil.ADMINISTRADOR)