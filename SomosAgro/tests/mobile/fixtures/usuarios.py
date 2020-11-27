from src.domain.usuario import Usuario
import pytest


@pytest.fixture
def usuario_prueba_fbapp():
    return Usuario("TomiTestAutom", "TomiAgro", "tmoreira@cys.com.ar", "12345678")
