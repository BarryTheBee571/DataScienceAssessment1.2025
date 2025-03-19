import requests

base_url="https://pokeapi.co/api/v2/"

def get_pokemoninfo(name):
    url = f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    if response.status_code ==200:
        pokemondata =response.json()
        return pokemondata
    else:
        print("Not Found. Check for typos")

pokemonname= input("What pokemone would you like to learn about? ")
pokemon_info= get_pokemoninfo(pokemonname)

def pokemonstandard():
    if pokemon_info:
        print(f"{pokemon_info['name']}")
        print(f"{pokemon_info['id']}")

choice = input("What would you like to know about this pokemon?(Types, Stats, Forms, Abilities, Amount of Moves, Sound)")

if choice==str("types"):
    pokemonstandard
    print(f"{pokemon_info['type']}")