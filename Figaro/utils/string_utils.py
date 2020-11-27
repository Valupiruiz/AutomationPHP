from typing import List
from utils.exceptions import FormatoDeFechaInvalida


class StringUtils:
    @staticmethod
    def descomponer_fecha_en_atomos(fecha: str) -> List[str]:
        """
        Dada una fecha en formato DD/MM/AAAA, la descompongo en una tupla de año, mes y dia
        Args:
            fecha: contiene la fecha en formato DD/MM/AAAA

        Returns:
            Tuple[str, str, str]

        """
        lista_componentes: List[str] = fecha.split("/")
        if len(lista_componentes) is not 3:
            raise FormatoDeFechaInvalida
        return lista_componentes
