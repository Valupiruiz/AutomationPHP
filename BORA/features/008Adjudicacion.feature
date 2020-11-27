Feature: Crear y verificar aviso Adjudicacion

  Scenario: Crear un aviso 1era ley
     Given  Estoy logueado como usuario Tomas
     And  Envio informacion del  aviso de tipo adjudicacion
     And Envio documento
     And Envio anexos

  Scenario: Verificar estado aviso, documentos, anexos, firmantes
    When Me dirijo a Avisos, Verificacion
    And Visualizar aviso
    When Aprobar aviso en estado Pendiente de Verificacion
    Then Se aprobo con exito

  Scenario: Verificar texto de documento
    When Me dirijo a Avisos, Bandeja de Tramites
    Then Verificar que el aviso este en estado Pendiente de Publicación
    And Visualizar aviso
    When Descargar documento del aviso
    And Voy a descargar pdf del texto del aviso
    Then Verificar texto de documento de texto
    When Guardo aviso en estado Pendiente de publicación
    Then Cerrar sesion

