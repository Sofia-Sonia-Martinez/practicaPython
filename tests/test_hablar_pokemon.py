import pytest
from src.interfaces.pokemon_api_interface import PokemonApiInterface 
from src.services.pokemon_service import *
from tests.agents.fake_pokemon_service_api_agent import *
from src.agents.pokemon_service_api_agent import *
from tests.factory.pokemon_factory import *

def test_pokemon_should_be_define():
    pokemon_service = PokemonService(PokemonServiceApiAgent()) 
    assert type(pokemon_service) is PokemonService

def test_pokemon_should_have_method_hablar():
    pokemon_service = PokemonFactory(PokemonServiceApiAgent()).build()
    assert type(pokemon_service.hablar("ditto")) is tuple

def test_pokemon_factory_should_receive_agent_as_parameter_or_implement_fake_agent():
    pokemon_factory = PokemonFactory().build()
    assert type(pokemon_factory) is PokemonService

def test_should_return_valid_json_name_abiliti() :
    agent=PokemonServiceApiAgent()
    book_service=PokemonFactory(agent).build()
    result=book_service.hablar("ditto")
    assert len(result) > 1
