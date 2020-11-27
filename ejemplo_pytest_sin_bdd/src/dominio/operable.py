class TiposOperable:
    Caja = "Caja"
    Boveda = "Bóveda"


class EstadosOperable:
    ABIERTA = 1
    CERRADA_TOTALMENTE = 3
    CERRADA_PARCIALMENTE = 4
    BLOQUEADA = 2


class Operable:

    def __init__(self, codigo, monedas):
        # todo: sacar esto, por el momento es mas facil y rapido agregarlo como atributo
        #  que agregar la password como parametro de apertura
        self.id = None
        self.password = "12345678"
        self._operaciones = []
        self.codigo = codigo
        self._monedas = set(monedas)
        self._envia_giros = True
        self._recibe_giros = True
        # Al crear, siempre tienen todas las monedas permitidas
        self._monedas_envio_giros = {moneda: True for moneda in monedas}
        self._monedas_recibo_giros = {moneda: True for moneda in monedas}

    def agregar_operacion(self, operacion):
        self._operaciones.append(operacion)

    @property
    def monedas_permitidas(self):
        # Las monedas permitidas son aquellas que estan habilitadas en el envio y recibo de giros
        monedas_recibo_giros = self.monedas_recibo_giros
        return {moneda for moneda, estado in self.monedas_envio_giros.items()
                if estado and monedas_recibo_giros[moneda]}

    @property
    def monedas_envio_giros(self):
        return self._monedas_envio_giros

    @property
    def monedas_recibo_giros(self):
        return self._monedas_recibo_giros

    @property
    def envia_giros(self):
        return self._envia_giros

    @property
    def recibe_giros(self):
        return self._recibe_giros

    @property
    def monedas(self):
        return self._monedas

    def balance(self):
        balance = {moneda: 0 for moneda in self.monedas_permitidas}
        for operacion in self._operaciones:
            for moneda, monto in operacion.relative_value(self).items():
                balance[moneda] += monto
        return balance

    def monedas_en_uso(self):
        return [moneda for moneda, monto in self.balance().items() if monto > 0]


class Caja(Operable):

    def __init__(self, codigo, monedas):
        super().__init__(codigo, monedas)
        self.activa = True
        self.tipo = TiposOperable.Caja

    @Operable.envia_giros.setter
    def envia_giros(self, val):
        if not val:  # cuando se deshabilitan los giros, se desactivan las monedas permitidas
            self._monedas_envio_giros = {moneda: False for moneda in self._monedas_envio_giros}
        self._envia_giros = val

    @Operable.recibe_giros.setter
    def recibe_giros(self, val):
        if not val:
            self._monedas_recibo_giros = {moneda: False for moneda in self._monedas_recibo_giros}
        self._recibe_giros = val

    def habilitar_moneda_giro(self, tipo_giro, moneda):
        # todo: hacer mas lindo
        if moneda not in self._monedas:
            raise Exception("No se puede agregar a las monedas permitidas ya que no es una moneda de la caja")

        if tipo_giro == "Recibe":
            self._monedas_recibo_giros[moneda] = True
        elif tipo_giro == "Envia":
            self._monedas_envio_giros[moneda] = True
        elif tipo_giro == "Ambos":
            self._monedas_recibo_giros[moneda] = True
            self._monedas_envio_giros[moneda] = True

    def deshabilitar_moneda_giro(self, tipo_giro, moneda):

        if tipo_giro == "Recibe":
            self._monedas_recibo_giros[moneda] = False
        elif tipo_giro == "Envia":
            self._monedas_envio_giros[moneda] = False
        elif tipo_giro == "Ambos":
            self._monedas_envio_giros[moneda] = False
            self._monedas_recibo_giros[moneda] = False
        else:
            raise Exception("No se ingreso un tipo de giro reconocible")

    def desactivar(self):
        self.activa = False

    def activar(self):
        self.activa = True


class Boveda(Operable):

    def __init__(self, codigo, monedas):
        super().__init__(codigo, monedas)
        self.tipo = TiposOperable.Boveda
        # esto es feo pero es mas facil suponer
        # que siempre es 1, ya que la base se seedea asi, a fetchearlo
        self.id = 1


class Moneda:

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self._id = None
        self.estado = True

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
