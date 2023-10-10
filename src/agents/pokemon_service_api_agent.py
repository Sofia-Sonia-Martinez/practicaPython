import requests
import json
from src.interfaces.pokemon_api_interface import *

class PokemonServiceApiAgent(PokemonApiInterface):
    
    def find_pokemon(self, name):
        self.name = name
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.name}').json()
        abilities = response["abilities"]
        ability=[]
        for ability_info in abilities:
            ability_name = ability_info["ability"]["name"]
            ability.append(ability_name)
        return name, ability


