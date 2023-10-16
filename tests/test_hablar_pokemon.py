import pytest
from requests.models import Response
from src.interfaces.pokemon_api_interface import PokemonApiInterface 
from src.services.pokemon_service import *
from tests.agents.fake_pokemon_service_api_agent import *
from src.agents.pokemon_service_api_agent import *
from tests.factory.pokemon_factory import *

class TestPokemonService:
    def test_pokemon_should_be_define(self):
        pokemon_service = PokemonService(PokemonServiceApiAgent()) 
        assert type(pokemon_service) is PokemonService

    def test_pokemon_should_have_method_hablar(self):
        pokemon_service = PokemonFactory(PokemonServiceApiAgent()).build()
        assert type(pokemon_service.hablar("ditto")) is tuple 

class TestAgentService:
    def test_should_return_valid_json_name_abiliti(self) :
        agent=PokemonServiceApiAgent()
        book_service=PokemonFactory(agent).build()
        result=book_service.hablar("ditto")
        assert len(result) > 0

    def test_should_return_valid_value_for_given_name(self) :
        agent=PokemonServiceApiAgent()
        pokemon_service=PokemonFactory(agent).build()
        result=pokemon_service.hablar("ditto")
        assert type(result) is tuple

    def test_request_should_return_valid_response(self) :
        agent = PokemonServiceApiAgent()
        response = agent.make_request("ditto")
        assert type(response) is Response

    def test_should_parse_response_to_json(self) :
        agent = PokemonServiceApiAgent()
        response = agent.make_request("ditto")
        parsed_response = agent.parsed_json(response)
        assert type(parsed_response) is dict
       
    def test_should_pick_pokemon_and_search_abilities(self):
        agent = PokemonServiceApiAgent()
        response = agent.make_request("ditto")
        parsed_response = agent.parsed_json(response)
        abilities = agent.search_abilities(parsed_response)
        assert type(abilities) is list
        
def test_pokemon_factory_should_receive_agent_as_parameter_or_implement_fake_agent():
    pokemon_factory = PokemonFactory().build()
    assert type(pokemon_factory) is PokemonService
