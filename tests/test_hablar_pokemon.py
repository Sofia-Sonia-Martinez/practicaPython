import pytest
from requests.models import Response
from src.interfaces.pokemon_api_interface import PokemonApiInterface 
from src.services.pokemon_service import *
from tests.agents.fake_pokemon_service_api_agent import *
from src.agents.pokemon_service_api_agent import *
from tests.factory.pokemon_factory import *

class TestPokemonService:
    def test_pokemon_should_be_define(self):
        pokemon_service = PokemonService(FakePokemonServiceApiAgent()) 
        assert type(pokemon_service) is PokemonService

    def test_pokemon_should_have_method_hablar(self):
        pokemon_service = PokemonFactory(FakePokemonServiceApiAgent()).build()
        instance=pokemon_service.hablar("ditto")
        assert isinstance(instance,dict)

    def test_should_pick_pokemon_and_search_abilities(self):
        pokemon_service = PokemonService(FakePokemonServiceApiAgent())
        
        abilities = pokemon_service.search_abilities("ditto")
        assert isinstance(abilities,tuple)

def test_pokemon_factory_should_receive_agent_as_parameter_or_implement_fake_agent():
    pokemon_factory = PokemonFactory().build()
    assert type(pokemon_factory) is PokemonService
