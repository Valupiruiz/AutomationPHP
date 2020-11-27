Feature: Apyc con tope maximo por categoria cultural previo 678

  Scenario: Cargo apyc
    Given me encuentro en la pagina principal
    And ingreso con usuario docente
    And me encuentro en principal docente
    When me dirijo a Documentación -> Agregar antecedentes pedagógicos y culturales
    And cargo apyc previo decreto 678 categoria 1
    Then se cargo exitosamente el apyc
    And cierro sesion

  Scenario: Calcular puntaje
    Given me encuentro en la pagina principal
    And ingreso con usuario administrador
    And me encuentro en principal backend
    When me dirijo a Docentes -> Buscador
    And aprobar documentacion de apyc previo decreto 678 categoria
    And me dirijo a Calcuador -> Control
    When calcular puntaje
    Then verificar puntaje de apyc previo decreto 678 categoria
    And cierro sesion

  Scenario: Revertir aprobacion apyc
    Given me encuentro en la pagina principal
    And ingreso con usuario administrador
    And me encuentro en principal backend
    When me dirijo a Docentes -> Buscador
    And revertir aprobacion de apyc previo decreto 678 categoria
    Then cierro sesion



