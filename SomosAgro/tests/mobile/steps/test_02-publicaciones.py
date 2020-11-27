from pytest_bdd import given, when, then, scenario, parsers
from src.sag_data.app_constants import PRECIO_DIA_PUBLICACION
from src.domain.publicacion import TipoPublicacion
import pytest_check as check


@scenario("../features/02-publicaciones.feature", "crear publicacion gratuita")
def test_publicacion_gratuita(context):
    pass


@given("quiero crear una publicacion gratuita")
def get_publicacion_gratuita(context, publicacion_gratuita):
    context["publicacion"] = publicacion_gratuita


@when(parsers.parse("selecciona tipo publicacion"))
def seleccionar_tipo(context):
    context["act"] = context["act"].seleccionar_tipo_publicacion(context["publicacion"].tipo)


@when("selecciona cantidad de dias")
def seleccionar_cantidad_dias(context):
    context["act"].seleccionar_dias(context["publicacion"].cantidad_dias)
    precio = 0
    if context["publicacion"].tipo == TipoPublicacion.PREMIUM:
        precio = PRECIO_DIA_PUBLICACION * context["publicacion"].cantidad_dias
    check.equal(precio, context["act"].get_precio())
    context["act"] = context["act"].continuar()


@when("ingresa descripcion")
def ingresar_descripcion(context):
    context["act"].completar_campos(context["publicacion"])
    context["act"] = context["act"].continuar()


@when("selecciona foto y recorta")
def seleccionar_foto(context):
    context["act"].seleccionar_foto()
    context["act"] = context["act"].continuar()


@when("selecciona intereses")
def seleccionar_intereses(context):
    context["act"].tocar_interes(context["publicacion"].interes.nombre)
    context["act"].tocar_subinteres(context["publicacion"].subinteres)
    context["act"].aceptar_subinteres()
    context["act"] = context["act"].continuar()


@when("selecciona zona")
def seleccionar_zona(context):
    context["act"].tocar_zona(context["publicacion"].zona)
    context["act"] = context["act"].continuar_zonas()


@then("verifico datos de la vista previa")
def verifcar_vista_previa(context):
    check.equal(context["publicacion"].cabecera.titulo, context["act"].get_vp_titulo())
    check.equal(context["publicacion"].ipseudonimo, context["act"].get_vp_etiqueta().lower())
    check.equal(context["publicacion"].zona.lower(), context["act"].get_vp_zona())
    check.equal(context["publicacion"].cabecera.sintesis, context["act"].get_vp_sintesis())
    if context["publicacion"].tipo == TipoPublicacion.PREMIUM:
        check.equal(context["publicacion"].cabecera.descripcion, context["act"].get_vp_descripcion())


@then("la publicación es creada")
def verificar_creacion_publicacion(context):
    # TODO: check a la base
    context["act"].publicar("Publicar")


@when("realiza el pago")
def realizar_pago(context):
    # no funciona en ambiente de test
    pass


@scenario("../features/02-publicaciones.feature", "editar publicacion")
def test_editar_publicacion():
    pass


@when("selecciona publicaciones vigentes")
def seleccionar_publicaciones_vigentes(context):
    context["act"].ir_publicaciones_vigentes()


@when(parsers.parse("selecciono para {accion} una publicacion"))
def edicion_publicacion(context, accion):
    context["publicacion_anterior"] = context["publicacion"]
    context["act"].seleccionar_opciones_publicacion()
    # dump = json.dumps(context["publicacion"].__dict__, default=lambda o: o.__dict__, ensure_ascii=False)
    # cabecera = Publicacion.from_json(json.loads(dump))
    context["act"] = context["act"].seleccionar_opcion(accion)

@scenario("../features/02-publicaciones.feature", "eliminar publicacion")
def test_eliminar_publicacion():
    pass

@when("selecciono opcion para eliminar")
def opcion_eliminar(context):
    context["act"].eliminar()

@then("la publicacion queda eliminada")
def publicacion_eliminada(context):
    pass


@when("modifico descripcion")
def modificar_descripcion(context, publicacion_editada):
    context["publicacion"] = publicacion_editada
    context["act"].editar_campos(context["publicacion"])
    context["act"] = context["act"].continuar_editar()


@when("modifico intereses")
def modificar_intereses(context):
    context["act"].tocar_interes(context["publicacion_anterior"].interes.nombre)
    context["act"].tocar_subinteres(context["publicacion_anterior"].subinteres)
    context["act"].aceptar_subinteres()
    context["act"].tocar_interes(context["publicacion"].interes.nombre)
    context["act"].tocar_subinteres(context["publicacion"].subinteres)
    context["act"].aceptar_subinteres()
    context["act"] = context["act"].continuar()


@when("modifico zona")
def modificar_zona(context):
    context["act"].tocar_zona(context["publicacion_anterior"].zona)
    context["act"].tocar_zona(context["publicacion"].zona)
    context["act"] = context["act"].continuar_zonas()


@then("la publicacion es editada")
def guardar_edicion_publicacion(context):
    context["act"].guardar()
