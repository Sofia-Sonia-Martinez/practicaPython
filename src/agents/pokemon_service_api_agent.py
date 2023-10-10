import requests
import json
from src.interfaces.pokemon_api_interface import *

class PokemonServiceApiAgent(PokemonApiInterface):
    
    def find_pokemon(self, name):
        self.name = name
        response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto').json()
        abilities = response["abilities"]
        ability=[]
        for ability_info in abilities:
            ability_name = ability_info["ability"]["name"]
            ability.append(ability_name)
        return name, ability


