from random import randint


class Sucursal(object):

    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.codigo_area = str(randint(0, 999))
        self.telefono = str(randint(10000000, 99999999))
        self.provincia = Provincia("Ciudad Autónoma de Buenos Aires")
        self.ciudad = "Buenos Aires"
        self.direccion = "Direccion de prueba"
        self.mail = "jrodriguez@cys.com.ar"
        self.codigo_postal = str(randint(1000, 9999))
        self._cajas = []
        self.activa = True

    @property
    def cajas(self):
        return self._cajas

    def agregar_cajas(self, *cajas):
        for caja in cajas:
            self._cajas.append(caja)

    def _buscar(self, iterator, func):
        return iterator(caja for caja in self._cajas if func(caja))

    def cajas_activas(self):
        return self._buscar(list, lambda caja: caja.activa)

    def cajas_inactivas(self):
        return self._buscar(list, lambda caja: not caja.activa)

    def buscar_caja(self, identificador):
        # identificador puede ser un nombre o un codigo
        return self._buscar(next, lambda caja: identificador in [caja.nombre, caja.codigo])

    def desactivar(self):
        self.activa = False
        [caja.desactivar() for caja in self.cajas]

    def nombre_compuesto(self):
        return f"{self.codigo} - {self.nombre}"


class Provincia:

    def __init__(self, nombre):
        self.nombre = nombre
        self._id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id_):
        self._id = id_

