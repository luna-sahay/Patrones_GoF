class ConfiguracionCallCenter:

    _instancia = None

    def __new__(cls):

        if cls._instancia is None:

            cls._instancia = super().__new__(cls)
            cls._instancia.nombre = "Call Center KPI"
            cls._instancia.version = "1.0"

        return cls._instancia

    def actualizar_version(self, version):

        self.version = version