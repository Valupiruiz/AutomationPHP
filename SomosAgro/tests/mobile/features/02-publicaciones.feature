# Created by tomas at 1/6/2020
Feature: crear publicaciones desde la aplicación
  Como un usuario publicador necesito realizar publicaciones

  Background:
    Given ingreso a la aplicacion
    And ingreso con Facebook
    And me encuentro en la pantalla principal

  Scenario: crear publicacion gratuita
    Given quiero crear una publicacion gratuita
    And me dirijo a tab nuevo_feed
    When selecciona tipo publicacion
    And selecciona cantidad de dias
    And ingresa descripcion
    And selecciona foto y recorta
    And selecciona intereses
    And selecciona zona
    Then verifico datos de la vista previa
    And la publicación es creada
    And me deslogueo

  @wip
  Scenario: crear publicacion premium
    Given me dirijo a tab nuevo_feed
    When selecciona tipo publicacion
    And selecciona cantidad de dias
    And ingresa descripcion
    And selecciona foto y recorta
    And selecciona intereses
    And selecciona zona
    And realiza el pago
    Then verifico datos de la vista previa
    And la publicación es creada
    And me deslogueo

  Scenario: editar publicacion
    Given me dirijo a tab usuario
    When selecciona publicaciones vigentes
    And selecciono para editar una publicacion
    And modifico descripcion
    And modifico intereses
    And modifico zona
    Then verifico datos de la vista previa
    And la publicacion es editada
    And me deslogueo

  Scenario: eliminar publicacion
    Given me dirijo a tab usuario
    When selecciona publicaciones vigentes
    And selecciono para eliminar una publicacion
    And selecciono opcion para eliminar
    Then la publicacion queda eliminada
    And me deslogueo
