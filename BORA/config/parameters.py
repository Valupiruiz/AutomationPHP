import json
import os


class Parameters:
    __json_file = None
    __filename = None

    @classmethod
    def execute_file(cls, filename):
        """Si filename coincide con algún generador, lo ejecuta."""
        try:
            cls.__json_file = None
            file = open(os.path.join(os.path.dirname(__file__), "generators\{}.py".format(filename)))
            exec(file.read())
            file.close()
            cls.__filename = filename
            print("El archivo '{}.json' cargado correctamente.".format(os.path.splitext(filename)[0]))
        except FileExistsError:
            print("No se encontró el archivo {} en 'configs/generators/'".format(filename))

    @classmethod
    def __load_json(cls, filename):
        """Carga la variable si está vacía y la devuelve, sino sólo la devuelve."""
        if cls.__json_file is None:
            with open(os.path.join(os.path.dirname(__file__), 'JSONS\{}.json'.format(filename)),
                      encoding='utf-8') as file:
                cls.__json_file = json.load(file)
        return cls.__json_file

    @classmethod
    def save_json(cls,data):
        try:
            with open(os.path.join(os.path.dirname(__file__), r'JSONS\datos.json'), 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                print("El archivo 'sin_modalidad.json' generado correctamente.")
        except Exception as e:
            print("Error al intentar guardar en 'datos.json':", e)

    @classmethod
    def get_data(cls):
        data = Parameters.__load_json(cls.__filename)
        return data


    @classmethod
    def get_ambiente(cls):
        """Devuelve los parametros de ambiente."""
        data = Parameters.__load_json(cls.__filename)
        return data['ambiente']

    @classmethod
    def set_usu_pub(cls,usuario):
        data = Parameters.__load_json(cls.__filename)
        data['acta']['usuarioOrigen'] = usuario
        cls.save_json(data)


    @classmethod
    def set_cuit_sec(cls,cuit):
        data = Parameters.__load_json(cls.__filename)
        data['sucesion']['organismo'] = cuit
        cls.save_json(data)

    @classmethod
    def set_aviso_oa_sup(cls, nro, texto):
        data = Parameters.__load_json(cls.__filename)
        if cls.get_nro_oa_sup() == "" and cls.get_texto_oa_sup() == "":
            coma = ''
        else:
            coma = ','
        data['oa_sup']['id_avisos'] = cls.get_nro_oa_sup() + coma + str(nro)
        data['oa_sup']['textos'] = cls.get_texto_oa_sup() + coma + str(texto)
        cls.save_json(data)

    @classmethod
    def set_nombre_oa_sup(cls, nombre):
        data = Parameters.__load_json(cls.__filename)
        data['oa_sup']['nombre'] = nombre
        cls.save_json(data)


    @classmethod
    def get_nro_oa_sup(cls):
        data = Parameters.__load_json(cls.__filename)
        return data['oa_sup']['id_avisos']

    @classmethod
    def get_texto_oa_sup(cls):
        data = Parameters.__load_json(cls.__filename)
        return data['oa_sup']['textos']


    @classmethod
    def get_usuarios(cls):
        """Devuelve los parametros de usuarios."""
        data = Parameters.__load_json(cls.__filename)
        return data['usuarios']

    @classmethod
    def get_anexos(cls):
        """Devuelve los parametros de anexos."""
        data = Parameters.__load_json(cls.__filename)
        return data['anexos']


    @classmethod
    def get_aviso(cls):
        "Devuelve los parametros de un aviso de acta"
        data = Parameters.__load_json(cls.__filename)
        return data['aviso']

    @classmethod
    def get_organismo(cls):
        "Devuelve los parametros de un orgasnismo "
        data = Parameters.__load_json(cls.__filename)
        return data['organismo']

    @classmethod
    def get_organismo_judicial(cls):
        data = Parameters.__load_json(cls.__filename)
        return data['orgaJudicial']

    @classmethod
    def get_aviso_api(cls, tipo):
        "devuelve los parametros de un aviso en api"
        data = Parameters.__load_json(cls.__filename)
        return data[tipo]

    @classmethod
    def get_documento(cls):
        data = Parameters.__load_json(cls.__filename)
        return data['documento']
