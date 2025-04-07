import requests
import tkinter as tk
from tkinter import Label, Entry, Button
from PIL import Image, ImageTk
from io import BytesIO
import pygame
import time
import os
from pathlib import Path
import random

# Create the Tkinter window
root = tk.Tk()
root.title("Pokedex")
root.iconbitmap("other/pngegg.ico")
root.geometry("280x460")

# Load the default Pokemon image
default_image_path = Path("other/filler_image.png")
default_image = Image.open(default_image_path)
default_image = default_image.resize((250, 92))
default_photo = ImageTk.PhotoImage(default_image)

# Create label for Pokemon image
label_image = Label(root, image=default_photo)
label_image.image = default_photo
label_image.pack()

#displays the pokemon logo when you launch the program
def display_default_image():
    label_image.config(image=default_photo)
    label_image.image = default_photo 

#funciton to get the pokemon data such as stats and type
def fetch_pokemon():
    name = entry.get().lower().strip()
    if not name:
        label_name.config(text="Please enter a Pokémon name!")
        display_default_image()
        return None

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        display_pokemon(pokemon_data)
        return pokemon_data
    else:
        label_name.config(text="Pokemon not found")
        label_id.config(text="")
        label_types.config(text="")
        label_abilities.config(text="")
        label_stats.config(text="")
        display_default_image()
        return None

#funciton to display the image of the pokemon
def display_pokemon(data):
    label_name.config(text=f"Name: {data['name'].capitalize()}")
    label_id.config(text=f"ID: {data['id']}")
    
    types = ", ".join(t["type"]["name"].capitalize() for t in data["types"])
    label_types.config(text=f"Type: {types}")
    
    abilities = ", ".join(a["ability"]["name"].capitalize() for a in data["abilities"])
    label_abilities.config(text=f"Abilities: {abilities}")
    
    stats = "\n".join(f"{s['stat']['name'].capitalize()}: {s['base_stat']}" for s in data["stats"])
    label_stats.config(text=f"Stats:\n{stats}")
    
    image_url = data["sprites"]["other"]["official-artwork"]["front_default"]
    if image_url:
        img_data = requests.get(image_url).content
        img = Image.open(BytesIO(img_data))
        img = img.resize((150, 150))
        img = ImageTk.PhotoImage(img)
        label_image.config(image=img)
        label_image.image = img

#funciton to play the sound of the pokemon
def play_sound():
    pygame.init()
    pygame.mixer.init()
    
    name = entry.get().lower().strip()
    pokemon_info = fetch_pokemon()
    
    if not pokemon_info:
        label_name.config(text="Please search for a pokemon")
        return
    
    poke_id = pokemon_info.get("id")
    
    sound_url = f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{poke_id}.ogg"
    out_file = Path(f"other/{name.capitalize()}.ogg").expanduser()
    
    sound_data = requests.get(sound_url).content
    with open(out_file, "wb") as file:
        file.write(sound_data)
    
    pygame.mixer.music.load(out_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    time.sleep(0.5)
    os.remove(out_file)

#function that adds a delay when you press a button so you can't spam it
def delay():
    root.after(1000, random_button)


#function to generate a random pokemon's ID
def random_button():
    random_number = random.randint(1, 1025)
    label_name.config(text=f"Random ID: {random_number}")
    entry.delete(0, tk.END)
    entry.insert(0, str(random_number))
    fetch_pokemon()

# Create UI elements
Label(root, text="Enter Pokemon Name:").pack()
entry = Entry(root)
entry.pack()
entry.bind("<Return>", lambda event: fetch_pokemon())

# Buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack()
btn_fetch = Button(frame_buttons, text="Search", command=fetch_pokemon)
btn_fetch.grid(row=0, column=0, padx=5, pady=5)
btn_random = Button(frame_buttons, text="Random", command=random_button)
btn_random.grid(row=0, column=1, padx=5, pady=5)

btn_sound = Button(root, text="Play Sound", command=play_sound)
btn_sound.pack()

# Labels for Pokemon details
label_name = Label(root, text="")
label_name.pack()
label_id = Label(root, text="")
label_id.pack()
label_types = Label(root, text="")
label_types.pack()
label_abilities = Label(root, text="")
label_abilities.pack()
label_stats = Label(root, text="")
label_stats.pack()

# Run the application
root.mainloop()