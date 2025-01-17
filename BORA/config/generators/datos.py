import os
import json
from config.data.enums import *
from config.data.utils import Utils
import random


utils = Utils()
fecha_a_usar = utils.fecha_de_hoy_guion()
fecha_a_usar_invertida = utils.fecha_hoy_guion_invertida()
fecha_pub_erronea = '2020-10-14'
#

"""Archivo de configuración para un Proceso de Compras sin modalidad."""

__data = {
    "ambiente":
        {
            "url": "http://10.2.1.112:8081",
            "urlAPI": "http://10.2.1.112:8082",
            "ordenFirmante": ["ALBERTOANGELFERNANDEZ", "SCAFIERO"]
        },
    "usuarios":
        {
            "administrador": ["admin"],
            "contrasena": "1234"
        },
    "aviso":
        {
            "seccion": "26",
            "rubro": "Acta",
            "tipoAviso": "Acta",
            "diasPublicar": 1,
            "formaPago": "Pospago",
            "archivo": "C:\\Users\\vruiz\\Downloads\\OA_01-11-2018.pdf",
            "dia": utils.fecha_de_hoy(),
            "origen": "GDE",
            "orga": "Organismo100720191447",
            "fechaFirma": utils.fecha_de_hoy()
        },
    "organismo":
        {
            "nombre_orga": "Organismo"+utils.fecha_de_hoy_hora(),
            "sector_orga": "TestSecOrga",
            "buz_gru_orga": "TestBuzOrga",
            "sistemas_orga": "2,5",
            "activo_orga": "0",
            "pub0_activo": 0,
            "calle_orga": "Miller",
            "numero_orga": "2552",
            "cod_postal_orga": "1431",
            "provincia_orga": "Buenos Aires",
            "pub0_nombre_orga": "TestNombrePubOrgaCero",
            "pub0_apellido_orga": "TestApellidoPubOrgaCero",
            "pub0_tel_orga": 23484848,
            "pub0_mail_orga": "test@cys.com.ar",
            "pub0_usuario_gde_orga": "test"+utils.fecha_de_hoy_hora(),
            "pub1_nombre_orga": "TestNombrePubOrgaUno",
            "pub1_apellido_orga": "TestNombrePubOrgaUno",
            "pub1_tel_orga": 5456456,
            "pub1_mail_orga": "Test2@cys.com.ar",
            "pub_1_usuario_gde_orga":  "test1"+utils.fecha_de_hoy_hora(),
            "fac0_nombre_orga": "TestNombreFacOrgaCero",
            "fac0_apellido_orga": "TestApellidoFacOrgaCero",
            "fac0_tel_orga": "5454545",
            "fac0_mail_orga": "vruiz@cys.com.ar",
            "fac1_nombre_orga": "TestNombreFacOrgaUno",
            "fac1_apellido_orga": "TestApellidoFacOrgaUno",
            "fac1_tel_orga": 5454545,
            "fac1_mail_orga": "vruiz@cys.com.ar",
            "partido_orga": "testPartidoOrga",
            "localidad_orga": "testLocalidadOrga",
            "dep0_nombre": "DependenciaCero"+utils.fecha_de_hoy_hora(),
            "dep0_codigo_gde": "test9"+utils.fecha_de_hoy_hora(),
            "dep0_sector": "Test",
            "dep0_buzon_grupal": "Test",
            "dep0_calle": "Test",
            "dep0_numero": "546454",
            "dep0_cod_postal": "1456",
            "dep0_provincia": "Buenos Aires",
            "dep0_partido": "Buenos aires",
            "dep0_localidad": "CABA",
            "dep0_pub0_nombre": "Test",
            "dep0_pub0_apellido": "test",
            "dep0_pub0_tel": 564654,
            "dep0_pub0_mail": "test@cys.com.ar",
            "dep0_pub0_usu_gde": "pub0Dep0"+utils.fecha_de_hoy_hora(),
            "dep0_fac0_nombre": "TestNombreFacDepCero",
            "dep0_fac0_apellido": "TestApellidoFacDepCero",
            "dep0_fac0_tel": 464564,
            "dep0_fac0_mail": "vruiz@cys.com.ar",
            "dep0_sub0_nombre": "Dep0Sub0"+utils.fecha_de_hoy_hora(),
            "dep0_sub0_codgde":"Test1411"+utils.fecha_de_hoy_hora(),
            "dep0_sub0_sector": "Test1422"+utils.fecha_de_hoy_hora(),
            "dep0_sub0_buzon":"test1423"+utils.fecha_de_hoy_hora(),
            "dep1_sub0_nombre": "SubdependenciaUNO"+utils.fecha_de_hoy_hora(),
            "dep1_sub0_codigo_gde": "test654654"+utils.fecha_de_hoy_hora(),
            "dep1_sub0_sector": "Test",
            "dep1_sub0_buzon_grupal": "Test",
            "dep1_sub0_calle": "Test",
            "dep1_sub0_numero": "546454",
            "dep1_sub0_cod_postal": "1456",
            "dep1_sub0provincia": "Buenos Aires",
            "dep1_sub0_pub0_nombre": "Test",
            "dep1_sub0_pub0_apellido": "test",
            "dep1_sub0_pub0_tel": 564654,
            "dep1_sub0_pub0_mail": "test@cys.com.ar",
            "dep1_sub0_pub0_usu_gde": "test3"+utils.fecha_de_hoy_hora(),
            "dep1_sub0_fac0_nombre": "TestNombreFacSubDepCero",
            "dep1_sub0_fac0_apellido": "TestApellidoSubFacDepCero",
            "dep1_sub0_fac0_tel": 464564,
            "dep1_sub0_fac0_mail": "vruiz@cys.com.ar",
            "dep1_nombre": "DependenciaUNO"+utils.fecha_de_hoy_hora(),
            "dep1_codigo_gde": "test653145"+utils.fecha_de_hoy_hora(),
            "dep1_sector": "Test",
            "dep1_buzon_grupal": "Test",
            "dep1_calle": "Test",
            "dep1_numero": "546454",
            "dep1_cod_postal": "1456",
            "dep1_provincia": "Buenos Aires",
            "dep1_partido": "Test",
            "dep1_localidad": "Test",
            "dep1_pub0_nombre": "Test",
            "dep1_pub0_apellido": "test",
            "dep1_pub0_tel": 564654,
            "dep1_pub0_mail": "test@cys.com.ar",
            "dep1_pub0_usu_gde": "dep1Pub0" + utils.fecha_de_hoy_hora(),
            "dep1_fac0_nombre": "TestNombreFacDepCero",
            "dep1_fac0_apellido": "TestApellidoFacDepCero",
            "dep1_fac0_tel": 464564,
            "dep1_fac0_mail": "vruiz@cys.com.ar"
        },
    "judicial":{
        "cantDias":"1",
        "tipoDeAviso":"concursos",
        "titulo":"Citacion"+utils.fecha_de_hoy_hora(),
        "organismo":23454844444,
        "codigoModalidadPago":"post-pago",
        "nroNorma":"1",
        "anio":"2019",
        "textoAPublicar":"TEXTO DEL AVISO A PUBLICAR",
        "seccion":"segunda-seccion",
        "EE":"EX-2018-00000002",
        "fechaPublicacion": fecha_a_usar,
        "rubro":"edictos-judiciales",
        "sintesis":"Datos de la sintesis",
        "usuarioOrigen":"PBORA",
        "observacionesGenerales":"OBSERVACIONES laralala",
        "observacionesAviso":"OBSERVACIONES ",
        "fechaFirma":"2019-05-22",
        "nroExpedienteJudicial":"test",
        "anioExpedienteJudicial":"45454",
        "sistemaOrigen": "sistema-judiciales",
        "autos": "test",
        "subtipo": "2",
        "fechaLimite": utils.fecha_de_hoy(),
    },
    "decreto":{
            "cantDias": "1",
            "sistemaOrigen": "sistema-presidencia",
            "tipoDeAviso": "decreto",
            "titulo": "decreto"+utils.fecha_de_hoy_hora(),
            "organismo": "test654654"+utils.fecha_de_hoy_hora(),
            "codigoModalidadPago": "post-pago",
            "anio":"2019",
            "nroNorma": "1",
            "textoAPublicar": "decreto"+utils.fecha_de_hoy_hora(),
            "seccion": "primera-seccion",
            "EE": "EX-2018-00000002",
            "fechaPublicacion": fecha_a_usar,
            "firmantes":"ALBERTOANGELFERNANDEZ-SCAFIERO-"+str(utils.generate_word()),
            "rubro": "decreto",
            "sintesis":"Datos de la sintesis",
            "usuarioOrigen": "PBORA",
            "observacionesGenerales": "OBSERVACIONES laralala",
            "observacionesAviso": "OBSERVACIONES ",
            "fechaFirma": "2019-05-22"
        },
    "decretoErroneo":{
        "fechaPublicacion": fecha_pub_erronea,
        "cantDias": "4",
        "fechaFirma": "22-05-2019"
    },
    "decreto api": {
        "cantDias": "1",
        "sistemaOrigen": "sistema-presidencia",
        "tipoDeAviso": "decreto",
        "titulo": "Aviso generado por API",
        "organismo": "Organismo"+utils.fecha_de_hoy_hora(),
        "codigoModalidadPago": "post-pago",
        "anio": "2019",
        "nroNorma": "1",
        "textoAPublicar": "Decreto "+utils.fecha_de_hoy_hora(),
        "seccion": "primera-seccion",
        "EE": "EX-2018-00000002",
        "fechaPublicacion": fecha_a_usar,
        "firmantes": "GMichetti-MPENA-MMACRI",
        "nombresAnexos": "Test1.pdf,test2.pdf",
        "rubro": "decreto",
        "sintesis": "Datos de la sintesis",
        "usuarioOrigen": "PBORA",
        "observacionesGenerales": "OBSERVACIONES laralala",
        "observacionesAviso": "OBSERVACIONES ",
        "fechaFirma": "2019-05-22"
    },
    "ley": {
        "cantDias": "1",
        "sistemaOrigen": "sistema-presidencia",
        "tipoDeAviso": "ley",
        "organismo": "Organismo"+utils.fecha_de_hoy_hora(),
        "codigoModalidadPago": "post-pago",
        "anio": "2019",
        "nroNorma": "1",
        "textoAPublicar": "ley "+utils.fecha_de_hoy_hora(),
        "seccion": "primera-seccion",
        "EE": "EX-2018-00000002",
        "fechaPublicacion": fecha_a_usar,
        "firmantes": "GMichetti-MPENA-MMACRI-asdasd",
        "rubro": "ley",
        "sintesis": "Datos de la sintesis",
        "usuarioOrigen": "PBORA",
        "observacionesGenerales": "OBSERVACIONES laralala",
        "observacionesAviso": "OBSERVACIONES ",
        "fechaFirma": "2019-05-22"
    },
    "leyErroneo":{
        "fechaPublicacion": fecha_pub_erronea,
        "cantDias": "4",
        "fechaFirma": "22-05-2019"
    },
    "orgaJudicial":{
        "nombre_orga":"Organismo_judicial_"+utils.fecha_de_hoy_hora(),
        "calle_orga":"TestCalle",
        "num_orga":"454545454",
        "cod_postal_orga":"54545",
        "partido_orga":"TestPartido",
        "localidad_orga":"TestLocalidad",
        "nombre_secre": "secre"+utils.fecha_de_hoy_hora(),
        "calle_secre":"testCalle",
        "num_secre":"56454",
        "cod_postal_secre":"454",
        "prov_op": "146",
        "partido_sec": "TestPartido",
        "localidad_sec":"TestLocalidad",
        "nombre_rep": "testNombre",
        "apellido_rep": "TestApe",
        "telefono_rep": "55454",
        "mail_rep":"vruiz@cys.com.ar",
        "usuario_rep":"testusu"+utils.fecha_de_hoy_hora(),
        "cargo_rep": "test"
    },
    "sucesion":{
        "cantDias": "1",
        "tipoDeAviso": "sucesiones",
        "titulo": "Sucesion"+ utils.fecha_de_hoy_hora(),
        "organismo": "23251570064",
        "codigoModalidadPago": "post-pago",
        "nroNorma": "1",
        "anio": "2019",
        "textoAPublicar": "Sucesion "+utils.fecha_de_hoy_hora(),
        "seccion": "segunda-seccion",
        "EE": "EX-2018-00"+str(random.randint(1,6000)),
        "fechaPublicacion": fecha_a_usar,
        "rubro": "edictos-judiciales",
        "sintesis": "Datos de la sintesis",
        "usuarioOrigen": "PBORA",
        "observacionesGenerales": "OBSERVACIONES laralala",
        "observacionesAviso": "OBSERVACIONES ",
        "fechaFirma": "2020-04-12",
        "nroExpedienteJudicial": "test",
        "anioExpedienteJudicial": "45454",
        "sistemaOrigen": "sistema-judiciales",
        "autos": "test",
        "subtipo": "2",
        "fechaLimite": "22-10-2019",
        "causante":"test"

    },
    "sucesionErroneo":{
        "cantDias":"4",

    },
    "acta": {
        "cantDias": "1",
        "sistemaOrigen": "sistema-gde",
        "tipoDeAviso": "acta",
        "organismo":"test654654"+utils.fecha_de_hoy_hora(),
        "codigoModalidadPago": "post-pago",
        "anio": "2019",
        "nroNorma": "1",
        "textoAPublicar": "Acta "+utils.fecha_de_hoy_hora(),
        "seccion": "primera-seccion",
        "EE": "EX-2018-"+utils.fecha_de_hoy_hora(),
        "fechaPublicacion": fecha_a_usar,
        "firmantes": "GMichetti-MPENA-MMACRI-asdasd",
        "rubro": "acta",
        "sintesis": "Datos de la sintesis",
        "usuarioOrigen":  "pub0Dep0"+utils.fecha_de_hoy_hora(),
        "observacionesGenerales": "OBSERVACIONES laralala",
        "observacionesAviso": "OBSERVACIONES ",
        "fechaFirma": "2019-05-22"
    },
    "actaErroneo":{
        "fechaPublicacion": fecha_a_usar,
        "cantDias": "4",
        "fechaFirma": "22-05-2019"
    },
    "actaDos":{
        "cantDias": "1",
        "sistemaOrigen": "sistema-gde",
        "tipoDeAviso": "acta",
        "titulo": "",
        "organismo":"SLYT",
        "codigoModalidadPago": "post-pago",
        "anio": "2019",
        "nroNorma": "1",
        "textoAPublicar": "test",
        "seccion": "primera-seccion",
        "EE": "EX-2018-"+utils.fecha_de_hoy_hora(),
        "fechaPublicacion": "2020-07-31",
        "firmantes": "GMichetti-MPENA-MMACRI-asdasd",
        "rubro": "acta",
        "sintesis": "Datos de la sintesis",
        "usuarioOrigen":  "PBORA",
        "observacionesGenerales": "OBSERVACIONES laralala",
        "observacionesAviso": "OBSERVACIONES ",
        "fechaFirma": "2019-05-22"
    },
    "actaDosErroneo": {
        "fechaPublicacion": "31-07-2020",
        "cantDias": "4",
        "fechaFirma": "22-05-2019"
    },
    "adjudicacion":{
        "EE": "EX-2018-00"+str(random.randint(1,6000)),
        "seccion": "tercera-seccion",
        "rubro": "adjudicacion",
        "tipoDeAviso": "adjudicacion",
        "fechaPublicacion": fecha_a_usar,
        "cantDias": 1,
        "periodicidad": "diaria",
        "textoAPublicar": "TEXTO",
        "organismo": "SLYT",
        "nombresAnexos": "",
        "avisoRelacionadoId": "",
        "nroContratacion": "123",
        "anioContratacion": "2019",
        "observacionesAviso": "OBSERVACIONES",
        "usuarioOrigen": "COMPRAR",
        "sistemaOrigen": "sistema-comprar"
    },
    "adjudicacionErroneo":{
        "fechaPublicacion": fecha_pub_erronea,
        "cantDias": "7",
    },
    "oa_sup":{
        "id_avisos": "",
        "textos": "",
        "nombre": "",
        "fecha": fecha_a_usar_invertida,
        "nro_edicion": utils.fecha_de_hoy_hora()
    }

}


try:
    with open(os.path.join(os.path.dirname(__file__), r'JSONS\datos.json'), 'w', encoding='utf-8') as file:
        json.dump(__data, file, indent=4, ensure_ascii=False)
        print("El archivo 'sin_modalidad.json' generado correctamente.")
except Exception as e:
    print("Error al intentar ejectuar 'datos.py':", e)
