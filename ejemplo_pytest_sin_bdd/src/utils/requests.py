import json

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Base:
    _HEADERS = {'Content-Type': 'application/json',
                'Accept': '*/*'}

    def _make_request(self, method, endpoint, headers, params=None, body=None):
        body = json.dumps(body)
        print(f"\n-----------------Request------------------"
              f"\nMethod: {method}"
              f"\nendpoint: {endpoint}"
              f"\nheaders: {headers}"
              f"\nbody: {body}")
        response = requests.request(method, endpoint, headers=headers, data=body, params=params, verify=False)
        print(f"\n---------------Response-------------------"
              f"\nstatus: {response.status_code}"
              f"\ncontent: {response.content}"
              f"\ntext: {response.text}")
        return response

    def put(self, endpoint, body, headers=_HEADERS):
        return self._make_request("PUT", endpoint, headers, body=body)

    def post(self, endpoint, body, headers=_HEADERS):
        return self._make_request("POST", endpoint, headers, body=body)

    def get(self, endpoint, qs: dict, headers=_HEADERS):
        return self._make_request("GET", endpoint, headers, params=qs)


class Request(Base):

    def __init__(self, target):
        super().__init__()
        self._base_url = target
        self._endpoints = ENDPOINTS(target)
        self._token = None

    def login(self, usuario):
        body = {
            "mail": usuario.mail,
            "IdNumber": str(usuario.dni),
            "Password": usuario.password
        }
        response = self.post(self._endpoints.login(), body)
        self.save_token(response.json()['tokenDeAcceso'])
        return response

    def save_token(self, token):
        self._token = token

    def crear_sucursal(self, sucursal):
        body = {
            "name": sucursal.nombre,
            "codigo": sucursal.codigo,
            "mail": sucursal.mail,
            "phone": sucursal.telefono,
            "areaCode": sucursal.codigo_area,
            "companyId": 1,
            "address": {
                "provinceId": sucursal.provincia.id,
                "city": sucursal.ciudad,
                "streetLine": sucursal.direccion,
                "zipCode": sucursal.codigo_postal
            }
        }
        return self.post(self._endpoints.crear_sucursal(), body, headers=self.auth_header())

    def crear_caja(self, id_sucursal, caja):
        body = {
            "oficinaId": id_sucursal,
            "codigo": caja.codigo,
            "canEnviarGiros": True,
            "canRecibirGiros": True,
            "monedasGirosEntrantes": [moneda.id for moneda in caja.monedas_recibo_giros],
            "monedasGirosSalientes": [moneda.id for moneda in caja.monedas_envio_giros]
        }
        return self.post(self._endpoints.crear_caja(), body, headers=self.auth_header())

    def aperturar_caja(self, caja, apertura, cajero):
        return self.post(
            self._endpoints.aperturar_caja(caja.id),
            _get_operacion_body(apertura, cajero.password),
            self.auth_header()
        )

    def aperturar_boveda(self, boveda, apertura, cajero):
        return self.post(
            self._endpoints.aperturar_boveda(boveda.id),
            _get_operacion_body(apertura, cajero.password),
            self.auth_header()
        )

    def cerrar_totalmente_caja(self, caja, cierre, cajero):
        return self.post(
            self._endpoints.cerrar_caja(caja.id),
            _get_operacion_body(cierre, cajero.password),
            self.auth_header()
        )

    def cerrar_parcialmente_caja(self, caja, cierre, cajero):
        return self.post(
            self._endpoints.cerrar_caja_parcialmente(caja.id),
            _get_operacion_body(cierre, cajero.password),
            self.auth_header()
        )

    def cerrar_boveda(self, boveda, cierre, operador):
        return self.post(
            self._endpoints.cerrar_boveda(boveda.id),
            _get_operacion_body(cierre, operador.password),
            self.auth_header()
        )

    def gestion_caja(self, caja):
        qs = {
            "Code": caja.codigo,
            "Page": 1,
            "PageSize": 1,
        }
        return self.get(
            self._endpoints.gestion_caja(),
            qs,
            self.auth_header()
        )

    def desbloquear_caja(self, caja, resolucion):
        return self.put(
            self._endpoints.desbloquear_caja(caja.id),
            {"resolucion": resolucion},
            self.auth_header()
        )

    def generar_transferencia(self, transferencia, cajero):
        body = {
            "origenId": transferencia.origen.id,
            "destinoId": transferencia.destino.id
        }

        return self.post(
            self._endpoints.generar_transferencia(),
            {**body, **_get_operacion_body(transferencia, cajero.password)},
            self.auth_header()
        )

    # fixme, deberia incorporar el id a la transferencia
    def confirmar_transferencia(self, id_, transferencia, cajero):
        return self.post(
            self._endpoints.confirmar_transferencia(id_),
            _get_operacion_body(transferencia, cajero.password),
            self.auth_header()
        )

    def auth_header(self):
        if not self._token:
            raise Exception(f"No hay una sesion activa, token={self._token}")
        aux = self._HEADERS.copy()
        aux['Authorization'] = f'Bearer {self._token}'
        return aux

    def recepcionar_transferencia(self, id_):
        return self.post(
            self._endpoints.recepcionar_transferencia(id_),
            {},
            self.auth_header()
        )


class ENDPOINTS:

    def __init__(self, base_url):
        self.base_url = base_url

    def login(self):
        return f"{self.base_url}/Auth/authenticate"

    def crear_sucursal(self):
        return f"{self.base_url}/branches"

    def crear_caja(self):
        return f"{self.base_url}/checkouts"

    # Deberia ver como escala esto, caja y boveda tienen muchas similitudes (ambos son tipos de operables)
    # que podrian resumirse en un diccionario por tipo de operable pero quizas meter logica de negocio
    # en esta capa no sea de las mejores ideas a largo plazo, por el momento es mas facil hacerlo especifico
    # y en el action definir que metodo llamar

    def aperturar_caja(self, id_):
        return f"{self.base_url}/Checkouts/{id_}/aperturas"

    def cerrar_caja(self, id_):
        return f"{self.base_url}/Checkouts/{id_}/cierrestotales"

    def cerrar_caja_parcialmente(self, id_):
        return f"{self.base_url}/Checkouts/{id_}/cierresparciales"

    def aperturar_boveda(self, id_):
        return f"{self.base_url}/bovedas/{id_}/aperturas"

    def cerrar_boveda(self, id_):
        return f"{self.base_url}/bovedas/{id_}/cierrestotales"

    def gestion_caja(self):
        return f"{self.base_url}/Checkouts/gestiondecajas"

    def desbloquear_caja(self, id_):
        return f"{self.base_url}/Checkouts/{id_}/desbloquear"

    def generar_transferencia(self):
        return f"{self.base_url}/transferencias"

    def confirmar_transferencia(self, id_):
        return f"{self.base_url}/transferencias/{id_}/confirmar"

    def recepcionar_transferencia(self, id_):
        return f"{self.base_url}/transferencias/{id_}/recepcionar"


def _get_operacion_body(operacion, password):
    return {
        "montos": [{"monedaId": moneda.id, "monto": monto} for moneda, monto in operacion.montos.items()],
        "observaciones": str(operacion.observaciones),
        "password": password
    }
