import sys
import os

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "src")
)

from builder import AgenteEmailBuilder, DirectorAgenteEmail
from factory import FabricaPhone, FabricaChat, FabricaEmail
from singleton import ConfiguracionCallCenter
from decorator import AHTBase, ConBono, ConPenalidad
from facade import SistemaCallCenter
from command import ListaAgentes, AgregarAgente

def test_singleton_misma_instancia():
    assert ConfiguracionCallCenter() is ConfiguracionCallCenter()

def test_singleton_estado_compartido():
    ConfiguracionCallCenter().actualizar_version("2.0")
    assert ConfiguracionCallCenter().version == "2.0"

def test_factory_phone():
    assert FabricaPhone().crear_agente().canal() == "Phone"

def test_factory_chat():
    assert FabricaChat().crear_agente().canal() == "Chat"

def test_builder_campos():
    a = (
        AgenteEmailBuilder()
        .agent_id("001")
        .team_manager("Carlos")
        .handle_time(100)
        .build()
    )

    assert a.agent_id == "001"

def test_builder_director():
    a = DirectorAgenteEmail.crear_nuevo_agente(
        AgenteEmailBuilder(),
        "002",
        "Laura"
    )

    assert a.agent_id == "002"

def test_decorator_bono():
    assert ConBono(AHTBase(20)).valor() == 25

def test_decorator_penalidad():
    assert ConPenalidad(AHTBase(20)).valor() == 18

def test_facade_instancia():
    s = SistemaCallCenter()
    assert s.phone is not None

def test_facade_modulos():
    s = SistemaCallCenter()
    assert s.chat.listar() == "Agentes Chat"

def test_command_agregar():
    lista = ListaAgentes()

    AgregarAgente(lista, "Juan").ejecutar()

    assert "Juan" in lista.listar()

def test_command_eliminar():
    lista = ListaAgentes()

    lista.agregar("Juan")
    lista.eliminar("Juan")

    assert "Juan" not in lista.listar()