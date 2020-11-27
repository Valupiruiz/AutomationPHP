import psycopg2
from filelock import FileLock

from src.config.config import LOCKS

lock = FileLock(LOCKS.DB)


# fixme


class ConexionBd:

    def __init__(self, hostname, username='adminargenper', password='argenperadmin', database='argenper'):
        self.conexion = psycopg2.connect(host=hostname, user=username,
                                         password=password, dbname=database)
        self.conexion.set_client_encoding('utf-8')
        self.cursor = self.conexion.cursor()
        self._result = None

    def select(self, query):
        with lock:
            self._result = self.cursor.execute(query)
            self._fetch_results()
            print(f"\nSe ejecuto la query correctamente:\n"
                  f"{query}\n"
                  f"Arrojo los resultados:\n"
                  f"{self._result}\n")

    def update(self, query, commit=True):
        with lock:
            self.cursor.execute(query)
            if commit:
                self.conexion.commit()
            if self.cursor.description:
                self._fetch_results()
            print(f"\nSe ejecuto la modificacion correctamente:\n"
                  f"{query}\n")

    def _fetch_results(self):
        columnas = [column[0] for column in self.cursor.description]
        self._result = [dict(zip(columnas, row)) for row in self.cursor.fetchall()]

    def fetch_first(self, column=None):
        if len(self._result) == 0:
            raise EmptyQueryResultException("La query no arrojo resultados")

        if column:
            return self._result[0][column]
        return self._result[0]

    def fetch_all(self):
        return self._result

    def __del__(self):
        if self.cursor:
            self.cursor.close()

        if self.conexion:
            self.conexion.close()


class Db(object):

    def __init__(self, hostname):
        self.conexion = ConexionBd(hostname)
        self.queries = Queries

    def asignar_operador(self, cajero, codigo_caja):
        id_cajero = self.get_usuario(cajero)['id']
        if self.get_cajero_caja(codigo_caja) == id_cajero:
            # no hago nada porque ya esta asignado
            return

        # limpio la caja asignada del cajero para no tener varias asignaciones
        self.conexion.update(self.queries.LIMPIAR_CAJERO.format(id=id_cajero))

        # asigno la nueva caja
        self.conexion.update(self.queries.ASIGNAR_CAJERO.format(id=id_cajero, codCaja=codigo_caja))

    def desasignar_cajero(self, cajero):
        self.conexion.update(self.queries.LIMPIAR_CAJERO.format(id=self.get_usuario(cajero)['id']))

    def modificar_estado_caja(self, codigo_caja, nuevo_estado):
        self.conexion.update(self.queries.MODIFICAR_ESTADO_CAJA.format(estado=nuevo_estado, codCaja=codigo_caja))

    def get_estado_caja(self, codigo_caja):
        self.conexion.select(self.queries.GET_ESTADO_CAJA.format(codCaja=codigo_caja))
        return self.conexion.fetch_first('estado_de_operable_id')

    def get_cajero_caja(self, codigo_caja):
        self.conexion.select(self.queries.GET_CAJERO_CAJA.format(codCaja=codigo_caja))
        try:
            return self.conexion.fetch_first('id')
        except EmptyQueryResultException:
            return None

    def numero_caja_por_subfijo(self, subfijo):
        self.conexion.select(self.queries.CAJA_POR_SUBFIJO.format(subfijo=subfijo))
        try:
            codigo = self.conexion.fetch_first('codigo')
            return int(codigo.replace(subfijo, ''))
        except EmptyQueryResultException:
            return -1

    def numero_sucursal_por_subfijo(self, subfijo):
        self.conexion.select(self.queries.SUCURSAL_POR_SUBFIJO.format(subfijo=subfijo))
        try:
            codigo = self.conexion.fetch_first('codigo')
            return int(codigo.replace(subfijo, ''))
        except EmptyQueryResultException:
            return -1

    def get_id_sucursal(self, codigo_sucursal):
        self.conexion.select(self.queries.GET_SUCURSAL.format(codigo_sucursal=codigo_sucursal))
        return self.conexion.fetch_first('id')

    def get_id_caja(self, codigo_caja):
        self.conexion.select(self.queries.CAJA.format(cod_caja=codigo_caja))
        return self.conexion.fetch_first('id')

    def get_id_moneda(self, moneda):
        self.conexion.select(self.queries.GET_ID_MONEDA.format(symbol=moneda.codigo))
        try:
            return self.conexion.fetch_first('id')
        except EmptyQueryResultException:
            raise QueryResultNotFoundException()

    def crear_moneda(self, moneda):
        self.conexion.update(self.queries.CREAR_MONEDA.format(estado=moneda.estado, symbol=moneda.codigo,
                                                              name=moneda.nombre))
        return self.conexion.fetch_first('id')

    def crear_usuario(self, usuario):
        if usuario.password == "12345678":
            password = "VJFpK+dk25VvnexkWgg/VIz6Dm4Ao6Get2H2tlSU/2oRjI1foC/bK308NPTsnqsLJRy0rDeWEO+nAJgY6P6/HA=="
            salt = "jPnFVYOlgl1SoUFniqRWCPjPgTGyDEK7Rm3OaV+3OhY="
        elif usuario.password == "Factory.07":
            password = "vZ/LaIY+FHRKv/237KV82GP7SGlnoI2C+oP46db5X5oPaXhrLz+/fz1LWSHV/shWfhAgww1PJaZiWRx3Nx9DYA=="
            salt = "XGTiiRdM0iizpE7yx4uTFsc5a8jRCi+spzynbAxBk2Q="
        else:
            raise Exception("No tengo esa contraseña")
        self.conexion.update(self.queries.CREAR_USUARIO.format(nombre=usuario.nombre, apellido=usuario.apellido,
                                                               mail=usuario.mail, password=password,
                                                               salt=salt, dni=usuario.dni, company=1))
        id_usuario = self.conexion.fetch_first('id')
        self.conexion.select(self.queries.GET_ID_ROL.format(nombre_rol=usuario.tipo['db']))
        self.conexion.update(self.queries.ASIGNAR_ROL_USUARIO.format(id_rol=self.conexion.fetch_first('id'),
                                                                     id_usuario=id_usuario))
        return id_usuario

    def get_usuario(self, usuario):
        self.conexion.select(self.queries.GET_USUARIO.format(mail=usuario.mail, dni=usuario.dni))
        try:
            return self.conexion.fetch_first()
        except EmptyQueryResultException:
            raise QueryResultNotFoundException("No se encontro el usuario")

    def get_transferencia(self, transferencia):
        self.conexion.select(self.queries.GET_TRANSFERENCIA.format(codigo_destino=transferencia.destino.codigo,
                                                                   codigo_origen=transferencia.origen.codigo))
        return self.conexion.fetch_first()

    def transferencia_por_numero(self, numero):
        self.conexion.select(self.queries.GET_TRANSFERENCIA_POR_NUMERO.format(numero=numero))
        return self.conexion.fetch_first()

    def set_tolerancia_moneda(self, codigo, tolerancia):
        self.conexion.update(self.queries.SET_TOLERANCIA_MONEDA.format(codigo=codigo, tolerancia=tolerancia))

    def get_provincia(self, nombre):
        self.conexion.select(self.queries.GET_PROVINCIA.format(nombre=nombre))
        return self.conexion.fetch_first()


# noinspection SqlNoDataSourceInspection
class Queries:
    ASIGNAR_CAJERO = "update \"operables\" " \
                     "set \"operador_id\" = (select \"id\" from \"usuarios\" where \"id\" = '{id}') " \
                     "where \"codigo\" = '{codCaja}'"
    LIMPIAR_CAJERO = "update \"operables\" " \
                     "set \"operador_id\" = NULL " \
                     "where \"operador_id\" = (select \"id\" from \"usuarios\" where \"id\" = '{id}')"
    MODIFICAR_ESTADO_CAJA = "update \"operables\" " \
                            "set \"estado_de_operable_id\" = '{estado}' " \
                            "where \"codigo\" = '{codCaja}'"
    GET_ESTADO_CAJA = "select \"estado_de_operable_id\" " \
                      "from \"operables\" " \
                      "where \"codigo\" = '{codCaja}'"
    GET_CAJERO_CAJA = "select \"id\" " \
                      "from \"usuarios\" " \
                      "where \"id\" = (select \"operador_id\" from \"operables\" where \"codigo\" = '{codCaja}')"
    GET_SUCURSAL = "select \"id\" " \
                   "from \"oficinas\" " \
                   "where \"codigo\" = '{codigo_sucursal}'"

    GET_USUARIO = "select \"id\" from \"usuarios\" " \
                  "where \"correo_electronico\" = '{mail}' " \
                  "and \"identificacion\" = '{dni}'"

    SUCURSAL_POR_SUBFIJO = "select \"codigo\" from \"oficinas\" " \
                           "where \"codigo\" LIKE '{subfijo}%' order by \"codigo\" desc"

    CAJA_POR_SUBFIJO = "select \"codigo\" from \"operables\" " \
                       "where \"codigo\" LIKE '{subfijo}%' order by \"codigo\" desc"

    CREAR_USUARIO = "INSERT INTO \"usuarios\" " \
                    "values (DEFAULT ,'true', '{nombre}', '{apellido}', '{mail}', NULL, " \
                    "'{password}', '{salt}', '{dni}', '{company}') " \
                    "RETURNING \"id\" "

    ASIGNAR_ROL_USUARIO = "INSERT INTO \"usuarios_roles\" values ('{id_usuario}', '{id_rol}')"

    GET_ID_ROL = "select \"id\" from \"roles\" where \"nombre\" = '{nombre_rol}'"

    GET_ID_MONEDA = "select \"id\" from \"monedas\" where \"codigo_iso\" = '{symbol}'"

    MONEDA_COMPANIA = "select \"compania_id\" from \"companias_monedas\" where \"moneda\" = '{id_moneda}'"

    CREAR_MONEDA = "INSERT INTO \"companias_monedas\" (\"companias_id\", \"moneda\", \"tolerancia\") " \
                   "values (1, '{symbol}', 0) " \
                   "RETURNING \"id\""

    CAJA = "select \"id\" from \"operables\" WHERE \"codigo\" = '{cod_caja}'"

    GET_TRANSFERENCIA = "select \"tipo_de_transaccion_id\", \"numero_transaccion\", \"fecha\" " \
                        "from \"transferencias\" " \
                        "where 	" \
                        "   \"destino_id\" = (select \"id\" from \"operables\" where \"codigo\" = '{codigo_destino}') " \
                        "and " \
                        "   \"origen_id\" = (select \"id\" from \"operables\" where \"codigo\" = '{codigo_origen}') " \
                        "order by \"fecha\""

    GET_TRANSFERENCIA_POR_NUMERO = "select * from \"transferencias\" where \"numero_transaccion\" = '{numero}'"

    SET_TOLERANCIA_MONEDA = "update \"companias_monedas\" " \
                            "set \"tolerancia\" = '{tolerancia}' " \
                            "where \"moneda\" = '{codigo}'"

    GET_PROVINCIA = "SELECT * FROM \"provincias\" where \"nombre\"='{nombre}'"


class EmptyQueryResultException(Exception):
    pass


class QueryResultNotFoundException(Exception):
    pass
