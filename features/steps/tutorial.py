from behave import given, when, then
from src.services.pokemon_service import PokemonService
from src.agents.pokemon_service_api_agent import PokemonServiceApiAgent
from src.interfaces.pokemon_api_interface import PokemonApiInterface
from tests.factory.pokemon_factory import *

@given(u'el "pokemon" fue elegido')
def step_impl(context):
    context.service = PokemonFactory(PokemonServiceApiAgent()).build()

@when(u'elijo el modo {hablar}')
def step_impl(context, hablar):
    context.result = context.service.hablar("ditto")

@then(u'el sistema me dice su nombre y habilidades')
def step_impl(context):
    assert isinstance(context.result, tuple)
