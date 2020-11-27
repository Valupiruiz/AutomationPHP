import pytest
from src.domain.publicacion import Publicacion, TipoPublicacion, CabeceraPublicacion
from datetime import datetime
import random


_DIAS_PREMIUM = 30
_ZONAS = ["Centro", "Cuyo", "Noreste", "Noroeste", "Patagonia"]


@pytest.fixture
def dias_premium():
    return _DIAS_PREMIUM


@pytest.fixture
def cabecera_publicacion_gratuita():
    now = str(datetime.now().strftime('%Y%M%d %H%M%S'))
    titulo = f"Título publicación gratuita {now}"
    sintesis = f"Síntesis publicación gratuita {now}"
    return CabeceraPublicacion(titulo, sintesis)


@pytest.fixture
def cabecera_publicacion_premium():
    now = str(datetime.now().strftime('%Y%M%d %H%M%S'))
    titulo = f"Título publicación premiun {now}"
    sintesis = f"Síntesis publicación premiun {now}"
    descripcion = "Soy premium y puedo poner una descripción 😎"
    return CabeceraPublicacion(titulo, sintesis, descripcion)


@pytest.fixture
def cabecera_publicacion_editada():
    now = str(datetime.now().strftime('%Y%m%d %H%M%S'))
    titulo = f"Editado por automatizacion {now}"
    sintesis = f"Editada por automatizacion {now}"
    return CabeceraPublicacion(titulo, sintesis)


@pytest.fixture
def publicacion_gratuita(cabecera_publicacion_gratuita, interes_todos):
    return Publicacion(TipoPublicacion.GRATUITA, 15, cabecera_publicacion_gratuita, random.choice(interes_todos),
                       random.choice(_ZONAS))


@pytest.fixture
def publicacion_premiun(cabecera_publicacion_premium, dias_premium, interes_todos):
    return Publicacion(TipoPublicacion.PREMIUM, dias_premium, cabecera_publicacion_premium,
                       random.choice(interes_todos), random.choice(_ZONAS))


@pytest.fixture
def publicacion_editada(cabecera_publicacion_editada, interes_todos):
    return Publicacion(TipoPublicacion.GRATUITA, 15, cabecera_publicacion_editada,
                       random.choice(interes_todos), random.choice(_ZONAS))
