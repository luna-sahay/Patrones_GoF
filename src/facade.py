class ModuloPhone:

    def listar(self):
        return "Agentes Phone"


class ModuloChat:

    def listar(self):
        return "Agentes Chat"


class ModuloEmail:

    def listar(self):
        return "Agentes Email"


class SistemaCallCenter:

    def __init__(self):

        self.phone = ModuloPhone()
        self.chat = ModuloChat()
        self.email = ModuloEmail()

    def mostrar_resumen(self):

        print(self.phone.listar())
        print(self.chat.listar())
        print(self.email.listar())