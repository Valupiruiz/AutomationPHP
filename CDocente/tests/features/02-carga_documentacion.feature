Feature: Cargar Documentacion

  Scenario: Cargo datos faltantes
    Given me encuentro en la pagina principal
    And ingreso con usuario docente
    And me encuentro en principal docente
    When me dirijo a Mis datos -> Datos personales
    And completo datos faltantes
    And me dirijo a Inscripciones -> Seleccionar distritos -> Periodo Ordinario 2021 Int y Supl 2022
    And cargo distritos
    Then cierro sesion

 Scenario: Cargo titulo
    Given me encuentro en la pagina principal
    And ingreso con usuario docente
    And me encuentro en principal docente
    When me dirijo a Documentación -> Agregar título
    And cargo titulo
    Then cierro sesion

  Scenario: Aprobar documentacion
   Given me encuentro en la pagina principal
   And ingreso con usuario administrador
   And me encuentro en principal backend
   And me dirijo a Docentes -> Buscador
   When aprobar documentacion de titulo
   Then cierro sesion

 Scenario: Inscripcion a cargo
   Given me encuentro en la pagina principal
   And ingreso con usuario docente
   And me encuentro en principal docente
   When nueva inscripcion
   Then cierro sesion

  Scenario: Deshabilitar usuario
   Given me encuentro en la pagina principal
   And ingreso con usuario administrador
   And me encuentro en principal backend
   And me dirijo a Administración -> Usuarios -> Usuarios @bue
   When deshabilito y cambio mail
   Then cierro sesion

 Scenario: Cargo curso
   Given me encuentro en la pagina principal
   And ingreso con usuario docente
   And me encuentro en principal docente
   And me dirijo a Documentación -> Agregar cursos
   When agrego curso
   Then se aprobo exitosamente el curso
   And cierro sesion

