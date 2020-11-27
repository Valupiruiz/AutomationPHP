from decimal import Decimal
from dominio.evaluacion import Ponderacion
from dominio.redondeo import Redondeo
from dominio.calificacion import Calificacion
from typing import List


def calcular_promedio_exacto(calificaciones: List[Calificacion], periodo: str):
    # Solo se toman en consideracion las evaluaciones que no esten excluidas, donde el alumno este como presente
    # Se hace calculo de las ponderaciones recordar por ej: Si una evaluacion tiene ponderacion Manual de 70
    # y calificaciones 10 2 10 entonces el prom sera 10*0,70 + 0,20 *2 + 10 * 0,10
    if not calificaciones:
        raise Exception("MANDAME CALIFICACIONES........SINO QUE PROMEDIO CALCULO????")
    calificaciones_de_periodo = list(filter(lambda c: c.evaluacion.periodo == periodo, calificaciones))
    calificaciones_no_excluidas = get_calificaciones_no_excluidas(calificaciones_de_periodo)
    definitivo = get_calificaciones_no_ausente(calificaciones_no_excluidas)
    calif_con_ponderacion = list(filter(lambda x: x.evaluacion.ponderacion == Ponderacion.MANUAL, definitivo))
    calif_sin_ponderacion = list(filter(lambda x: x.evaluacion.ponderacion == Ponderacion.AUTOMATICA, definitivo))
    if len(calif_con_ponderacion) > 0:
        ponderaciones = Decimal(sum([x.evaluacion.porcentaje / 100 for x in calif_con_ponderacion])).quantize(
            Decimal('0.10'))
        prom_con_pond = sum([(c.nota * c.evaluacion.porcentaje) / 100 for c in calif_con_ponderacion])
        if ponderaciones == 1:
            return Decimal(prom_con_pond).quantize(Decimal('0.10'))
        else:
            ponderacion_restante = (1 - ponderaciones) / len(calif_sin_ponderacion)
            prom_sin_pond = sum([(c.nota * ponderacion_restante) for c in calif_sin_ponderacion])
            prom_exacto = prom_con_pond + prom_sin_pond
            return Decimal(prom_exacto).quantize(Decimal('0.10'))
    else:
        ponderacion_igual = Decimal(1 / len(calif_sin_ponderacion))
        prom_exacto = sum([(c.nota * ponderacion_igual) for c in calif_sin_ponderacion])
        print(prom_exacto)
        return Decimal(prom_exacto).quantize(Decimal('0.10'))


def calcular_ev(promedio_exacto: Decimal, tipo_promedio: Redondeo):
    return tipo_promedio.redondear(promedio_exacto)


def get_calificaciones_no_excluidas(calificaciones: List[Calificacion]):
    return list(filter(lambda x: not x.evaluacion.excluida, calificaciones))


def get_calificaciones_no_ausente(calificaciones: List[Calificacion]):
    return list(filter(lambda x: not x.ausente, calificaciones))
