from src.dominio.operable import Moneda
from src.utils.db_utils import QueryResultNotFoundException


class MonedasFactory:

    def __init__(self, db):
        self._db = db
        self._monedas = [Moneda('ARS', 'Peso Argentino'), Moneda('PEN', 'Sol Peruano'),
                         Moneda('USD', 'Dólar Estadounidense')]

    def build(self):
        for moneda in self._monedas:
            try:
                id_ = self._db.get_id_moneda(moneda)
            except QueryResultNotFoundException:
                id_ = self._db.crear_moneda(moneda)
            moneda.id = id_
            self._db.set_tolerancia_moneda(moneda.codigo, 50)
        return self._monedas
