Feature: Crear, verificar aviso ley, documentos y texto del pdf

  Scenario: Crear un aviso 1era ley
     Given Estoy logueado como usuario Tomas
     And  Envio informacion del  aviso de tipo ley
     And Envio documento
     And Envio anexos

  Scenario: Verificar estado aviso, documentos, anexos, firmantes
    When Me dirijo a Avisos, Verificacion
    And Visualizar aviso
    When Voy a descargar pdf del texto del aviso
    Then Verificar texto de documento de texto
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
    Then Se guardo correctamente

  Scenario: Agrego aviso a OA Suplementos
    When Agregar aviso a OA de suplementos
    And Me dirijo a Avisos, Bandeja de Tramites
    And visualizar aviso
    And Guardo aviso en estado requiere aprobacion
    Then Se guardo correctamente
    And Verificar que el aviso este en estado Pendiente de publicación
    Then cerrar sesion

