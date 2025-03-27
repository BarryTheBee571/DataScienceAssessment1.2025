import requests
import pygame
import time
import os
from pathlib import Path

base_url="https://pokeapi.co/api/v2/"

def get_pokemoninfo(name): #this function sends an API request to see if the informaiton is available
    url = f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    if response.status_code ==200:
        pokemondata =response.json()
        return pokemondata
    else:
        print("Not Found. Check for typos") 


def pokemonstandard(): #this gets the name and ID of the pokemon so it can be displayed later
    if pokemon_info:
        print("Name: " + pokemon_info['name'].capitalize())
        print("ID: " + f"{pokemon_info['id']}")


def types(): #this gets the type/s of the pokemon from the api
    for type_info in pokemon_info['types']:
        print("Type: " + type_info['type']['name'].capitalize())

def abilities(): #this gets the abilities of the pokemon from the api
    abilities = [a["ability"]["name"].capitalize() for a in pokemon_info["abilities"]]
    print(f"Abilities: {', '.join(abilities)}")

def stats(): #this funciton displays all the stats that the pokemon has such as HP
    stats = {s["stat"]["name"].capitalize(): s["base_stat"] for s in pokemon_info["stats"]}
    for stat, value in stats.items():
        print(f"{stat}: {value}")

def moves(): #this function displays the amount of moves that a pokemon has access to
    moves_count = len(pokemon_info['moves'])
    print(f"Number of moves: {moves_count}\n(cannot display each individual move)")

def sound(): #this function pulls the sound file from the API, downloads it into a special folder, plays the sound and then wipes the sound of the folder
    pygame.init()
    pygame.mixer.init()
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

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    time.sleep(0.5)

    os.remove(out_file)


while True: #this is the main function and where all the user inputs start
    pokemonname= input("What pokemon would you like to learn about? ")
    pokemon_info= get_pokemoninfo(pokemonname)

    if not pokemon_info:
        continue

    while True:    
        choice = input("What would you like to know about this pokemon?(Types, Stats, Abilities, Moves, Sound or Everything): ").lower() #this gives them the option to see everything or just a specific thing

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
            print("Please enter a valid option") #failsafe for if they enter something that isn't accepted
            continue
        
        learn_more = input("Would you like to learn more about this pokemon? (yes/no): ").lower() #allows them to get another piece of information about the same pokemon
        if learn_more !="yes":
            break
    same_pokemon=input("Would you like to learn something about another pokemon? (yes/no): ").lower() #allows to either exit the program or restart this whole loop for a new pokemon
    if same_pokemon !="yes":
        print("Thank you for using my program. Farewell")
        break
