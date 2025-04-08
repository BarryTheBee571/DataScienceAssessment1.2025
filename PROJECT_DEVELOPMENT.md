# <ins> **DataScienceAssessment1.2025**<ins>
---
## <ins> **Requirements Definition** <ins>
---
### <ins> **Functional Requirents** <ins>
**Data Retrieval**\
Users will need to download the needed files, and programs in order to use and view it

**User Interface**\
User is required to have a keyboard and mouse in order to interact with the system and have access to the internet. As well as meeting the requirements (having the necessary things installed)

**Data Display**\
The user will need to be able to obtain the name of the pokemon, their moves, abilities, type, sound, their statistics, and an image of the pokemon.

---
### <ins>**Non- Functional Requirements**<ins>
**Performance**\
The system needs to perform reasonably well, therefore not requiring much power to operate and be efficient in delivering results and the information that has been requested by the user.

**Reliability**\
The system will have to be able to provide the necessary and reliable information/data to the user. If the user searches for a pokemon that doesn't exist or have made a typo, the system should return an error letting them know.

**Usability and Accessibility**\
The system's navigational system should be easy to access and understand. The main function will be a search system which will go find the needed pokemon and the relative information regarding that pokemon, then returning it to the user, allowing them to view it.

---
---
## <ins> **Determining Specifications** <ins>
---
### <ins> **Functional Specifications** <ins>
**User Requirements**\
The system should allow the user to search for the pokemon they want and then return the necessary informaiton related to that pokemon. For example if someone searches for Charizard, it will give you the type, base stats and other informaiton.

**Inputs and Outputs**\
The system will need to accept text or integer (pokemon ID number) as the input and then find them by sending a request to the API to then return all the necessary information regarding that pokemon in a GUI which allows it to be visually appealing.

**Core Features**\
The core features of this program is to search and find information relating to the pokemon that the user has requested and then display that information so that they can view it.

**User Interaction**\
The users will interact with the system through a GUI, which allows them to view the needed information that has been provided by the program relating to whatever they searched. This assists the user with labels on the buttons so that it is simple to navigate and understand.

**Error Handling**\
The system will need to be able to return an error in case the user enters a pokemon that doesn't exist or if they make a typo. 

---
### <ins> **Non-Functional Specificaitons** <ins>
**Performance**\
The program shouldn't take longer than a few seconds to return the necessary information that has been requested by the user regarding the pokemon, a good UI will also be needed to ensure that the program runs as efficient as possible instead of hiding functions under other processes.

**Usability/Accessibility**\
The user interface is incredibly simple, it gives the user a few buttons and a search bar. The search bar can be used to enter the pokemon's name or ID and then you can press enter or the search button making it more efficient. If you want to hear the sound that the pokemon makes, there's the play sound button. Lastly for some fun, there's the random button which generates a random integer between 1-1025 (the number of pokemon there are) and enters it directly into the search bar effectively giving you everything on a random pokemon.

**Reliability**\
An issue that might cause a problem to the program will be typos, or a pokemon that doesn't exist. In this case it will simply return an error message stating that the pokemon doesn't exist. Another issue is that it might slow down and lag significantly if the buttons are spammed too many times.

---
---
## <ins> **Use Cases** <ins>
**Actors**\
User(Someone that likes Pokemon)

**Preconditions**\
Access to the internet and the API (PokeApi)

**Main Flow**
User enters this loop until they exit the program
1. Search for a pokemon
2. Get a random pokemon
3. play the sound of the current pokemon (only works if there is a current pokemon)

**Postconditions**\
Pokemon data has been given to the user

---
---
## <ins> **Design**
**Gantt Chart**\
![image](theory_images/Ganttchart.png "Gantt Chart")
---
**Structure Chart**\
![image](theory_images/Structure%20Chart.png "Structure Chart")
---
**Algorithms**
- #### **Main Function**
```
BEGIN main()
    WHILE not END
        IF choice= searchpokemon
            USERINPUT pokemon_name
            DISPLAY pokemon_data
        ELIF choice= randompokemon
            RANDINT= (1,1025)
            pokemon_name= RANDINT
            fetch_pokemon(pokemon_name)
        ELIF choice= PLAYSOUND
            IF current_pokemon
                Play sound
            ELSE
                error
        ELSE choice= END
    ENDWHILE
END main()
```
![image](theory_images/Flowchart%20(1).png "Flowchart of Main Function")

---
- #### **Sub-function (Display Pokemon)**
```
BEGIN display_pokemon()
    USERINPUT pokemon_name
    fetch_pokemon(pokemon_name)
END display_pokemon
```
<img src="theory_images/Blank%20diagram%20(3).png" alt= "random pokemon" width = "150"/>

---

- #### **Sub-function (random pokemon)**
```
BEGIN random_pokemon
    RANDINT= (1,1025)
    pokemon_name=RANDINT
    fetch_pokemon(pokemon_name)
    display_pokemon
END rnadom_pokemon
```
<img src="theory_images/Blank%20diagram%20(4).png" alt= "random pokemon" width = "150"/>

---

**Data Dictionary**

| Variable | Data Type | Format for Display | Size in Bytes | Size for Display | Description  | Example | Validation |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| name | String | Text | 50 | 50 | The name of the pokemon | Glaceon | Must be valid Pokemon name |
| ID | Integer | Whole Number | 4 | 4 | The ID number of the pokemon | 471 | Must be positive |
| type | String | Text | 50 | 50 | The type/s of the pokemon  | Ice | Must be the type of the pokemon |
| abilities | String | Text | 100 | 100 | The abilities that the pokemon has | Snow Cloak | Must be a ability of the pokemon |
| stats | Integer | Whole Number | 4 | 4 | The base stats of the pokemon | HP: 65 | Must be valid base stats for pokemon |
| moves | Integer | Whole Number | 4 | 4 | The amount of moves that the pokemon has access to | 87 | Must be valid moves from game |
| sound | Binary | n/a | varies | n/a | The sound that the pokemon made in the games | n/a | Must be valid .ogg file from PokeAPI |
| image | Image | n/a | varies | n/a | The image of a pokemon | <img src="theory_images/471.png" alt= "Glaceon" width = "100"/>| Must be the official artwork of the pokemon |

---
---
## <ins> **Development** <ins>
```
# Import necessary modules
import requests  # For making HTTP requests to the Pokemon API
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

# Display the default image again (used when no Pokemon is found or on start)
def display_default_image():
    label_image.config(image=default_photo)
    label_image.image = default_photo

# Fetch data about a Pokemon from the API
def fetch_pokemon():
    name = entry.get().lower().strip()  # Get user input
    if not name:
        label_name.config(text="Please enter a Pokemon name!")
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
    fetch_pokemon()  # Fetch random Pokemon

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

# Labels to display Pokemon data
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
```
---
---
## <ins> **Testing and Debugging** <ins>
**Ongoing Evaluations**
1. 3/03/25  
created the repository
2. 5/03/2025  
layed out everything needed for the theory (headings and subheadings). Helps me see all the stuff that I have to do and what I haven't done yet
3. 10/03/2025  
Did most of the theory for the start such as specifying requirements, etc. May need to change in the future as the program may change goals. Also finished gantt chart which provides me with a good schedule to go of.
4. 11/01/2025  
Did the structure chart, may need to change in future as the program changes
5. 18/03/2025  
Started on the pseudocode for the algorithms, may need to change once again in the future due to changes in the program
6. 19/03/2025  
Finished off the rest of the graphs needed for the algorithms, these may need to be changed in the future. Finally started on the main.py, after adding a few funcitons that work. Still experimenting
7. 21/03/2025  
literally made type a plural and that's it
8. 24/03/2025  
Fixed all my graphs to align more with my program, may still need to change in future. Added a sound function that plays the sound of the pokemon then deletes it. Also finished my main code now just needs some tweaking. 
9. 25/03/2025  
Finished of the diagrams and pseudocode, hopefully won't have to change again in the future (foreshadowing). 
10. 28/03/2025  
Finished the readme and requirements as well as adding comments explaining what each funcsions does. I also added the entire program into a code block in the development section of the project development.
11. 31/03/2025  
I fixed a bug as when there is no files in the sounds folder, it disappears. This is a problem for when a new user is cloning the repository to use it as we need a sound folder to store and play the sound. Fixed it by putting a random image into the folder which means that the folder won't disappear when the repository is closed. 
12. 2/04/2025  
Finished filling in the data dictionary
13. 3/04/2025  
I made a test GUI because I had time and had nothing else to do, it works but could be better in the visual department.
14. 4/04/2025  
Trying to make a random button that gives you a random pokemon after miles asked for it :/
15. 7/04/2025  
Replaced main.py with the TestGUI as it works better and is mroe visually appealing.
16. 8/04/2025  
Finished the graphs to finally adjust them to the program. Finished tweaking the code. All that is left is the theory


---
### <ins> **Maintenance** <ins>
**Maintenance Questions**\
1. Explain how you would handle issues caused by changes to the PokeAPI over time.\
If the PokeAPI changed over time, the code could be edited quite simply, for example if they update the image for the pokemon it would just be a simple change to 1 line. If they add new pokemon, the randint limit will need to be increased to suit it. 

2. Explain how you would ensure the program remains compatible with new versions of Python and libraries like requests and matplotlib.\
Check if any updates to requests, pygame, tkinter are available. Test the program often so see if it still functions correctly.

3. Describe the steps you would take to fix a bug found in the program after deployment.\
Get an example and an exact guide to how the bug happened so that you can recreate it, then check the error message to find what the problem is and then use a debugger to find where the bug is. Now fix the code and update the program files to the newer files.

4. Outline how you would maintain clear documentation and ensure the program remains easy to update in the future.\
Write clear comments in the code explaining what each thing does which makes it easier for if someone else is fixing it or if i've forgotten what the line does, this allows for easy explanations and other things. Each change being updated to github with deatiled commits also helps.


---
### **Peer Evaluation**
Stephen Wirianata:  
Barry GUI work perfectlly with its goal to help users find dat on their pokemon. His GUI provides various features (ncluding the random button) and the PLAY SOUND button. he could add an exit button to exit the program instead of exiting the way of the exit old ways.

Chris Wong:  
Barrys GUI provides multiple features that allows users to improve their knowledge on pokemon. It provides a really nice looking picture and looks a really good and doesnt look pixalated. 

---
**Final Evaluation**\
The program successfully meets most of the functional requirements. It allows users to search for a Pokemon, view its details (name, ID, type, abilities, stats), and see the official artwork. It also includes extra features like a random Pokemon generator and the ability to play Pokemon sounds, which improves the overall user experience. In terms of non-functional requirements, the program has a clean and simple GUI, loads fairly quickly (if you have a decent computer), and handles missing or incorrect Pokemon names with error messages.

Things to improve on could be things such as adding a search filter, for example if you wanted to search by type or generation. Store pokemon and like a go back function, or favouriting a pokemon so that they can have quick access. More stats would also be great such as height, weight or evolution lines. Lastly adding a feature that resizes the window to fit your screen better or if you want it fullscreened.

When I made the program, I followed a simple plan to help me stay on track. First, I thought about what I wanted the program to do, like letting users search for a Pokemon, show its picture, and play its sound. I chose tools like Tkinter to make the window and Requests to get information from the PokeAPI. I built the program one step at a time and tested it often to make sure it worked. Some parts were harder than I expected, but I managed by searching online and trying different things. I think I managed my time fairly well, and overall I’m proud of what I made.

---
---