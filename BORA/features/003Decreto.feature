Feature: Crear, verificar aviso Decreto y verificacion de campos
  Scenario: Crear un Organismo con publicador inactivo
    Given Estoy logueado como usuario Tomas
    And Me dirijo a Administracion, Organismos Nuevo
    When Creo un organismo
    Then El organismo se crea existosamente
    When Agrego dependencia
    Then La dependencia se agrego exitosamente
    When Agrego subdepdendencia
    Then La subdependencia se agrego exitosamente

  Scenario: Crear un aviso 1era decreto
     Given Envio informacion del  aviso de tipo decreto
     And Envio documento
     And Envio anexos
     When Me dirijo a Avisos, Bandeja de Tramites
     Then Verificar que el aviso este en estado Pendiente de rechazo

  Scenario: Firmante valido
    Given Obtengo el firmante  que no existe
    When Me dirijo a Administracion, Firmantes
    And Creo firmante
    Then Creación exitosa firmante

  Scenario: Activar organismo
    Given Me dirijo a Administracion, Organismos Nuevo
    When Activar organismo
    Then El organismo se modifico existosamente

  Scenario: Reprocesar aviso
    When Me dirijo a Avisos, Bandeja de Tramites
    And Reprocesar aviso
    Then Se reproceso correctamente

  Scenario: Aviso En pendiente de verificacion
    When Me dirijo a Avisos, Verificacion
    Then Verificar que el aviso este en estado Pendiente de verificación
    And Visualizar aviso

  Scenario Outline: Verificar advertencia de <campo> aprobando y guardando el aviso en estado Pendiente de Verificacion
    When Modifico <campo> erroneamente en estado Pendiente de verificacion
    And Aprobar aviso en estado Pendiente de Verificacion
    When Guardo aviso en estado Pendiente de verificacion
    Then Verificar advertencia <campo>
    When Modifico <campo> correctamente

    Examples: Campos
   | campo  |
   | dias   |
   | firma  |
#   | fecha  |

  Scenario: Verificar estado aviso y firmantes
    When Aprobar aviso en estado Pendiente de Verificacion
    Then Se aprobo con exito
    And Me dirijo a Avisos, Bandeja de Tramites
    Then Verificar que el aviso este en estado Pendiente de Publicación
    And Verificar orden de firmantes

  Scenario Outline: Modificar aviso
    When Modifico <campo> erroneamente en estado Pendiente de publicación
    And Guardo aviso en estado Pendiente de publicación
    Then Verificar advertencia <campo>
    When Modifico <campo> correctamente

    Examples: Campos
   | campo  |
   | dias   |
   | firma  |
#   | fecha  |

  Scenario: Verificar estado de aviso requiere aprobacion
    When Guardo aviso en estado Pendiente Publicacion
    Then Se guardo correctamente
    And Verificar que el aviso este en estado Requiere Aprobación
    And Visualizar aviso


  Scenario Outline: Aprobar aviso con campo <campo>
    When Modifico <campo> erroneamente en estado Requiere Aprobación
     And Guardo aviso en estado requiere aprobacion
    Then Verificar advertencia <campo>
    When Modifico <campo> correctamente
    Examples: Campos
   | campo  |
   | dias   |
   | firma  |
#   | fecha  |

    Scenario: Verificar documento de aviso y estado de aviso Pendiente de publicacion
    When Descargar documento del aviso
    And Agregar aviso a OA de suplementos
    And Guardo aviso en estado requiere aprobacion
    Then Se guardo correctamente
    And Verificar que el aviso este en estado Pendiente de publicación
    And Cerrar sesion

#    Scenario:  Enviar a publicaciones dos veces
#    When Publicar aviso
#    Then Informacion enviada exitosamente
