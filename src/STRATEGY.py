from abc import ABC, abstractmethod


class EstrategiaAHT(ABC):

    @abstractmethod
    def calcular(self, handle_time, transacciones):
        pass


class AHTPhone(EstrategiaAHT):

    def calcular(self, handle_time, transacciones):

        if transacciones == 0:
            return 0

        return round(handle_time / transacciones, 2)


class AHTEmail(EstrategiaAHT):

    def calcular(self, handle_time, transacciones):

        if transacciones == 0:
            return 0

        return round(handle_time / transacciones, 2)


class CalculadoraAHT:

    def __init__(self, estrategia):
        self._estrategia = estrategia

    def calcular(self, handle_time, transacciones):
        return self._estrategia.calcular(handle_time, transacciones)