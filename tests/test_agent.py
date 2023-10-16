import pytest
from requests.models import Response
from src.interfaces.pokemon_api_interface import PokemonApiInterface 
from src.services.pokemon_service import *
from tests.agents.fake_pokemon_service_api_agent import *
from src.agents.pokemon_service_api_agent import *
from tests.factory.pokemon_factory import *


class TestAgentService:
    def test_should_return_valid_json(self) :
        agent=PokemonServiceApiAgent()
        book_service=PokemonFactory(agent).build()
        result=book_service.hablar("ditto")
        assert len(result) > 0

    def test_request_should_return_valid_response(self) :
        agent = PokemonServiceApiAgent()
        response = agent.make_request("ditto")
        assert type(response) is Response

    def test_should_parse_response_to_json(self) :
        agent = PokemonServiceApiAgent()
        response = agent.make_request("ditto")
        parsed_response = agent.parsed_json(response)
        assert type(parsed_response) is dict
 
