# Import necessary modules
import requests  # For making HTTP requests to the Pokémon API
import tkinter as tk  # For making the GUI
from tkinter import Label, Entry, Button  # Specific functions from tkinter
from PIL import Image, ImageTk  # For displaying images
from io import BytesIO  # For handling image data
import pygame  # For playing Pokemon sound files
import time  # For adding delays
import os  # For file operations
from pathlib import Path  # For better file path handling
import random  # For generating random numbers

# Create the main Tkinter window
root = tk.Tk()
root.title("Pokedex")  # Set window title
root.iconbitmap("other/pngegg.ico")  # Set window icon
root.geometry("280x460")  # Set window size

# Load and prepare the default image to show at startup
default_image_path = Path("other/filler_image.png")
default_image = Image.open(default_image_path)
default_image = default_image.resize((250, 92))  # Resize the image
default_photo = ImageTk.PhotoImage(default_image)  # Convert image to Tkinter format

# Display the default image in a Label widget
label_image = Label(root, image=default_photo)
label_image.image = default_photo  # Keep a reference to prevent garbage collection
label_image.pack()  # Add to window

# Display the default image again (used when no Pokémon is found or on start)
def display_default_image():
    label_image.config(image=default_photo)
    label_image.image = default_photo

# Fetch data about a Pokemon from the API
def fetch_pokemon():
    name = entry.get().lower().strip()  # Get user input
    if not name:
        label_name.config(text="Please enter a Pokémon name!")
        display_default_image()
        return None

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"  # API link
    response = requests.get(url)  # Send request to API
    if response.status_code == 200:
        pokemon_data = response.json()  # Converts JSON to pyhton
        display_pokemon(pokemon_data)  # Show Pokemon data
        return pokemon_data
    else:
        # Reset labels and show error if Pokemon not found
        label_name.config(text="Pokemon not found")
        label_id.config(text="")
        label_types.config(text="")
        label_abilities.config(text="")
        label_stats.config(text="")
        display_default_image()
        return None

# Display Pokemon image and info on the GUI
def display_pokemon(data):
    label_name.config(text=f"Name: {data['name'].capitalize()}")  # Show name
    label_id.config(text=f"ID: {data['id']}")  # Show ID
    
    # Show types
    types = ", ".join(t["type"]["name"].capitalize() for t in data["types"])
    label_types.config(text=f"Type: {types}")
    
    # Show abilities
    abilities = ", ".join(a["ability"]["name"].capitalize() for a in data["abilities"])
    label_abilities.config(text=f"Abilities: {abilities}")
    
    # Show base stats
    stats = "\n".join(f"{s['stat']['name'].capitalize()}: {s['base_stat']}" for s in data["stats"])
    label_stats.config(text=f"Stats:\n{stats}")
    
    # Download and show Pokemon image
    image_url = data["sprites"]["other"]["official-artwork"]["front_default"]
    if image_url:
        img_data = requests.get(image_url).content
        img = Image.open(BytesIO(img_data))
        img = img.resize((150, 150))
        img = ImageTk.PhotoImage(img)
        label_image.config(image=img)
        label_image.image = img

# Play Pokemon sound
def play_sound():
    pygame.init()  # Initialise pygame
    pygame.mixer.init()  # Initialise sound mixer
    
    name = entry.get().lower().strip()
    pokemon_info = fetch_pokemon()  # Get Pokemon info
    
    if not pokemon_info:
        label_name.config(text="Please search for a pokemon")
        return
    
    poke_id = pokemon_info.get("id")  # Get Pokemon ID
    
    # URL of sound file
    sound_url = f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{poke_id}.ogg"
    out_file = Path(f"other/{name.capitalize()}.ogg").expanduser()  # Path to save sound locally
    
    sound_data = requests.get(sound_url).content  # Download sound
    with open(out_file, "wb") as file:
        file.write(sound_data)  # Save sound file
    
    pygame.mixer.music.load(out_file)  # Load sound
    pygame.mixer.music.play()  # Play sound
    while pygame.mixer.music.get_busy():
        continue  # Wait until sound finishes
    
    pygame.mixer.music.stop()  # Stop sound
    pygame.mixer.quit()  # Cleanup
    time.sleep(0.5)  # Small delay
    os.remove(out_file)  # Delete the sound file

# Pick a random Pokemon and fetch its data
def random_button():
    random_number = random.randint(1, 1025)  # Generate random ID
    entry.delete(0, tk.END)  # Clear text box
    entry.insert(0, str(random_number))  # Replaces with new ID
    fetch_pokemon()  # Fetch random Pokémon

# Create label and entry box for Pokemon input
Label(root, text="Enter Pokemon Name:").pack()
entry = Entry(root)
entry.pack()
entry.bind("<Return>", lambda event: fetch_pokemon())  # Fetch on Enter key

# Create button frame
frame_buttons = tk.Frame(root)
frame_buttons.pack()

# Search button
btn_fetch = Button(frame_buttons, text="Search", command=fetch_pokemon)
btn_fetch.grid(row=0, column=0, padx=5, pady=5)

# Random button
btn_random = Button(frame_buttons, text="Random", command=random_button)
btn_random.grid(row=0, column=1, padx=5, pady=5)

# Play sound button
btn_sound = Button(root, text="Play Sound", command=play_sound)
btn_sound.pack()

# Labels to display Pokémon data
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

# Start the GUI application
root.mainloop()