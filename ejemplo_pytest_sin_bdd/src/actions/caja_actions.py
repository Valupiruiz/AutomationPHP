from src.actions.operable_actions import CierreOperableAction
from src.factory.page.listado_paginas import Paginas

# A diferencia de boveda, al realizar un cierre se muestra la DDJJ
class CierreTotalCajaAction(CierreOperableAction):

    # todo: validar ddjj cuando deje de estar mockeada en sut

    def __init__(self, context):
        super().__init__(context)

    def success(self):
        self.page.ir_home_dj(False)
        return super().success()

    def failure(self, failure_type):
        if failure_type == 'Bloqueo':
            self.page.ir_home_dj(True)
        return super().failure(failure_type)


# No creo que sea realmente necesario, es solo para que quede mas intuitivo en el test
class CierreParcialCajaAction(CierreOperableAction):

    def __init__(self, context):
        super().__init__(context)

    def failure(self, failure_type):
        raise NotImplementedError("Los cierres parciales no pueden fallar")

    # al final si era necesario
    def fast_forward(self, operador, operable, cierre, redirect=True):
        self.api.login(operador)
        response = self.api.cerrar_parcialmente_caja(operable, cierre, operador)
        assert response.ok
        if redirect:
            self.page.create_with_name(Paginas.AperturaCaja, refresh=True)
