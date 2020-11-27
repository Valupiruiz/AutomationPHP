from pytest_bdd import when, then, scenario
from src.mobile.user_interface.activities.registro_info_activity import RegistroInfoActivity


@scenario('../features/01-registro.feature', 'intentar login exitoso con Facebook')
def test_login_facebook_app():
    pass


@when("completo datos de registro y aprieto en continuar")
def completar_registro(context):
    context["act"] = RegistroInfoActivity(context["driver"])
    context["act"] = context["act"].completar_datos_registro_y_continuar(context["user"])


@when("completo intereses")
def completar_intereses(context, interes_todos):
    context["act"].tocar_intereses_y_subintereses(interes_todos)
    context["act"] = context["act"].continuar()


@when("completo zonas")
def completar_zonas(context, todas_las_zonas):
    context["act"].tocar_zonas(todas_las_zonas)
    context["act"] = context["act"].continuar_zonas_login()


@when("acepto terminos y condiciones")
def acepto_terminos_condiciones(context):
    context["act"] = context["act"].aceptar()


@then("quedo registrado en la aplicacion")
def verificar_registro(context):
    context["act"] = context["act"].empezar_bienvenida()
    # TODO: hacer assert contra la base
