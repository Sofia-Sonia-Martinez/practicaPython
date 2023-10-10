from abc import abstractmethod , ABC 

class PokemonApiInterface(ABC):
    @abstractmethod
    def find_pokemon(self, name):
        return []    
