import pytest
from tests.fixtures import *


@pytest.fixture
def media_mate_basico():
    return Inscripcion([Listado.INGRESO, Listado.SUPLENCIAS], 'AREA DE EDUCACION MEDIA', 'PROFESOR DE EDUCACION MEDIA (1599)',
                       'MATEMATICA (6169)', 'NES - CICLO BASICO DE DISEÑO CURRICULAR')
@pytest.fixture
def maestro_grado():
    return Inscripcion([Listado.INGRESO, Listado.SUPLENCIAS], 'AREA DE LA EDUCACION PRIMARIA', 'MAESTRO DE GRADO (1020)',
                       'Sin Asignatura', 'Sin Especialidad', distrito=['10'])
