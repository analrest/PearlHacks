import tkinter as tk
from PIL import Image, ImageTk
import random

# Turn the button red when clicked on.
def turn_red(event):
    event.widget.config(bg="red")


"""Creating a List of all the Images to choose from randomly."""

# Each of the photos turned into Images in tkinter and being assigned a variable name
Bluey = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Bluey.png")
GSD = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/GermanShepherd.png")
SpringSpaniel = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/EngSpringSpaniel.png")
Husky = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Husky.png")
Golden = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Golden2.png")
Chihuahua = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Chihuahua.png")
Beagle = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Beagle.png")
Malinios = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Malinios.png")
Lab = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Lab3.png")
Aussie = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Aussie.png")
Schnauzer = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Schnauzer.png")
Poodle = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/poodle2.png")
Affenpinscher = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/affey.png")
Afghan = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/afghan.png")
Akita = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Akita2.png")
Airdale = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Airedale.png")
Alaskan = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Alaskan.png")
Bulldog = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/bulldog.png")
Cockerspan = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/cockerspan.png")
Eskimo = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/eskimo2.png")
Rat = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/rat.png")
# EDIT HERE WHEN ADDING A NEW DOG

score = 0 

# Second Window:
# QUESTIONS:
def questions():
    """Function to create questions"""
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("500x600")
    root.title("Questions")

    global score
    score += 1

    if score == 15:
        end_page()
    
    else:

        label3 = tk.Label(root, text=f"Score: {score}", font=('Arial', 20))
        label3.place(x=100, y=200)


        label2 = tk.Label(root, text="What Dog Breed is This?", font=('Arial', 30))
        label2.pack(padx=20, pady=20)

        # EDIT HERE WHEN ADDING A NEW DOG
        photolist = [Bluey, GSD, SpringSpaniel, Husky, Golden, Chihuahua, Beagle, Malinios, Lab, Aussie, Schnauzer, Poodle, Affenpinscher, Afghan, Akita, Airdale, Alaskan, Bulldog, Cockerspan, Eskimo, Rat] #edit here when adding a dog
        # EDIT HERE WHEN ADDING A NEW DOG
        random_num = random.randint(0,20) 
        dog = photolist[random_num]

        width, height = 600, 600
        resized_dog = dog.resize((width, height))
        tk_image = ImageTk.PhotoImage(resized_dog)

        label2 = tk.Label(root, image=tk_image)
        label2.image = tk_image
        label2.place(x=700, y=150)


        choices, correct_index = answer_choices(random_num)

        # Creating buttons with choices from answer choices function
        buttonframe = tk.Frame(root)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)


        for i, choice in enumerate(choices):
            if i == correct_index:
                btn = tk.Button(buttonframe, text=choice, font=('Arial', 22), command=questions)

            else:
                btn = tk.Button(buttonframe, text=choice, font=('Arial', 22))
                btn.bind("<Button-1>", turn_red)
            btn.grid(row=i, column=0, sticky=tk.W+tk.E)


        buttonframe.place (x=100, y=300)



def answer_choices(index):
    "Creating answer choices with three being wrong and one being right" 
    # EDIT HERE WHEN ADDING A NEW DOG
    options = ["Australian Cattle Dog", "German Shepherd", "English Springer Spaniel", "Husky", "Golden Retriever", "Chihuahua", "Beagle", "Belgian Malinios", "Labrador Retriever", "Australian Shepherd", "Schnauzer", "Poodle", "Affenpinscher", "Afghan Hound", "Akita", "Airedale Terrier", "Alaskan Malmute", "American Bulldog", "American Cocker Spaniel", "American Eskimo Dog", "Rat Terrier"] #edit here when adding a dog
    correct_index = random.randint(0,3)
    correct = options[index]

    options.remove(correct)
    random.shuffle(options)
    choices = options[:3]
    choices.insert(correct_index, correct)

    return choices, correct_index




def end_page():
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("500x600")
    root.title("End Screen")

    label = tk.Label(root, text="Congrats! You've Won The Dog Breed Game!", font=('Arial', 35))
    label.pack(padx=40, pady=40)

    image = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Celebrate.png")
    tk_image = ImageTk.PhotoImage(image)

    resize_image = image.resize((800, 800))

    frame = tk.Frame(root, width=resize_image.width, height=resize_image.height)
    frame.pack()

    label = tk.Label(frame, image=tk_image)
    label.image = tk_image
    label.place(x=20, y=5)




# Main Window:
root = tk.Tk() #initializing the window

root.geometry("500x600") #size of window

label = tk.Label(root, text="The Dog Breed Game", font=('Arial', 35)) #opening page text
label.pack(padx=40, pady=40)


button = tk.Button(root, text="Let's Play!", font=('Arial', 22), command=questions) #button that takes you to the next window
button.pack(padx=20, pady=20)


image = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/MainDogs.png") #opening page image
tk_image = ImageTk.PhotoImage(image)

width, height = 1000, 500
resized_image = image.resize((width, height))
tk_image = ImageTk.PhotoImage(resized_image)

label = tk.Label(root, image=tk_image)
label.image = tk_image
label.pack(padx=20, pady=20)


root.mainloop()