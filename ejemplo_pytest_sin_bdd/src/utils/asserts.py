class Assert:

    def __init__(self):
        self._that = None

    def that(self, o):
        self._that = o
        return self

    def equals(self, other):
        assert self._that == other, f"Esperaba que fueran iguales\n" \
                                    f"Esperado: {self._that}\n" \
                                    f"Obtenido: {other}\n"

    def contains(self, other):
        assert self._that in other, f"Esperaba que contuviera\n" \
                                    f"Esperado: {self._that}\n" \
                                    f"Obtenido: {other}\n"

    def greater_than(self, other):
        assert self._that > other, f"Esperaba que fuera mayor estricto\n" \
                                    f"Esperado: {self._that}\n" \
                                    f"Obtenido: {other}\n"

    def ge_than(self, other):
        assert self._that >= other, f"Esperaba que fuera mayor o igual" \
                                    f"Esperado: {self._that}\n" \
                                    f"Obtenido: {other}\n"
