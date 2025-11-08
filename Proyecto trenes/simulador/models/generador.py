class Generador:
    def __init__(
        self,
        poblacion: int,
        seed=123,
        fecha_inicial: dt.datetime = dt.datetime(2025, 1, 1),
        hora_apertura: dt.time = dt.time(7, 0),
        hora_cierre: dt.time = dt.time(20, 0),
    ):
        ...
        ...
        self.poblacion = poblacion
        self.seed = seed
        self.current_datetime: dt.datetime = fecha_inicial
        self.rdm = random.Random(seed)

    def generar_clientes(self, minutos: int):
        size = int(minutos * CPM)
        return [Cliente(dt.datetime.now())] * size

