import requests
import pygame
import time
import os
from pathlib import Path

pygame.init()
pygame.mixer.init()
base_url="https://pokeapi.co/api/v2/"

def get_pokemoninfo(name):
    url = f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    if response.status_code ==200:
        pokemondata =response.json()
        return pokemondata
    else:
        print("Not Found. Check for typos")

pokemonname= input("What pokemon would you like to learn about? ").lower()
pokemon_info= get_pokemoninfo(pokemonname)

def pokemonstandard():
    if pokemon_info:
        print("Name: " + pokemon_info['name'].capitalize())
        print("ID: " + f"{pokemon_info['id']}")


def types():
    for type_info in pokemon_info['types']:
        print("Type: " + type_info['type']['name'].capitalize())

def abilities():
    abilities = [a["ability"]["name"].capitalize() for a in pokemon_info["abilities"]]
    print(f"Abilities: {', '.join(abilities)}")

def stats():
    stats = {s["stat"]["name"].capitalize(): s["base_stat"] for s in pokemon_info["stats"]}
    for stat, value in stats.items():
        print(f"{stat}: {value}")
def moves():
    moves_count = len(pokemon_info['moves'])
    print(f"Number of moves: {moves_count}\n(cannot display each individual move)")
def sound():
    pokeID = f"{pokemon_info['id']}"
    pokesound = f"{str(pokeID).zfill(4)}_{pokemon_info['forms'][0]['name']}.latest"
    out_file = Path(f"sounds\{pokesound.capitalize()}.ogg").expanduser()
    resp = requests.get(f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{pokeID}.ogg")
    resp.raise_for_status()
    with open(out_file, "wb") as fout:
        fout.write(resp.content)
    time.sleep(1)
           
    file_path = r"sounds"'\\' + pokesound + ".ogg"
    pygame.mixer.music.load(str(file_path))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

choice = input("What would you like to know about this pokemon?(Types, Stats, Abilities, Moves, Sound or Everything): ").lower()
while choice != "End":
    if choice=="types":
        pokemonstandard()
        types()
    elif choice=="abilities":
        pokemonstandard()
        abilities()
    elif choice=="stats":
        pokemonstandard()
        stats()
    elif choice=="moves":
        pokemonstandard()
        moves()
    elif choice=="sound":
        sound()
    elif choice=="everything":
        pokemonstandard()
        types()
        stats()
        abilities()
        moves()
        sound()
    else:
        print("Please enter a valid option")
