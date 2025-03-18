import requests

# API Base URL
API_URL = "https://pokeapi.co/api/v2/pokemon/"

# Dictionary to store Pokémon
dex = {}

def search_pokemon(pokemon_name):
    """Search for a Pokémon in the PokéAPI and return its details."""
    response = requests.get(API_URL + pokemon_name.lower())
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"].capitalize(),
            "id": data["id"],
            "type": [t["type"]["name"] for t in data["types"]],
            "hp": data["stats"][0]["base_stat"]  # HP stat
        }
    else:
        print("Pokémon not found.")
        return None

def add_pokemon_to_dex(pokemon_name):
    """Add a Pokémon to the Pokédex if it exists in the API."""
    pokemon = search_pokemon(pokemon_name)
    if pokemon:
        dex[pokemon["name"]] = pokemon
        print(f"{pokemon['name']} added to your Pokédex!")