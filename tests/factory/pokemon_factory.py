from src.interfaces.pokemon_api_interface import *
from src.services.pokemon_service import *
from src.agents.pokemon_service_api_agent import *

class PokemonFactory: 
    def __init__ (self,agent: PokemonApiInterface = PokemonServiceApiAgent) ->None: 
        self.agent = agent
        pass

    def build(self):
        return PokemonService(self.agent)

