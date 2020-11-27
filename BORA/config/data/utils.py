import datetime
import lorem
import random
"""
Funciones genericas para abstraerse del manejo de fechas
"""


class Utils:
    def __init__(self, fecha=datetime.datetime.now(), dia=None, mes=None, anio=None):
        """
        Constructor para la clase. Por defecto se carga la fecha de hoy, sino, se le pasan parametros
        :param fecha: fecha de hoy
        :param dia: dia
        :param mes: mes
        :param anio: anio
        """
        self._fecha = fecha
        self._dia = dia
        self._mes = mes
        self._anio = anio

    def fecha_de_hoy_barras(self):
        """
        Devuelve la fecha de hoy formateada como DD/MM/AAAA
        :return: string
        """
        return self._fecha.strftime('%d/%m/%Y')

    def fecha_de_hoy(self):
        """
        Devuelve la fecha de hoy formateada como DDMMAAAA
        :return: string
        """
        return self._fecha.strftime('%d%m%Y')

    def fecha_de_hoy_hora(self):
        """
        Devuelve la fecha de hoy formateada como DDMMAAAAHHMM
        :return: string
        """
        return self._fecha.strftime('%d%m%Y%H%M')

    def fecha_de_hoy_guion(self):
        """
            Devuelve la fecha de hoy formateada como y-m-d
            :return: string
        """
        return self._fecha.strftime('%Y-%m-%d')

    def fecha_hoy_guion_invertida(self):
        """
            Devuelve la fecha de hoy formateada como d-m-y
            :return: string
        """
        return self._fecha.strftime('%d-%m-%Y')


    def fecha_de_ayer(self):
        """
        Devuelve la fecha de ayer formateada como DDMMAAAA
        :return: string
        """
        return (self._fecha - datetime.timedelta(1)).strftime('%d%m%Y')

    def fecha_de_ayer_barras(self):
        """
        Devuelve la fecha de ayer formateada como DD/MM/AAAA
        :return: string
        """
        return (self._fecha - datetime.timedelta(1)).strftime('%d/%m/%Y')

    def format_fecha_barra(self):
        """
        Es necesario pasarle dia, mes y anio al constructor. Formatea la fecha enviada como DD/MM/AAAA
        :return: string
        """
        return str(self._dia) + "/" + str(self._mes) + "/" + str(self._anio)

    def format_fecha(self):
        """
        Es necesario pasarle dia, mes y anio al constructor. Formatea la fecha enviada como DDMMAAAA
        :return: string
        """
        return str(self._dia) + str(self._mes) + str(self._anio)

    def fecha_guion_invertida(self):
        """
            Devuelve la fecha de hoy formateada como d-m-y
            :return: string
              """
        return str(self._dia) + "-" + str(self._mes) + "-" + str(self._anio)

    def fecha_dentro_de(self, dias):
        """
        Formatea la fecha de hoy mas la suma o resta de los dias que se le indique al parametro dias, con forma DDMMAAAA
        :param dias: la cantidad de dias a sumar o restar
        :return: string
        """
        return (self._fecha + datetime.timedelta(dias)).strftime('%d%m%Y')

    def fecha_dentro_de_barra(self, dias):
        """
        Formatea la fecha de hoy mas la suma o resta de los dias, con forma DD/MM/AAAA
        :param dias: la cantidad de dias a sumar o restar
        :return: string
        """
        return (self._fecha + datetime.timedelta(dias)).strftime('%d/%m/%Y')

    def add_business_days(self, date, add_days):

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

    @staticmethod
    def generate_paragraph():
        return lorem.paragraph()

    @staticmethod
    def generate_word():
        c = 'bcdfghjklmnpqrstvwxyzaeiou'
        palabra = ''
        for i in range(10):
            palabra = palabra + random.choice(c)
        return palabra

    def generate_sentence(self):
        return lorem.sentence()

    @property
    def generate_index(index):
        if index < 10:
            return str(0)+str(index)
        return str(index)


