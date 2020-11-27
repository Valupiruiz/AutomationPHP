from selenium.webdriver.common.by import By
from page_objects.base_page import Locator

class OrganismoLocators:
    orga_agregar_BTN = Locator(By.XPATH, "//a[@class='btn btn-info btn-sm pull-right botonnuevo']")
    nuevo_organismo_LBL = Locator(By.XPATH, "//h3[contains(text(),'Nuevo organismo')]")

    orga_nombre_INP = Locator(By.ID, "OrganismoType_nombre")
    orga_cuit_INP = Locator(By.ID, "OrganismoType_cuit")
    orga_sec_INP = Locator(By.ID, "OrganismoType_sector")
    orga_buz_gru_INP = Locator(By.ID, "OrganismoType_buzonGrupal" )
    orga_codigo_gde_INP = Locator(By.ID, "OrganismoType_codigo")
    orga_excento_CHK = Locator(By.ID,"OrganismoType_exento")
    orga_sis_utilizar_SEL = Locator(By.XPATH, "//span[contains(text(),'Buscar ...')]")
    orga_sis_utilizar_op1_LB = Locator(By.XPATH, "//label[contains(text(),'Presidencia')]")
    orga_sis_utilizar_op2_LB = Locator(By.XPATH, "//label[contains(text(),'COMPRAR')]")
    orga_sis_utilizar_op3_LB = Locator(By.XPATH, "//label[contains(text(),'TAD')]")
    orga_sis_utilizar_op4_LB = Locator(By.XPATH, "//li[@class='opt']//label[contains(text(),'GDE')]")
    orga_activo_CHK = Locator(By.ID, "OrganismoType_activo")

    orga_direc_calle_INP = Locator(By.ID, "OrganismoType_calle")
    orga_direc_numero_INP = Locator(By.ID, "OrganismoType_numero")
    orga_direc_piso_INP = Locator(By.ID, "OrganismoType_piso")
    orga_direc_depto_INP = Locator(By.ID, "OrganismoType_deptoOficina")
    orga_direc_cod_postal_INP = Locator(By.ID, "OrganismoType_codigoPostal")
    orga_direc_prov_ba_option = Locator(By.XPATH, "//div[@class='col-md-12 margin-bottom-10']//option[2]")
    orga_direc_prov_SEL = Locator(By.XPATH, "//select[@id='OrganismoType_provincia']")
    orga_direc_partido_INP = Locator(By.ID, "OrganismoType_partido")
    orga_direc_localidad_INP = Locator(By.ID, "OrganismoType_localidad")

    orga_pub0_TAB = Locator(By.XPATH,"//div[@id='heading_OrganismoType_publicadores_0']//a[@class='collapsed'][contains(text(),'Nuevo contacto')]")
    orga_pub0_nombre_INP = Locator(By.ID, "OrganismoType_publicadores_0_nombre")
    orga_pub0_apellido_INP = Locator(By.ID, "OrganismoType_publicadores_0_apellido")
    orga_pub0_cuil_INP = Locator(By.ID, "OrganismoType_publicadores_0_cuil")
    orga_pub0_tel_INP = Locator(By.ID, "OrganismoType_publicadores_0_telefono")
    orga_pub0_mail_INP = Locator(By.ID, "OrganismoType_publicadores_0_mail")
    orga_pub0_usugde_INP = Locator(By.ID, "OrganismoType_publicadores_0_usuarioGDE")
    orga_pub0_activo_CHK = Locator(By.XPATH, "//input[@id='OrganismoType_publicadores_0_activo']")

    orga_pub1_texto_LBL = Locator(By.XPATH, "//a[contains(text(),'Nuevo contacto')]")
    orga_pub1_nombre_INP = Locator(By.ID, "OrganismoGDEType_publicadores_2_nombre")
    orga_pub1_apellido_INP = Locator(By.ID, "OrganismoGDEType_publicadores_2_apellido")
    orga_pub1_cuil_INP = Locator(By.ID, "OrganismoGDEType_publicadores_2_cuil")
    orga_pub1_tel_INP = Locator(By.ID, "OrganismoGDEType_publicadores_2_telefono")
    orga_pub1_mail_INP = Locator(By.ID, "OrganismoGDEType_publicadores_2_mail")
    orga_pub1_usugde_INP = Locator(By.ID, "OrganismoGDEType_publicadores_2_usuarioGDE")
    orga_pub1_activo_CHK = Locator(By.ID, "OrganismoGDEType_publicadores_2_activo")

    orga_fac0_TAB = Locator(By.XPATH, "//div[@id='heading_OrganismoType_pagadores_0']//a[@class='collapsed'][contains(text(),'Nuevo contacto')]")
    orga_fac0_nombre_INP = Locator(By.ID, "OrganismoType_pagadores_0_nombre")
    orga_fac0_apellido_INP = Locator(By.ID, "OrganismoType_pagadores_0_apellido")
    orga_fac0_cuil_INP = Locator(By.ID, "OrganismoType_pagadores_0_cuil")
    orga_fac0_tel_INP = Locator(By.ID, "OrganismoType_pagadores_0_telefono")
    orga_fac0_mail_INP = Locator(By.ID, "OrganismoType_pagadores_0_mail")
    orga_fac0_activo_CHK = Locator(By.ID, "OrganismoType_pagadores_0_activo")
    orga_fac0_agregar_BTN = Locator(By.XPATH, "//a[contains(text(), 'Agregar Facturador')]")

    dep_agregar_BTN = Locator(By.XPATH, "//button[contains(text(),'Agregar Dependencia')]")
    dep0_nombre_INP = Locator(By.ID, "DependenciaOrganismoGDEType_nombre")
    dep0_codigo_gde_INP = Locator(By.ID, "DependenciaOrganismoGDEType_codigo")
    dep0_sec_INP = Locator(By.ID, "DependenciaOrganismoGDEType_sector")
    dep0_buz_gru_INP = Locator(By.ID, "DependenciaOrganismoGDEType_buzonGrupal")
    dep0_cuit_INP = Locator(By.ID, "DependenciaOrganismoGDEType_cuit")
    dep0_act_CHK = Locator(By.ID, "DependenciaOrganismoGDEType_publicadores_0_activo")
    dep0_direc_calle_INP = Locator(By.ID, "DependenciaOrganismoGDEType_calle")
    dep0_direc_numero_INP = Locator(By.ID, "DependenciaOrganismoGDEType_numero")
    dep0_cod_postal_INP = Locator(By.ID, "DependenciaOrganismoGDEType_codigoPostal")
    dep0_prov_SEL = Locator(By.ID, "DependenciaOrganismoGDEType_provincia")
    dep0_partido_INP = Locator(By.ID, "DependenciaOrganismoGDEType_partido")
    dep0_localidad_INP = Locator(By.ID, "DependenciaOrganismoGDEType_localidad")

    dep0_pub_TAB = Locator(By.XPATH, "//div[@id='heading_DependenciaOrganismoGDEType_publicadores_0']//a[@class='collapsed'][contains(text(),'Nuevo contacto')]")
    dep0_pub_nombre_INP = Locator(By.ID, "DependenciaOrganismoGDEType_publicadores_0_nombre")
    dep0_pub_apellido_INP = Locator(By.ID, "DependenciaOrganismoGDEType_publicadores_0_apellido")
    dep0_pub_cuil_INP = Locator(By.ID, "DependenciaOrganismoGDEType_publicadores_0_cuil")
    dep0_pub_tel_INP = Locator(By.ID, "DependenciaOrganismoGDEType_publicadores_0_telefono")
    dep0_pub_mail_INP = Locator(By.ID, "DependenciaOrganismoGDEType_publicadores_0_mail")
    dep0_pub_usuario_gde_INP = Locator(By.ID, "DependenciaOrganismoGDEType_publicadores_0_usuarioGDE")

    dep0_fac_TAB = Locator(By.XPATH, "//div[@id='heading_DependenciaOrganismoGDEType_pagadores_0']//a[@class='collapsed'][contains(text(),'Nuevo contacto')]")
    dep0_fac_nombre_INP = Locator(By.ID, "DependenciaOrganismoGDEType_pagadores_0_nombre")
    dep0_fac_apellido_INP = Locator(By.ID, "DependenciaOrganismoGDEType_pagadores_0_apellido")
    dep0_fac_cuil_INP = Locator(By.ID, "DependenciaOrganismoGDEType_pagadores_0_cuil")
    dep0_fac_tel_INP = Locator(By.ID, "DependenciaOrganismoGDEType_pagadores_0_telefono")
    dep0_fac_mail_INP = Locator(By.ID, "DependenciaOrganismoGDEType_pagadores_0_mail")


    dep0_sub0_agregar_BTN = Locator(By.XPATH, "//i[@class='fa fa-plus fa-lg']" )
    titulo_sub_LBL = Locator(By.XPATH, "//h4[@id='myModalLabel']")
    orga_guardar_BTN = Locator(By.XPATH, "//button[@id='guardar']")
    dep_guardar_BTN = Locator(By.XPATH, "//button[@id='guardarDep']")
    agregar_publicador_dep_BTN = Locator(By.XPATH, "//div[@class='modal-body']//div[@class='row']//div[@class='col-md-12']//div//a[@class='puntero text-14px'][contains(text(),'Agregar Publicador')]"
                                         )
    agregar_facturador_dep_BTN = Locator(By.XPATH, "//div[@class='modal-body']//div[@class='row']//div[@class='col-md-12']//div//a[@class='puntero text-14px'][contains(text(),'Agregar Facturador')]")
    mensaje_MSJ = Locator(By.XPATH, "//div[@class='alert alert-success']")

    orga_nombre_filtro_INP = Locator(By.ID, "OrganismoGDESearchType_nombre")
    orga_buscar_BTN = Locator(By.XPATH, "//button[@class='btn btn-default btn-sm']")
    orga_lapiz_modif_BTN = Locator(By.XPATH, "//i[@class='fa fa-pencil fa-lg']")
    orga_una_pagina_LB = Locator(By.XPATH, "//a[@class='puntero'][contains(text(),'1')]")
    orga_estado_SEL = Locator(By.XPATH, "//span[@class='placeholder']")
    orga_estado_inactivo_OP = Locator(By.XPATH, "//label[contains(text(),'Inactivos')]")
    orga_activar_BTN = Locator(By.XPATH, "//i[@class='fa fa-check fa-lg']")
    orga_aceptar_activo_BTN = Locator(By.XPATH,"//div[@id='activar_org']//button[@class='btn btn-sm btn-primary'][contains(text(),'Aceptar')]")
    dep1_subdep0_activo_CHK = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_activo")

    dep_pub_activo_CHK = Locator(By.ID, "DependenciaOrganismoGDEType_publicadores_0_activo")
    TEMP_LOCATOR_MENSAJE = Locator(By.XPATH, "//div[contains(text(),'{mensaje}')]")

    @staticmethod
    def locator_dep_dos_btn(nombre_dep):
        return Locator(By.XPATH, "//a[contains(text(), '" + nombre_dep + "')]")


