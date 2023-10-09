from abc import abstractmethod , ABC 

class PokemonApiInterface(ABC):
    @abstractmethod
    def find_pokemon(self, name, abiliti):
        return [{"name":"ditto","abiliti":"limber"}]    
