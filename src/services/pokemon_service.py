from src.agents.pokemon_service_api_agent import *
class PokemonService:
    def __init__ (self, agent):
        self.agent = agent

    def hablar(self, name):
        self.name=name
        return self.agent.find_pokemon(self.name)
