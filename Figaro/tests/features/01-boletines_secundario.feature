# Created by tomas at 1/4/2020
Feature: Boletines secundario
  Se realizan distintas acciones que hacen

  Background:
    Given me encuentro en la pantalla principal de secundario
    And ingreso al sistema con usuario <usuario>
    And verifico ciclo y sub-colegio
    And me dirijo a solapa Materias
    And selecciono una materia
    And cambio a vista de Evaluaciones

  @crear_evaluaciones
  Scenario: Crear evaluaciones
    When creo las evaluaciones
    Then salgo

  @calificar_evaluaciones
  Scenario: Calificar evaluaciones
    When Solicito la planilla de evaluaciones
    And Califico evaluaciones
    Then verifico promedios
    And vuelvo a pestaña principal
    And salgo

  @verificar_ausencias
  Scenario: Verificar ausencias
    When Solicito la planilla de evaluaciones
    And marco alumno como ausente y verifico promedios
    Then marco alumno como presente y verifico promedios
    And vuelvo a pestaña principal
    And salgo

  Scenario: Excluir evaluación
    When excluye la evaluacion
    And Solicito la planilla de evaluaciones
    Then verifico promedios
    And salgo

  Scenario: Volver a incluir evaluacion
    When incluye la evaluacion
    And Solicito la planilla de evaluaciones
    Then verifico promedios
    And salgo

  Scenario: cambiar fecha de evaluación en otro periodo
    When edita la evaluacion
    And Solicito la planilla de evaluaciones
    Then verifico promedios
    And salgo

  Scenario: cerrar materia
    When cierro la materia
    And Solicito la planilla de evaluaciones
    Then verifico promedio final
    And salgo
