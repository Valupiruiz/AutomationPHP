Feature: Usuario definitivo

@usuario_definitivo
Scenario: Usuario Definitivo
    Given me encuentro en la pagina principal
    And creo usuario
    When me encuentro en la pagina principal
    And ingreso con usuario administrador
    And me encuentro en principal backend
    And me dirijo a Administración -> Usuarios -> Usuarios temporales
    And habilitar usuario temporal
    Then cierro sesion