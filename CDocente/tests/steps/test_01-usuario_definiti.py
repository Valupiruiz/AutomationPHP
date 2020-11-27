from pytest_bdd import given, when, then, scenario
from page_objects.nuevo_usuario.nuevo_usuario import NuevoUsuario
import pytest_check as check
from page_objects.usuarios_temporales.usuarios_temporales import UsuariosTemporales
from page_objects.usuarios_bue.usuarios_bue import UsuariosBue



@scenario("../features/01-usuario_definitivo.feature", "Usuario Definitivo")
def test_usuario_definitivo():
    pass



@given('creo usuario')
def creo_usuario(context, docente_test5):
    context["page"].nuevo_usuario()
    context["page"] = NuevoUsuario(context["driver"])
    context["page"].completar_datos_personales(docente_test5)
    context["page"].completar_direccion_personal(docente_test5)
    context["page"].completar_email_contra(docente_test5)
    context["page"].guardar()
    check.equal(context["page"].creacion_correcta(), "×\nLa registración se ha realizado con éxito. Se le envió un mail con un link para completar la activación de su cuenta.",
                f'obtuve {context["page"].creacion_correcta()}')


@when("habilitar usuario temporal")
def habilitar_usuario(context, docente_test5):
    context["page"] = UsuariosTemporales(context["driver"])
    context["page"].habilitar_usuario(docente_test5.mail_temportal)
    check.equal(context["page"].cambio_correcto(), "×\nEl Usuario Temporal se habilitó correctamente.",
                f'obtuve {context["page"].cambio_correcto()}')
    context["page"].cambiar_mail(docente_test5.mail_temportal, docente_test5.mail)
    check.equal(context["page"].cambio_correcto(), "×\nEl usuario se ha validado con éxito.",
                f'obtuve {context["page"].cambio_correcto()}')
