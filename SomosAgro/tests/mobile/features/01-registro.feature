# Created by tmoreira at 11/3/2020
@con_registro
Feature: Registro de usuarios
  El usuario debe poder registrarse y loguearse mediante Facebook y Google

  Scenario: intentar login exitoso con Facebook
    Given ingreso a la aplicacion
    When ingreso con Facebook
    And completo datos de registro y aprieto en continuar
    And completo intereses
    And completo zonas
    And acepto terminos y condiciones
    Then quedo registrado en la aplicacion
    And se muestra la pantalla principal
    And me deslogueo

  #TODO: agregar los otros casos de login (Google, Facebook sin app)
