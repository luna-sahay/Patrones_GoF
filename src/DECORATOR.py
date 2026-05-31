from abc import ABC, abstractmethod


class Indicador(ABC):

    @abstractmethod
    def valor(self):
        pass


class AHTBase(Indicador):

    def __init__(self, aht):
        self._aht = aht

    def valor(self):
        return self._aht


class DecoradorIndicador(Indicador):

    def __init__(self, indicador):
        self._indicador = indicador

    def valor(self):
        return self._indicador.valor()


class ConBono(DecoradorIndicador):

    def valor(self):
        return self._indicador.valor() + 5


class ConPenalidad(DecoradorIndicador):

    def valor(self):
        return self._indicador.valor() - 2