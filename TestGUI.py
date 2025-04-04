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

base_url = "https://pokeapi.co/api/v2/pokemon/"

def display_default_image():
    """Sets the default image when there's an error or no search yet."""
    logo_image.config(image=default_photo)
    logo_image.image = default_photo 

def fetch_pokemon():
    name = entry.get().lower().strip()
    if not name:
        label_name.config(text="Please enter a Pokémon name!")
        return None  #return None if no name is entered

    url = f"{base_url}{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        display_pokemon(pokemon_data)  # Still updates the UI
        return pokemon_data  # Return the data so other functions can use it
    else:
        label_name.config(text="Pokémon not found")
        label_id.config(text="")
        label_types.config(text="")
        label_abilities.config(text="")
        label_stats.config(text="")
        label_image.config(image="")
        return None  # Return None when the Pokémon isn't found

def display_pokemon(data):
    label_name.config(text=f"Name: {data['name'].capitalize()}")
    label_id.config(text=f"ID: {data['id']}")
    
    types = ", ".join(t["type"]["name"].capitalize() for t in data["types"])
    label_types.config(text=f"Type: {types}")
    
    abilities = ", ".join(a["ability"]["name"].capitalize() for a in data["abilities"])
    label_abilities.config(text=f"Abilities: {abilities}")
    
    stats = "\n".join(f"{s['stat']['name'].capitalize()}: {s['base_stat']}" for s in data["stats"])
    label_stats.config(text=f"Stats:\n{stats}")
    
    image_url = data["sprites"]["front_default"]
    if image_url:
        img_data = requests.get(image_url).content
        img = Image.open(BytesIO(img_data))
        img = img.resize((150, 150))
        img = ImageTk.PhotoImage(img)
        label_image.config(image=img)
        label_image.image = img

def play_sound():
    pygame.init()
    pygame.mixer.init()
    
    name = entry.get().lower().strip()
    pokemon_info = fetch_pokemon()  # Calls fetch_pokemon() without arguments since you removed it
    
    if not pokemon_info:  # Check if fetch_pokemon() failed
        label_name.config(text="Pokémon not found!")
        return  # Exit function to prevent errors
    
    poke_id = pokemon_info.get('id')  # Use .get() to avoid KeyErrors
    
    if not poke_id:
        label_name.config(text="Pokémon ID not found!")
        return
    
    sound_url = f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{poke_id}.ogg"
    
    out_file = Path(f"sounds/{name.capitalize()}.ogg").expanduser()
    
    sound_data = requests.get(sound_url).content
    with open(out_file, "wb") as file:
        file.write(sound_data)
    
    pygame.mixer.music.load(out_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy()==True:
        continue
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    time.sleep(0.5)

    os.remove(out_file)

def random_button():
    random_number = random.randint(1, 1025)  # Generate a random ID within range
    label_name.config(text=f"Random ID: {random_number}")  # Fix the assignment
    entry.delete(0, tk.END)  # Clear the entry field
    entry.insert(0, str(random_number))  # Insert the random number into the entry field
    fetch_pokemon()  # Fetch Pokémon using the random ID

# Create the GUI
root = tk.Tk()
root.title("Pokédex")
root.geometry("350x500")

default_image_path = Path("sounds/filler_image.png")  
default_image = Image.open(default_image_path)  


default_image = default_image.resize((250, 92))  
default_photo = ImageTk.PhotoImage(default_image)

label_image = Label(root, image=default_photo)
label_image.image = default_photo  # Store reference
label_image.pack()

Label(root, text="Enter Pokémon Name:").pack()
entry = Entry(root)
entry.pack()
entry.bind("<Return>", lambda event: fetch_pokemon())
frame_buttons = tk.Frame(root)
frame_buttons.pack()
btn_fetch = Button(frame_buttons, text="Search", command=fetch_pokemon)
btn_fetch.grid(row=0, column=0, padx=5, pady=5)
btn_random = Button(frame_buttons, text="Random", command=random_button)
btn_random.grid(row=0, column=1, padx=5, pady=5)

label_image = Label(root, image=default_photo)
label_image.image = default_photo  
label_image.pack()

label_image = Label(root)
label_image.pack()
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

btn_sound = Button(root, text="Play Sound", command=play_sound)
btn_sound.pack()

root.mainloop()