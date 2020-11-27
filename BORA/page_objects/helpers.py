import datetime
import lorem
import re



def add_business_days(date, add_days):
    while add_days > 0:
        date += datetime.timedelta(days=1)
        weekday = date.weekday()
        if weekday >= 5:  # sábado = 5, domingo = 6.
            continue
        add_days -= 1
    return date


def generate_locator(locator, index):
    aux = str(locator[1]).format(index=index)
    return locator[0], aux


def generate_paragraph():
    return lorem.paragraph()


def generate_sentence():
    return lorem.sentence()


def generate_index(index):
    if index < 10:
        return str(0)+str(index)
    return str(index)


def extraer_numero_objeto_gasto(text):
    """Saco el texto y el último guión para que quede solo el número (x-x-x-x)"""
    text = "".join(re.findall(r'[\d-]', text))[0:-1]
    return text
