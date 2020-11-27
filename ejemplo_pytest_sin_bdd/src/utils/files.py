import json

from filelock import FileLock


def grabar(archivo, valores):
    with open(archivo, "r+") as jsonFile:
        data = json.load(jsonFile)
        for k, v in valores.items():
            print(f"{k}:{data[k]} -> {v}")
            data[k] = v
        jsonFile.seek(0)
        json.dump(data, jsonFile, indent=4)
        jsonFile.truncate()


def leer(archivo, clave):
    with open(archivo, "r") as jsonFile:
        data = json.load(jsonFile)
    return data[clave]


def get_codigo(archivo, key):
    with FileLock(archivo + ".lock"):
        codigo = leer(archivo, key)
        grabar(archivo, {key: codigo + 1})
        return codigo


# def generar_enviorement_allure(context):
#     constructor = namedtuple('parametro', 'clave valor')
#     lista = []
#     carpeta_reportes = cfgRutas.root_proyecto + r"\{0}".format(context.config.outfiles[0])
#     archivo_environment = carpeta_reportes + r"\environment.properties"
#
#     if not exists(carpeta_reportes):  # si no existe el path, no genero el properties
#         return
#
#     def agregar_parametro(clave, valor):
#         lista.append(constructor(clave, valor))
#
#     # browser
#     # Navegador
#     agregar_parametro('Navegador', context.driver.capabilities['browserName'])
#
#     # Version
#     stripped_ver = context.driver.capabilities['chrome']['chromedriverVersion'].index('(')
#     agregar_parametro('Version', context.driver.capabilities['chrome']['chromedriverVersion'][:stripped_ver])
#
#     # headless
#     agregar_parametro('Headless', context.headless)
#
#     # detach
#     agregar_parametro('Detach', context.detach)
#
#     # Test
#     # ambiente
#     agregar_parametro('Ambiente', context.ambiente)
#
#     with open(archivo_environment, 'wt') as f:
#         for parametro in lista:
#             linea = f"{parametro.clave}={parametro.valor}\n"
#             f.write(linea)
