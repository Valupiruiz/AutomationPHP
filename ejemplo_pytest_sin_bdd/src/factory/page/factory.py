from src.factory.page.listado_paginas import Paginas
from src.page_objects.boveda_central.apertura_boveda_central import AperturaBovedaPage
from src.page_objects.boveda_central.cierre_total_boveda import CierreTotalBovedaPage
from src.page_objects.boveda_central.no_asociada import BovedaNoAsociadaPage
from src.page_objects.caja.apertura_caja import AperturaCajaPage
from src.page_objects.caja.caja_bloqueada import CajaBloqueadaPage
from src.page_objects.caja.cierre_parcial_caja import CierreParcialCajaPage
from src.page_objects.caja.cierre_total_caja import CierreTotalCajaPage
from src.page_objects.caja.declaracion_jurada import DeclaracionJuradaPage
from src.page_objects.caja.gestion_de_caja import GestionDeCajaPage
from src.page_objects.caja.no_asociada import CajaNoAsociadaPage
from src.page_objects.configuracion.configuracion import Configuracion
from src.page_objects.dashboard.dashboard import DashboardPage
from src.page_objects.default.default import DefaultPage
from src.page_objects.login.login import Login
from src.page_objects.operaciones.operaciones import OperacionesPage
from src.page_objects.operaciones.transferencias_entrantes import TransferenciasEntrantesPage
from src.page_objects.operaciones.transferencias_salientes import TransferenciasSalientesPage
from src.page_objects.sucursales.agregar_sucursal import AgregarSucursal
from src.page_objects.sucursales.editar_sucursal import EditarSucursalPage
from src.page_objects.sucursales.sucursal_page import SucursalPage


class PageFactory(object):

    def __init__(self):
        self.driver = None
        self.history = PageHistory()
        self.observer = PageObserver()

    def create_from(self, page_object):
        if page_object.next_page is None:
            raise ValueError(f"{page_object.__class__} no tiene asignadaa una pagina siguiente")
        return self._create(page_object.next_page)

    def create_with_name(self, class_name, refresh):
        if refresh:
            self.driver.refresh()
        return self._create(class_name)

    def get_login(self):
        return self._create(Paginas.Login)

    def _create(self, name):
        try:
            page = self.__paginas[name]
        except KeyError:
            raise ValueError(f"la key '{name}' no tiene asignado un pageobject")

        validate_page = self.history.add_if_not_exits(page)
        page = page(self.driver, validate_page)
        page.observer = self.observer
        return page

    def switch_driver(self, new_driver):
        self.driver = new_driver

    __paginas = {
        Paginas.Dashboard: DashboardPage,
        Paginas.Default: DefaultPage,
        Paginas.BovedaNoAsociada: BovedaNoAsociadaPage,
        Paginas.CajaNoAsociada: CajaNoAsociadaPage,
        Paginas.AperturaCaja: AperturaCajaPage,
        Paginas.AperturaBoveda: AperturaBovedaPage,
        Paginas.CierreTotalBoveda: CierreTotalBovedaPage,
        Paginas.CierreTotalCaja: CierreTotalCajaPage,
        Paginas.CierreParcialCaja: CierreParcialCajaPage,
        Paginas.CajaBloqueada: CajaBloqueadaPage,
        Paginas.Configuracion: Configuracion,
        Paginas.Login: Login,
        Paginas.Sucursal: SucursalPage,
        Paginas.AgregarSucursal: AgregarSucursal,
        Paginas.EditarSucursal: EditarSucursalPage,
        Paginas.OperacionesCaja: OperacionesPage,
        Paginas.DeclaracionJurada: DeclaracionJuradaPage,
        Paginas.TransferenciasSalientes: TransferenciasSalientesPage,
        Paginas.TransferenciasEntrantes: TransferenciasEntrantesPage,
        Paginas.GestionDeCaja: GestionDeCajaPage
    }


class PageHistory:

    def __init__(self):
        self.instance_history = []


    def add_if_not_exits(self, class_name):
        # todo: esto no tiene que hacerlo el page ya que estos metodos contienen cierta logica de dominio,
        #  quizas deberia armar hooks/observers en las actions para que un "ValidationHandler" o similar,
        #  se subscriba y realice acciones similares a los validar pantalla
        return False
        # if class_name in self.instance_history:
        #     return False
        # self.instance_history.append(class_name)
        # return False

    def reset_history(self):
        self.instance_history = []


class PageObserver:

    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def notify(self):
        for subscriber in self._subscribers:
            subscriber.update()
