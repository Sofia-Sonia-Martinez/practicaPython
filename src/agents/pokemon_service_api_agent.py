import requests
import json
from requests.exceptions import JSONDecodeError, ConnectionError, ConnectTimeout 
from src.interfaces.pokemon_api_interface import *

class PokemonServiceApiAgent(PokemonApiInterface):
   

    def find_pokemon(self,name):
        ability_list = ()
        response = self.make_request(name)
        parsed = self.parsed_json(response)
        abilities_list=self.search_abilities(parsed)
        return name, abilities_list
 
    def search_abilities(self,parsed):
        abilities = parsed["abilities"]
        ability = []
        for ability_info in abilities:
            ability_name = ability_info["ability"]["name"]
            ability.append(ability_name)
        return ability 

    def make_request(self,name):
        try:
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
            return response
        except (ConnectionError, ConnectTimeout):
            return [{}]

    def parsed_json(self,response = requests.models.Response):
        resp_val = []
        try:
            resp_val = response.json()
        except JSONDecodeError as e:
            print("error al parsear la respuesta de la api a json")
        return resp_val 
    
