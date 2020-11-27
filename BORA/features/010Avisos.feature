Feature: Avisos

  Scenario Outline: Acta
     Given Estoy logueado como usuario Tomas
     And Envio informacion del  aviso de tipo actaDos
     And Envio documento
     And Envio anexos
     When Me dirijo a Avisos, Verificacion
     Then Visualizar aviso
     When Cambio fecha y Agrego aviso a Suplemento 2
     And  Cambio de rubro a <campo>
     And Aprobar aviso en estado Pendiente de Verificacion
     Then Se aprobo con exito
     And Cerrar sesion

   Examples: Campos
   | campo  |
#   |Acta|
#   |Resolución|
#   |Asociaciones Sindicales|
#   |Audiencias Públicas|
#   |Avisos Oficiales|
#   |Concursos Oficiales|
#   |Convenciones Colectivas de Trabajo|
#   |Disposición|
#   |Disposición Conjunta|
#   |Fallos|
#   |Instrucción|
#   |Instrucción General|
   |Laudos|
   |Remates Oficiales|
   |Tratados y Convenios Internacionales|
   |Resolución Conjunta|
   |Resolución General|
   |Resolución sintetizada|
   |Disposición sintetizada|
   |CSJN Acordadas|