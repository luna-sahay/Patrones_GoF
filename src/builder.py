class AgenteEmail:

    def __init__(self):
        self.agent_id = None
        self.team_manager = None
        self.handle_time = None
        self.inbound_tx = None
        self.acw = None

    def __str__(self):
        return f"AgenteEmail[{self.agent_id} | {self.team_manager}]"


class AgenteEmailBuilder:

    def __init__(self):
        self._a = AgenteEmail()

    def agent_id(self, v):
        self._a.agent_id = v
        return self

    def team_manager(self, v):
        self._a.team_manager = v
        return self

    def handle_time(self, v):
        self._a.handle_time = v
        return self

    def inbound_tx(self, v):
        self._a.inbound_tx = v
        return self

    def acw(self, v):
        self._a.acw = v
        return self

    def build(self):
        if not self._a.agent_id:
            raise ValueError("ID obligatorio")
        return self._a


class DirectorAgenteEmail:
    
    def crear_nuevo_agente(self, builder, agent_id, manager):
        builder.agent_id(agent_id)
        builder.team_manager(manager)
        builder.handle_time(0)
        builder.inbound_tx(0)
        builder.acw(0)
        return builder.build()