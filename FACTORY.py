from abc import ABC, abstractmethod

class Agente(ABC):

    @abstractmethod
    def canal(self):
        pass


class AgentePhone(Agente):

    def canal(self):
        return "Phone"


class AgenteChat(Agente):

    def canal(self):
        return "Chat"


class AgenteEmail(Agente):

    def canal(self):
        return "Email"


class FabricaAgente(ABC):

    @abstractmethod
    def crear_agente(self):
        pass


class FabricaPhone(FabricaAgente):

    def crear_agente(self):
        return AgentePhone()


class FabricaChat(FabricaAgente):

    def crear_agente(self):
        return AgenteChat()


class FabricaEmail(FabricaAgente):

    def crear_agente(self):
        return AgenteEmail()