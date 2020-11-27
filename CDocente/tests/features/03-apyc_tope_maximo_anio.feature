Feature: Apyc con tope maximo por anio cultural previo 678

  Scenario Outline: Cargo apyc
    Given me encuentro en la pagina principal
    And ingreso con usuario docente
    And me encuentro en principal docente
    When me dirijo a Documentación -> Agregar antecedentes pedagógicos y culturales
    And cargo apyc previo decreto 678 anio <veces>
    Then se cargo exitosamente el apyc
    And cierro sesion
    Examples: Campos
   | veces  |
   | 1 |
   | 2 |

  Scenario: Calcular puntaje
    Given me encuentro en la pagina principal
    And ingreso con usuario administrador
    And me encuentro en principal backend
    When me dirijo a Docentes -> Buscador
    And aprobar documentacion de apyc previo decreto 678 anio
    And me dirijo a Calcuador -> Control
    When calcular puntaje
    Then verificar puntaje de apyc previo decreto 678 anio
    And cierro sesion

  Scenario: Revertir aprobacion apyc
    Given me encuentro en la pagina principal
    And ingreso con usuario administrador
    And me encuentro en principal backend
    When me dirijo a Docentes -> Buscador
    And revertir aprobacion de apyc previo decreto 678 anio
    Then cierro sesion








