from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class MateriasLocators:
    MATERIAS_SEL = Locator(By.ID, "selectMateria")
    MATERIA_LBL = Locator(By.XPATH, "//span[@class='label label-primary label-asginatura']")
    SOLAPA_BTN = Locator(By.XPATH, "//a[contains(text(),'{solapa}')]")
    EDITAR_EV_TEMP = Locator(By.XPATH, "//td[contains(.,'{nom_evaluacion}')]/ancestor::tr//i[@class='fa fa-edit']")
    CARGANDO_IMG = Locator(By.XPATH, "//div[@id='loaderEvaluaciones']//div//div//img")
    PLANILLA_EV_BTN = Locator(By.XPATH, "//button[@class='btn btn-primary btn-xs pull-right']")
    PANTALLA_EV_BTN = Locator(By.XPATH, "//a[@id='salidaPlanillaHTML']")
    EXCLUIR_EV_TEMP = Locator(By.XPATH, "//td[contains(.,'{evaluacion}')]/ancestor::tr//label")
    CALIFICAR_NOTA_EV_TEMP_INP = Locator(By.XPATH, "//td[contains(text(),'{alumno}')]/ancestor::tr//td[3]/input")
    AUSENTE_EV_TEMP_BTN = Locator(By.XPATH, "//td[contains(text(),'{alumno}')]/ancestor::tr//td[2]/input")
    VERIFICAR_COLUMNA_TEMP = Locator(
        By.XPATH,
        "//html[1]/body[1]/div[1]/div[2]/table[1]/thead[1]/tr[2]/th[contains(@title, 'Evaluación: {evaluacion}')]"
    )


class EvaluacionLocators:
    MANZANA_CARGANDO = Locator(By.XPATH, "//div[@id='modalEdicionEvaluacion']//div//div//div[@class='modal-body']//div//img")
    CARGANDO_LISTADO_EVALUACIONES = Locator(By.XPATH, "//div[@id='listadoEvaluaciones']//div//img")
    MODAL_EVALUACION = Locator(By.ID, "modalEdicionEvaluacion")
    NUEVA_EV_BTN = Locator(By.XPATH, "//a[@title='Nueva Evaluación']")
    NOMBRE_EV_INP = Locator(By.ID, "nombre")
    FECHA_EV_INP = Locator(By.ID, "fechaEvaluacion")
    PONDERACION_BTN = Locator(By.XPATH, "//div[@class='col-md-2']//div[@class='toggle btn btn-success']")
    PONDERACION_AUTO_BTN = Locator(By.XPATH, "//label[contains(text(),'Automático')]")
    PONDERACION_MANUAL_BTN = Locator(By.XPATH, "//label[contains(text(),'Manual')]")
    VALORACION_PONDERACION_TXT = Locator(By.ID, "valoracion")
    GUARDAR_EV_BTN = Locator(By.ID, "guardar")
    TIPO_EVALUACION_SEL = Locator(By.ID, "tipoEvaluacion")
    PLANILLA_EVALUACIONES_BTN = Locator(By.XPATH, "//button[@class='btn btn-primary btn-xs pull-right']")
    PANTALLA_EVALUACIONES = Locator(By.ID, "salidaPlanillaHTML")
    CERRAR_VENTANA_PLANILLA_BTN = Locator(By.XPATH, "//div[@id='modalPlanillaVuelco']//span[contains(text(),'×')]")




