from random import choice

from src.actions.base.base_action import BaseAction
from src.config import MensajesError


# region Sucursal

# Debido a que la accion guardar sucursal se realiza en otros contextos tambien, se desacopla la accion
# completar de el guardado
class CompletarDatosNuevaSucursalAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._sucursal = None

    def verify_state(self):
        return self

    def do(self, sucursal):
        self.page.configuracion()
        self.page.configurar_sucursales()
        self.page.nueva_sucursal()
        self.page.agregar_sucursal(sucursal)
        self._sucursal = sucursal
        return self

    def success(self):
        _validar_sucursal(self, self._sucursal)

    def failure(self):
        pass


class GuardarSucursalAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)

    def verify_state(self, sucursal):
        _validar_sucursal(self, sucursal)
        return self

    def do(self):
        self.page.guardar_sucursal()
        return self

    def success(self, nueva_sucursal=False):
        if nueva_sucursal:
            mensaje = MensajesError.AgregarSucursal
        else:
            mensaje = MensajesError.EditarSucursal
        self._assert.that(mensaje).equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.redireccionar_usuario()

    def failure(self, failure_type):
        mensajes_por_razon = {
            'Nombre': 'El nombre de la oficina debe ser único',
            'Codigo': 'El código de la oficina debe ser único'
        }
        self._assert.that(mensajes_por_razon[failure_type]).equals(self.page.get_toast())
        self.page.dismiss_toast()


class ModificarDatosSucursalAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._nuevo_nombre = None

    def verify_state(self, sucursal):
        _validar_sucursal(self, sucursal)
        return self

    def do(self, nuevo_nombre):
        self._nuevo_nombre = nuevo_nombre
        # todo: modificar mas datos de la sucursal
        self.page.modificar_nombre_sucursal(nuevo_nombre)
        return self

    def success(self):
        self._assert.that(self._nuevo_nombre).equals(self.page.nombre_sucursal())

    def failure(self):
        pass


class ModificarEstadoSucursalAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._sucursal = None

    def verify_state(self, sucursal):
        self.page.configuracion()
        self.page.configurar_sucursales()
        _buscar_sucursal(self, sucursal)
        self.page.validar_estado_sucursal(sucursal.nombre_compuesto(), sucursal.activa)
        return self

    def do(self, sucursal):
        self._sucursal = sucursal
        self.page.cambiar_estado_sucursal(sucursal)
        return self

    def success(self):
        self._assert.that(MensajesError.EditarSucursal).that(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.validar_estado_sucursal(self._sucursal.nombre_compuesto(), self._sucursal.activa)
        self.page.validar_cajas_activas_sucursal(self._sucursal)

    def failure(self, failure_type, sucursal, caja):
        mensajes = {
            "con saldo": f"No puede deshabilitar la caja {caja.codigo} con cierres mayores a cero",
            "abierta": f'No se puede deshabilitar la caja {caja.codigo} por que no se encuentra cerrada totalmente'
        }
        self._assert.that(mensajes[failure_type]).equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.cerrar_modal()
        self.page.validar_estado_sucursal(self._sucursal.nombre_compuesto(), sucursal)
        self.page.validar_cajas_activas_sucursal(sucursal)


class IrEdicionSucursalAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._sucursal = None

    def verify_state(self):
        return self

    def do(self, sucursal):
        self._sucursal = sucursal
        self.page.configuracion()
        self.page.configurar_sucursales()
        _buscar_sucursal(self, sucursal)
        self.page.ir_edicion_sucursal(sucursal.nombre_compuesto())
        return self

    def success(self):
        _validar_sucursal(self, self._sucursal)

    def failure(self):
        pass


# endregion

# Caja Actions

class CrearCajaAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._caja = None
        self._sucursal = None

    def verify_state(self, sucursal):
        self._assert.that(sucursal.nombre).equals(self.page.nombre_sucursal())
        self._sucursal = sucursal
        return self

    def do(self, caja):
        self._caja = caja
        self.page.crear_nueva_caja(caja.codigo)
        return self

    def success(self):
        self._assert.that(MensajesError.AgregarCaja).equals(self.page.get_toast())
        self.page.dismiss_toast()
        self._assert.that(self._caja.activa).equals(self.page.estado_caja(self._caja.codigo))

    def failure(self, failure_type):
        mensaje = {
            "Sucursal desactivada": f"No se permiten agregar cajas, la oficina {self._sucursal.codigo} "
                                    f"está desactivada",
            "Codigo repetido": "El código de la caja debe ser único"
        }[failure_type]

        self._assert.that(mensaje).equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.cerrar_modal()


class EditarCajaAction(BaseAction):

    def verify_state(self, caja):  # verifica el estado de la caja previo a la edicion
        self.page.abrir_edicion_caja(caja)
        estado_giros = self.page.estado_giros()
        estado_monedas_giros = self.page.estado_monedas_giros()
        esperado = {
            "Caja": {
                "Estado": caja.activa,
                "Envia giros": caja.envia_giros,
                "Recibe giros": caja.recibe_giros
            },
            "Monedas": {
                "Total de monedas": {
                    "Envia": len(caja.monedas),
                    "Recibe": len(caja.monedas)
                },
                "Monedas que opera": {
                    "Envia": {moneda.codigo: estado for moneda, estado in caja.monedas_envio_giros.items()},
                    "Recibe": {moneda.codigo: estado for moneda, estado in caja.monedas_recibo_giros.items()}
                }
            }
        }
        obtenido = {
            "Caja": {
                "Estado": self.page.estado_toggle_caja(),
                "Envia giros": estado_giros["Envia"],
                "Recibe giros": estado_giros["Recibe"]
            },
            "Monedas": {
                "Total de monedas": {
                    "Envia": len(estado_monedas_giros["Envia"]),
                    "Recibe": len(estado_monedas_giros["Recibe"])
                },
                "Monedas que opera": {
                    "Envia": estado_monedas_giros["Envia"],
                    "Recibe": estado_monedas_giros["Recibe"]
                }
            }
        }
        self._assert.that(esperado).equals(obtenido)
        return self

    def do(self, caja):
        estado_giros = self.page.estado_giros()

        if estado_giros["Envia"] != caja.envia_giros:
            self.page.modificar_estado_giro("Envia", caja.envia_giros)
        if estado_giros["Recibe"] != caja.recibe_giros:
            self.page.modificar_estado_giro("Recibe", caja.recibe_giros)

        estado_monedas_giros = self.page.estado_monedas_giros()

        for codigo, estado in estado_monedas_giros["Envia"].items():
            moneda = next(moneda for moneda in caja.monedas if moneda.codigo == codigo)
            estado_esperado = caja.monedas_envio_giros[moneda]
            if estado_esperado != estado:
                self.page.modificar_moneda_giro("Envia", codigo, estado_esperado)

        for codigo, estado in estado_monedas_giros["Recibe"].items():
            moneda = next(moneda for moneda in caja.monedas if moneda.codigo == codigo)
            estado_esperado = caja.monedas_recibo_giros[moneda]
            if estado_esperado != estado:
                self.page.modificar_moneda_giro("Recibe", codigo, estado_esperado)

        if caja.activa != self.page.estado_toggle_caja():
            self.page.modificar_estado_caja(caja.activa)

        self.page.guardar_caja()
        return self

    def success(self):
        self._assert.that(MensajesError.EditarCaja).equals(self.page.get_toast())
        self.page.dismiss_toast()

    def failure(self, caja, failure_type):
        mensajes = {
            "abierta": f"No se puede deshabilitar la caja {caja.codigo} por que no se encuentra cerrada totalmente",
            "con saldo": f'No puede deshabilitar la caja {caja.codigo} con cierres mayores a cero',
        }

        mensaje = mensajes[failure_type]
        self._assert.that(mensaje).equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.cerrar_modal()


# endregion

# todo: ver donde meter este tipo de metodos que se usan en mas de un action
def _buscar_sucursal(self, sucursal):
    self.page.clear_filters()
    if choice([True, False]):
        self.page.buscar_sucursal_por_codigo(sucursal.codigo)
    else:
        self.page.buscar_sucursal_por_nombre(sucursal.nombre)


def _validar_sucursal(self, sucursal):
    self._assert.that(sucursal.nombre).equals(self.page.nombre_sucursal())
    self._assert.that(sucursal.codigo).equals(self.page.codigo_sucursal())
    self._assert.that(sucursal.provincia.nombre).equals(self.page.provincia_sucursal())
    self._assert.that(sucursal.ciudad).equals(self.page.ciudad_sucursal())
    self._assert.that(sucursal.direccion).equals(self.page.direccion_sucursal())
    self._assert.that(sucursal.codigo_postal).equals(self.page.codigo_postal_sucursal())
    self._assert.that(sucursal.codigo_area).equals(self.page.codigo_area_sucursal())
    self._assert.that(sucursal.telefono).equals(self.page.telefono_sucursal())
    self._assert.that(sucursal.mail).equals(self.page.email_sucursal())
    _validar_cajas_sucursal(self, sucursal)


def _validar_cajas_sucursal(self, sucursal):
    estados = {
        True: "Activo",
        False: "Inactivo"
    }
    cajas_sucursal = {caja.codigo: estados[caja.activa] for caja in sucursal.cajas}
    self._assert.that(cajas_sucursal).equals(self.page.cajas_sucursal())
