from abc import ABC, abstractmethod


class ListaAgentes:

    def __init__(self):
        self._agentes = []

    def agregar(self, agente):
        self._agentes.append(agente)

    def eliminar(self, agente):

        if agente in self._agentes:
            self._agentes.remove(agente)

    def listar(self):
        return self._agentes


class Comando(ABC):

    @abstractmethod
    def ejecutar(self):
        pass


class AgregarAgente(Comando):

    def __init__(self, lista, agente):

        self._lista = lista
        self._agente = agente

    def ejecutar(self):

        self._lista.agregar(self._agente)


class EliminarAgente(Comando):

    def __init__(self, lista, agente):

        self._lista = lista
        self._agente = agente

    def ejecutar(self):

        self._lista.eliminar(self._agente)


class GestorComandos:

    def ejecutar(self, comando):

        comando.ejecutar()