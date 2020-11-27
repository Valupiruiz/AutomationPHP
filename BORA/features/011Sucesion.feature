Feature: Crear y verificar aviso de sucesion

  Scenario: Crear un aviso 2da sucesion
     Given Estoy logueado como usuario Tomas
     When Me dirijo a Administracion, Organismos Judiciales
     And Crear organismo Judicial
     Then El organismo judicial se crea existosamente

  Scenario: Envio informacion del tipo de aviso Sucesion
    Given Envio informacion del  aviso de tipo sucesion
    And Envio documento
    And Envio anexos

   Scenario: Aviso En pendiente de verificacion Sucesion
    When Me dirijo a Avisos, Verificacion
    Then Verificar que el aviso este en estado Pendiente de verificación
    And Visualizar aviso

  Scenario Outline: Verificar advertencia de <campo> aprobando y guardando el aviso en estado Pendiente de Verificacion
    When Modifico <campo> erroneamente en estado Pendiente de verificacion
    And Aprobar aviso en estado Pendiente de Verificacion
    And Guardo aviso en estado Pendiente de verificacion
    Then Verificar advertencia <campo>
    When Modifico <campo> correctamente

    Examples: Campos
   | campo           |
   | dias            |
   | anio expediente |
   | nro expediente  |

  Scenario: Apruebo aviso y lo pago en judiciales
    Given Aprobar aviso en estado Pendiente de Verificacion
    Then Se aprobo con exito
    When Nueva pestania de judiciales
    And Pagar aviso
    Then Se hizo el pago con exito
    When Volver a BOW
    And  Me dirijo a Avisos, Bandeja de Tramites
    Then Verificar que el aviso este en estado Pendiente de Publicación
    And Cerrar sesion






