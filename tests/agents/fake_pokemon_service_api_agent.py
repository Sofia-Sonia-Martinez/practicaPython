class FakePokemonServiceApiAgent:
    def find_pokemon(self, name):
        return {
            "abilities": [
                {
                    "ability": {
                        "name": "limber",
                        "url": "https://pokeapi.co/api/v2/ability/7/"
                    },
                    "is_hidden": False,
                    "slot": 1
                },
                {
                    "ability": {
                        "name": "imposter",
                        "url": "https://pokeapi.co/api/v2/ability/150/"
                    },
                    "is_hidden": True,
                    "slot": 3
                }
            ],
            "base_experience": 101,
            "forms": [
                {
                    "name": "ditto",
                    "url": "https://pokeapi.co/api/v2/pokemon-form/132/"
                },
            ],
            "game_indices": [
                {
                    "game_index": 76,
                    "version": {
                        "name": "red",
                        "url": "https://pokeapi.co/api/v2/version/1/"
                    }
                },
                {
                    "game_index": 76,
                    "version": {
                        "name": "blue",
                        "url": "https://pokeapi.co/api/v2/version/2/"
                    }
                },
                # ... (continúa con el resto de las versiones)
            ]
        }

