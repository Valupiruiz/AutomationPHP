from tests.fixtures import *
import pytest

#holy cross
@pytest.fixture
def hc_docente_vacuna():
    return Docente('vacuna@holycross.edu.ar', 'Verónica', 'Acuña')

@pytest.fixture
def hc_alumno_armagnif():
    return Alumno('', 'FEDERICO', 'ARMAGNI')

#end holy cross

#vanguardia
@pytest.fixture
def vgdia_docente_mrgarnero():
    return Docente('mrgarnero', 'Maria Rosa', 'Garnero')

@pytest.fixture
def vgdia_alumno_abdalaf():
    return Alumno('','FIAMMA NAIR','ABDALA')
#end vanguardia

#Adolfo Kolping
@pytest.fixture
def ak_docente_medina():
    return Docente('mmedina13', 'María Sol', 'Medina')

@pytest.fixture
def ak_alumno_lazzarom():
    return Alumno('', 'Martin', 'Lazzaro')


