import pytest
from src.domain.interes import Interes


@pytest.fixture
def interes_semillas():
    return Interes("Semillas", ["Trigo / Avena", "Maíz", "Forrajeras", "Soja", "Sorgo / Girasol", "Otras Semillas",
                                "Silobolsas"])


@pytest.fixture
def interes_agroquimicos():
    return Interes("Agroquímicos", ["Herbicidas", "Insecticidas y Funguicidas", "Fertilizantes", "Inoculantes",
                                    "Coadyuvantes", "Otros"])


@pytest.fixture
def interes_maquinaria_vehiculos():
    return Interes("Vehiculos / Maquinarias", ["Tractores", "Maquinas", "Camionetas / Autos", "Equipos",
                                               "Cosechadoras", "Sembradoras", "Pulverizadoras", "Herramientas"])


@pytest.fixture
def interes_instituciones():
    return Interes("Instituciones", ["Angus", "Braford", "Brangus", "Hereford", "AACREA", "Soc. Rural Arg",
                                     "IPCVA", "Aapresid"])


@pytest.fixture
def interes_remates():
    return Interes("Remates", ["Lecheria", "Cria / Inver", "Gordo / Consumo", "Herramientas", "Ovinos / Otros",
                               "Reproductores", "Equinos"])


@pytest.fixture
def interes_sanidad_alimentacion():
    return Interes("Sanidad / Alimentacion", ["Vacunas / Biologicos", "Antiparasitarios / Antibioticos",
                                              "Balanceados / Nucleos", "Minerales / Otros", "Subproductos / Forrajes",
                                              "Equipo Ganadero", "Instal. Ganaderas"])


@pytest.fixture
def interes_organismos_publicos():
    return Interes("Organismos Publicos", ["Sec. de Agric. / Gan.", "SENASA", "INTA", "Renatre",
                                           "Min. Prod. Pcia. Bs. As.", "Min. Prod. Cordoba", "Min. Prod. Salta",
                                           "Min. Prod. Corrientes"])


@pytest.fixture
def interes_capacitacion():
    return Interes("Capacitación", ["Congresos / Seminarios", "Giras / Dias de Campo", "Exposiciones", "Jornadas",
                                    "Cursos", "Carreras / Maestrias", "Charlas Virtuales"])


@pytest.fixture
def interes_servicios():
    return Interes("Servicios", ["Agricolas", "Ganaderos", "Financiación", "Consultoras / Profesionales",
                                 "Compra / Venta de Prop.", "Logistica y Fletes"])


@pytest.fixture
def interes_universidades():
    return Interes("Universidades", ["Fac. Agron. UBA", "Fac. Cs. Agrs. UCA", "Univ. Nac. N. Este", "Univ. Nac. Centro",
                                     "Univ. Nac. Cordoba", "Univ. Catolica Salta", "Univ. Lomas de Zamora",
                                     "Univ. Salvador"])


@pytest.fixture
def interes_busquedas_laborales():
    return Interes("Busquedas Laborales", ["Prof. Agropecuarios", "Prof. Administrativos", "Personal de campo",
                                           "Estudiantes y otros", "Pasantías", "Oficios", "Busquedas del Exterior"])


@pytest.fixture
def interes_tiempo_libre():
    return Interes("Tiempo libre", ["Pasajes", "Alojamiento", "Restaurantes", "Indumentaria",
                                    "Computación y electrodomésticos", "Espectaculos", "Otros"])


@pytest.fixture
def interes_empresas():
    return Interes("Empresas", ["Banco Galicia", "Biogenesis", "Farmquip", "Toyota", "John Deere", "Nidera",
                                "Basf", "Las Lilas"])


@pytest.fixture
def interes_todos(interes_semillas, interes_agroquimicos, interes_maquinaria_vehiculos, interes_instituciones,
                  interes_remates, interes_sanidad_alimentacion, interes_organismos_publicos,
                  interes_capacitacion, interes_servicios, interes_universidades, interes_busquedas_laborales,
                  interes_tiempo_libre, interes_empresas):
    return [
        interes_semillas, interes_agroquimicos, interes_maquinaria_vehiculos, interes_instituciones,
        interes_remates, interes_sanidad_alimentacion, interes_organismos_publicos, interes_capacitacion,
        interes_servicios, interes_universidades, interes_busquedas_laborales, interes_tiempo_libre, interes_empresas
    ]
