from selenium.webdriver.common.by import By
from page_objects.base_page import Locator

class OrganismoLocators:
    orga_agregar_BTN = Locator(By.XPATH, "//a[@class='btn btn-info btn-sm pull-right botonnuevo']")
    orga_nombre_filtro_INP = Locator(By.ID, "OrganismoGDESearchType_nombre")
    orga_buscar_BTN = Locator(By.XPATH, "//button[@class='btn btn-default btn-sm']")
    orga_lapiz_modif_BTN = Locator(By.XPATH, "//i[@class='fa fa-pencil fa-lg']")
    orga_una_pagina_LB = Locator(By.XPATH, "//a[@class='puntero'][contains(text(),'1')]")
    orga_estado_SEL = Locator(By.XPATH,"//span[@class='placeholder']")
    orga_estado_inactivo_OP = Locator(By.XPATH, "//label[contains(text(),'Inactivos')]")
    orga_activar_BTN = Locator(By.XPATH, "//i[@class='fa fa-check fa-lg']")
    orga_aceptar_activo_BTN = Locator(By.XPATH, "//div[@id='activar_org']//button[@class='btn btn-sm btn-primary'][contains(text(),'Aceptar')]")


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
    orga_direc_numero_INP = Locator(By.ID,"OrganismoType_numero")
    orga_direc_piso_INP = Locator(By.ID, "OrganismoType_piso")
    orga_direc_depto_INP = Locator(By.ID, "OrganismoType_deptoOficina")
    orga_direc_cod_postal_INP = Locator(By.ID, "OrganismoType_codigoPostal")
    orga_direc_prov_ba_option = Locator(By.XPATH, "//div[@class='col-md-12 margin-bottom-10']//option[2]")
    orga_direc_prov_SEL = Locator(By.XPATH, "//select[@id='OrganismoType_provincia']")
    orga_direc_partido_INP = Locator(By.ID, "OrganismoType_partido")
    orga_direc_localidad_INP = Locator(By.ID, "OrganismoType_localidad")

    orga_pub0_nombre_INP = Locator(By.ID, "OrganismoType_publicadores_0_nombre")
    orga_pub0_apellido_INP = Locator(By.ID, "OrganismoType_publicadores_0_apellido")
    orga_pub0_cuil_INP = Locator(By.ID, "OrganismoType_publicadores_0_cuil")
    orga_pub0_tel_INP = Locator(By.ID, "OrganismoType_publicadores_0_telefono")
    orga_pub0_mail_INP = Locator(By.ID, "OrganismoType_publicadores_0_mail")
    orga_pub0_usugde_INP = Locator(By.ID, "OrganismoType_publicadores_0_usuarioGDE")
    orga_pub0_activo_CHK = Locator(By.XPATH, "//input[@id='OrganismoType_publicadores_0_activo']")

    orga_pub1_texto_LBL = Locator(By.XPATH, "//a[contains(text(),'Nuevo contacto')]")
    orga_pub1_nombre_INP = Locator(By.ID, "OrganismoType_publicadores_2_nombre")
    orga_pub1_apellido_INP = Locator(By.ID, "OrganismoType_publicadores_2_apellido")
    orga_pub1_cuil_INP = Locator(By.ID, "OrganismoType_publicadores_2_cuil")
    orga_pub1_tel_INP = Locator(By.ID, "OrganismoType_publicadores_2_telefono")
    orga_pub1_mail_INP = Locator(By.ID, "OrganismoType_publicadores_2_mail")
    orga_pub1_usugde_INP = Locator(By.ID, "OrganismoType_publicadores_2_usuarioGDE")
    orga_pub1_activo_CHK = Locator(By.ID, "OrganismoType_publicadores_2_activo")

    orga_pub_agregar_BTN = Locator(By.XPATH, "//body[@class='modal-open']/div[@id='modalneweditorg']/div[@class='modal-dialog modal-lg']/div[@class='modal-content']/div[@id='content-newedit']/form[@id='newEditForm']/div[@id='organismoDependencia']/div[5]/div[1]/div[2]/a[1]")


    orga_fac0_nombre_INP = Locator(By.ID, "OrganismoType_pagadores_0_nombre")
    orga_fac0_apellido_INP = Locator(By.ID, "OrganismoType_pagadores_0_apellido")
    orga_fac0_cuil_INP = Locator(By.ID, "OrganismoType_pagadores_0_cuil")
    orga_fac0_tel_INP = Locator(By.ID, "OrganismoType_pagadores_0_telefono")
    orga_fac0_mail_INP = Locator(By.ID, "OrganismoType_pagadores_0_mail")
    orga_fac0_activo_CHK = Locator(By.ID, "OrganismoType_pagadores_0_activo")
    orga_fac0_agregar_BTN = Locator(By.XPATH, "//a[contains(text(), 'Agregar Facturador')]")

    orga_fac1_nombre_INP = Locator(By.ID, "OrganismoType_pagadores_1_nombre")
    orga_fac1_apellido1_INP = Locator(By.ID, "OrganismoType_pagadores_1_apellido")
    orga_fac1_cuil1_INP = Locator(By.ID, "OrganismoType_pagadores_1_cuil")
    orga_fac1_tel1_INP = Locator(By.ID, "OrganismoType_pagadores_1_telefono")
    orga_fac1_mail1_INP = Locator(By.ID, "OrganismoType_pagadores_1_mail")
    orga_fac1_activo1_CHK = Locator(By.ID, "OrganismoType_pagadores_1_activo")

    dep_agregar_BTN = Locator(By.XPATH, "//a[contains(text(),'Agregar Dependencia')]")
    dep0_nombre_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_nombre")
    dep0_codigo_gde_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_publicadores_1_usuarioGDE")
    dep0_sec_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_sector")
    dep0_buz_gru_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_buzonGrupal")
    dep0_cuit_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_cuit")
    dep0_act_CHK = Locator(By.ID, "OrganismoType_dependenciasPadre_0_activo")
    dep0_direc_calle_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_calle")
    dep0_direc_numero_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_numero")
    dep0_cod_postal_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_codigoPostal")
    dep0_prov_SEL = Locator(By.ID, "OrganismoType_dependenciasPadre_0_provincia")
    dep0_partido_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_partido")
    dep0_localidad_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_localidad")

    dep0_pub_nombre_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_publicadores_1_nombre")
    dep0_pub_apellido_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_publicadores_1_apellido")
    dep0_pub_cuil_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_publicadores_1_cuil")
    dep0_pub_tel_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_publicadores_1_telefono")
    dep0_pub_mail_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_publicadores_1_mail")

    dep0_fac_nombre_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_pagadores_1_nombre")
    dep0_fac_apellido_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_pagadores_1_apellido")
    dep0_fac_cuil_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_pagadores_1_cuil")
    dep0_fac_tel_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_pagadores_1_telefono")
    dep0_fac_mail_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_pagadores_1_mail")

    dep0_sub0_agregar_BTN = Locator(By.XPATH, "//a[contains(text(),'Agregar SubDependencia')]" )
    dep0_sub0_nombre_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_nombre")
    dep0_sub0_cod_gde_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_codigo")
    dep0_sub0_sector_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_sector")
    dep0_sub0_buz_grupal_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_buzonGrupal")
    dep0_sub0_cuit_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_cuit")
    dep0_sub0_calle_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_calle")
    dep0_sub0_num_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_numero")
    dep0_sub0_cod_postal_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_codigoPostal")
    dep0_sub0_prov_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_provincia")
    dep0_sub0_partido_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_partido")
    dep0_sub0_localdia_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_localidad")

    dep0_sub0_agregar_fac_BTN = Locator(By.XPATH, "//div[@id='collapse_OrganismoType_dependenciasPadre_0_subDependencias_0']//div[@class='panel-body']//div[@class='row']//div[@class='col-md-12']//div//a[@class='puntero text-14px'][contains(text(),'Agregar Publicador')]")
    dep0_sub0_agregar_pub_BTN = Locator(By.XPATH, "//div[@id='collapse_OrganismoType_dependenciasPadre_0_subDependencias_0']//div[@class='panel-body']//div[@class='row']//div[@class='col-md-12']//div//a[@class='puntero text-14px'][contains(text(),'Agregar Facturador')]")
    dep0_sub0_pub_nombre_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_publicadores_2_nombre")
    dep0_sub0_pub_apellido_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_publicadores_2_apellido")
    dep0_sub0_pub_cuil_INP = Locator(By.XPATH, "//input[@id='OrganismoType_dependenciasPadre_0_subDependencias_0_publicadores_2_cuil']")
    dep0_sub0_pub_tel_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_publicadores_2_telefono")
    dep0_sub0_pub_mail_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_publicadores_2_mail")
    dep0_sub0_pub_usu_gde_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_publicadores_2_usuarioGDE")

    dep0_sub0_pag_nombre_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_pagadores_2_nombre")
    dep0_sub0_pag_apellido_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_pagadores_2_apellido")
    dep0_sub0_pag_cuil_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_pagadores_2_cuil")
    dep0_sub0_pag_tel_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_pagadores_2_telefono")
    dep0_sub0_pag_mail_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_0_subDependencias_0_pagadores_2_mail")




    dep1_nombre_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_nombre")
    dep1_codigo_gde_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_codigo")
    dep1_sec_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_sector")
    dep1_buz_gru_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_buzonGrupal")
    dep1_cuit_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_cuit")
    dep1_act_CHK = Locator(By.ID, "OrganismoType_dependenciasPadre_2_activo")
    dep1_direc_calle_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_activo")
    dep1_direc_numero_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_numero")
    dep1_cod_postal_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_codigoPostal")
    dep1_prov_SEL = Locator(By.ID, "OrganismoType_dependenciasPadre_2_provincia")
    dep1_partido_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_partido")
    dep1_localidad_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_localidad")



    dep1_pub_nombre_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_publicadores_3_nombre")
    dep1_pub_apellido_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_publicadores_3_apellido")
    dep1_pub_cuil_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_publicadores_3_cuil")
    dep1_pub_tel_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_publicadores_3_telefono")
    dep1_pub_mail_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_publicadores_3_mail")
    dep1_pub_usugde_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_publicadores_3_usuarioGDE")

    dep1_fac_nombre_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_pagadores_3_nombre")
    dep1_fac_apellido_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_pagadores_3_apellido")
    dep1_fac_cuil_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_pagadores_3_cuil")
    dep1_fac_tel_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_pagadores_3_telefono")
    dep1_fac_mail_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_pagadores_3_mail")

    dep1_agregar_sub_BTN = Locator(By.XPATH, "//div[@id='collapse_OrganismoType_dependenciasPadre_2']//div[@class='panel-body']//div[@class='row']//div[@class='col-md-12']//div//a[@class='puntero text-14px'][contains(text(),'Agregar SubDependencia')]")
    dep1_subdep0_pub_nombre_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_publicadores_4_nombre")
    dep1_subdep0_pub_apellido_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_publicadores_4_apellido")
    dep1_subdep0_pub_cuil_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_publicadores_4_cuil")
    dep1_subdep0_pub_tel_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_publicadores_4_telefono")
    dep1_subdep0_pub_mail_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_publicadores_4_mail")
    dep1_subdep0_pub_usugde_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_publicadores_4_usuarioGDE")

    dep1_subdep0_fac_nombre_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_pagadores_4_nombre")
    dep1_subdep0_fac_apellido_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_pagadores_4_apellido")
    dep1_subdep0_fac_cuil_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_pagadores_4_cuil")
    dep1_subdep0_fac_tel_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_pagadores_4_telefono")
    dep1_subdep0_fac_mail_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_pagadores_4_mail")

    dep1_subdep0_nombre_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_nombre")
    dep1_subdep0_codgde_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_codigo")
    dep1_subdep0_sector_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_sector")
    dep1_subdep0_buzgrupal_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_buzonGrupal")
    dep1_subdep0_cuit_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_cuit")
    dep1_subdep0_calle_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_calle")
    dep1_subdep0_numero_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_numero")
    dep1_subdep0_codpostal_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_codigoPostal")
    dep1_subdep0_prov_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_provincia")
    dep1_subdep0_part_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_partido")
    dep1_subdep0_localidad_INP = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_localidad")
    dep1_subdep0_activo_CHK = Locator(By.ID, "OrganismoType_dependenciasPadre_2_subDependencias_0_activo")

    orga_guardar_BTN = Locator(By.XPATH, "//button[@id='guardar']")
    mensaje_MSJ = Locator(By.XPATH, "//div[@class='alert alert-success']")

    orga_pub0_TAB = Locator(By.XPATH,"//div[@id='heading_DependenciaOrganismoGDEType_publicadores_0']//a[@class='collapsed'][contains(text(),'Nuevo contacto')]")
    orga_fac0_TAB = Locator(By.XPATH,"//div[@id='heading_DependenciaOrganismoGDEType_pagadores_0']//a[@class='collapsed'][contains(text(),'Nuevo contacto')]")

    dep_dos_BTN = Locator(By.XPATH, "//a[contains(text(), '{nombre_dependencia_dos}')]")
    dep_dos_sub_uno_BTN = Locator(By.XPATH, "//a[contains(text(), '{nombre_dependencia_dos_sub_uno}')]")

    @staticmethod
    def locator_dep_dos_btn(nombre_dep):
        return Locator(By.XPATH, "//a[contains(text(), '"+nombre_dep+"')]")









