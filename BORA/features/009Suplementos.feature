Feature: OA de suplementos

  Scenario: Crear suplemento
    Given Estoy logueado como usuario Tomas
    When Me dirijo a Cierre de edición, Orden de armado suplementos
    And Creo OA suplementos

  Scenario: agregar suplementos a OA
    When Me dirijo a Avisos, Bandeja de Tramites
    And Agrego avisos a suplemento
    And Me dirijo a Cierre de edición, Orden de armado suplementos
    And Cambio numero de edicion
    Then Verificar avisos en el pdf de la orden



