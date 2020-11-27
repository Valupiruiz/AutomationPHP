from datetime import datetime, timedelta

from math import floor


def format_number(num, format_):
    cant_decimales = 2
    if not num % 1:
        return int(num)
    num = floor(num * 10 ** cant_decimales) / 10 ** cant_decimales
    return format(num, format_)


def calcular_porcentaje(m, p):
    return (m * p) / 100.0


def today():
    return '{d.day:02}/{d.month:02}/{d.year}'.format(d=datetime.utcnow())

def parse_iso_date(date):
    # el formato que acepta es YYYY-MM-DD[*HH[:MM[:SS[.mmm[mmm]]]][+HH:MM[:SS[.ffffff]]]]
    # es decir, '2017-01-01T12:30:59.000000', Si utilizo una fecha del estilo 2020-07-07T18:24:50.58548
    # pincha porque es una bija y no hay 6 digitos en los milisegundos, es mas facil ignorar los segundos
    # y el timezone a intentar padearlo
    d, _ = date.split('.')
    return '{d.day:02}/{d.month:02}/{d.year}'.format(d=datetime.fromisoformat(d))

def seconds_before_now(seconds):
    return datetime.utcnow() - timedelta(seconds=seconds)
