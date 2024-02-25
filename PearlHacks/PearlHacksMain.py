import tkinter as tk
from PIL import Image, ImageTk

# Turn the button red when clicked on.
def turn_red(event):
    event.widget.config(bg="red")


# Second Window:
# QUESTION 1
def open_new_window():
    """Opening a new window after clicking button"""
    for widget in root.winfo_children(): #changes to a new window
        widget.destroy()

    root.geometry("500x600") #size of window
    root.title("First Question")

    label2 = tk.Label(root, text="What Dog Breed is this?", font=('Comic Sans MS', 30)) #text
    label2.pack(padx=20, pady=20) #putting the text in the window

    image = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/GermanShepherd.png") #image variable linked with the pathway to image saved in vscode folder with python file
    tk_image = ImageTk.PhotoImage(image) #creating the image and printing it on the screen

    resize_image = image.resize((800, 800)) #changing the size of the picture (not scaling it, but cropping it bascially)

    frame = tk.Frame(root, width=resize_image.width, height=resize_image.height) #where the image is inside (like a textbox) instead of just placing the image in the entire window
    frame.pack()

    label = tk.Label(frame, image=tk_image) 
    label.image = tk_image #very important in making sure the images appears
    label.place(x=125, y=20) #where the image will be


    # A Grid of Buttons.
    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)


    # Each Individual Button in the Grid.
    btn1 = tk.Button(buttonframe, text="German Shepherd",  font=('Comic Sans MS', 22), command=Q2)
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

    btn2 = tk.Button(buttonframe, text="Bernes Mountain Dog",  font=('Comic Sans MS', 22))
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
    btn2.bind("<Button-1>", turn_red) #calling turn_red function when user clicks the wrong button

    btn3 = tk.Button(buttonframe, text="Belgian Malinios",  font=('Comic Sans MS', 22))
    btn3.grid(row=1, column=0, sticky=tk.W+tk.E)
    btn3.bind("<Button-1>", turn_red)

    btn4 = tk.Button(buttonframe, text="Maltese",  font=('Comic Sans MS', 22))
    btn4.grid(row=1, column=1, sticky=tk.W+tk.E)
    btn4.bind("<Button-1>", turn_red)


    # Putting the Buttons on the Window.
    buttonframe.place (x=100, y=300) #stretch into the x dimension


# QUESTION 2
def Q2():
    """Opening a new window after clicking correct answer"""
    for widget in root.winfo_children():
        widget.destroy() 

    root.geometry("500x600")
    root.title("Second Question")

    label2 = tk.Label(root, text="What Dog Breed is this?", font=('Comic Sans MS', 30)) #text
    label2.pack(padx=20, pady=20) #putting the text in the window

    image = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/EngSpringSpaniel.png")
    tk_image = ImageTk.PhotoImage(image)

    resize_image = image.resize((800, 800))

    frame = tk.Frame(root, width=resize_image.width, height=resize_image.height)
    frame.pack()

    label = tk.Label(frame, image=tk_image)
    label.image = tk_image
    label.place(x=300, y=115)

    # A Grid of Buttons.
    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)


    # Each Individual Button in the Grid.
    btn1 = tk.Button(buttonframe, text="Irish Setter",  font=('Comic Sans MS', 22))
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
    btn1.bind("<Button-1>", turn_red)

    btn2 = tk.Button(buttonframe, text="Golden Retriever",  font=('Comic Sans MS', 22))
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
    btn2.bind("<Button-1>", turn_red)

    btn3 = tk.Button(buttonframe, text="English Springer Spaniel",  font=('Comic Sans MS', 22), command=Q3)
    btn3.grid(row=1, column=0, sticky=tk.W+tk.E)

    btn4 = tk.Button(buttonframe, text="French Spaniel",  font=('Comic Sans MS', 22))
    btn4.grid(row=1, column=1, sticky=tk.W+tk.E)
    btn4.bind("<Button-1>", turn_red)

    # Putting the Buttons on the Window.
    buttonframe.place (x=100, y=300) #stretch into the x dimension


# QUESTION 3
def Q3():
    """Opening a new window after clicking correct answer"""
    for widget in root.winfo_children():
        widget.destroy() 

    root.geometry("500x600")
    root.title("Third Question")

    label2 = tk.Label(root, text="What Dog Breed is this?", font=('Comic Sans MS', 30)) #text
    label2.pack(padx=20, pady=20) #putting the text in the window

    image = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Bluey.png")
    tk_image = ImageTk.PhotoImage(image)

    resize_image = image.resize((800, 800))

    frame = tk.Frame(root, width=resize_image.width, height=resize_image.height)
    frame.pack()

    label = tk.Label(frame, image=tk_image)
    label.image = tk_image
    label.place(x=350, y=50)

    # A Grid of Buttons.
    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)


    # Each Individual Button in the Grid.
    btn1 = tk.Button(buttonframe, text="Corgi",  font=('Comic Sans MS', 22))
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
    btn1.bind("<Button-1>", turn_red)

    btn2 = tk.Button(buttonframe, text="Australian Cattle Dog ",  font=('Comic Sans MS', 22), command=Q4)
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

    btn3 = tk.Button(buttonframe, text="Australian Shepherd",  font=('Comic Sans MS', 22))
    btn3.grid(row=1, column=0, sticky=tk.W+tk.E)
    btn3.bind("<Button-1>", turn_red)

    btn4 = tk.Button(buttonframe, text="Australian Kelpie",  font=('Comic Sans MS', 22))
    btn4.grid(row=1, column=1, sticky=tk.W+tk.E)
    btn4.bind("<Button-1>", turn_red)

    # Putting the Buttons on the Window.
    buttonframe.place (x=100, y=300) #stretch into the x dimension


# QUESTION 4
def Q4():
    """Opening a new window after clicking correct answer"""
    for widget in root.winfo_children():
        widget.destroy() 

    root.geometry("500x600")
    root.title("Fourth Question")

    label2 = tk.Label(root, text="What Dog Breed is this?", font=('Comic Sans MS', 30)) #text
    label2.pack(padx=20, pady=20) #putting the text in the window

    image = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Husky.png")
    tk_image = ImageTk.PhotoImage(image)

    resize_image = image.resize((900, 900))

    frame = tk.Frame(root, width=resize_image.width, height=resize_image.height)
    frame.pack()

    label = tk.Label(frame, image=tk_image)
    label.image = tk_image
    label.place(x=300, y=90)

    # A Grid of Buttons.
    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)


    # Each Individual Button in the Grid.
    btn1 = tk.Button(buttonframe, text="Saint Bernard",  font=('Comic Sans MS', 22))
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
    btn1.bind("<Button-1>", turn_red)

    btn2 = tk.Button(buttonframe, text="Alaskan Malamute",  font=('Comic Sans MS', 22))
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
    btn2.bind("<Button-1>", turn_red)

    btn3 = tk.Button(buttonframe, text="Akita",  font=('Comic Sans MS', 22))
    btn3.grid(row=1, column=0, sticky=tk.W+tk.E)
    btn3.bind("<Button-1>", turn_red)

    btn4 = tk.Button(buttonframe, text="Husky",  font=('Comic Sans MS', 22), command=Q5)
    btn4.grid(row=1, column=1, sticky=tk.W+tk.E)


    # Putting the Buttons on the Window.
    buttonframe.place (x=100, y=300) #stretch into the x dimension


# QUESTION 5
def Q5():
    """Opening a new window after clicking correct answer"""
    for widget in root.winfo_children():
        widget.destroy() 

    root.geometry("500x600")
    root.title("Fifth Question")

    label2 = tk.Label(root, text="What Dog Breed is this?", font=('Comic Sans MS', 30)) #text
    label2.pack(padx=20, pady=20) #putting the text in the window

    image = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Golden2.png")
    tk_image = ImageTk.PhotoImage(image)

    resize_image = image.resize((900, 900))

    frame = tk.Frame(root, width=resize_image.width, height=resize_image.height)
    frame.pack()

    label = tk.Label(frame, image=tk_image)
    label.image = tk_image
    label.place(x=250, y=50)

    # A Grid of Buttons.
    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)


    # Each Individual Button in the Grid.
    btn1 = tk.Button(buttonframe, text="Labrador",  font=('Comic Sans MS', 22))
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
    btn1.bind("<Button-1>", turn_red)

    btn2 = tk.Button(buttonframe, text="Golden Retriever",  font=('Comic Sans MS', 22), command=Q6)
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)


    btn3 = tk.Button(buttonframe, text="Goldendoodle",  font=('Comic Sans MS', 22))
    btn3.grid(row=1, column=0, sticky=tk.W+tk.E)
    btn3.bind("<Button-1>", turn_red)

    btn4 = tk.Button(buttonframe, text="Poodle",  font=('Comic Sans MS', 22))
    btn4.grid(row=1, column=1, sticky=tk.W+tk.E)
    btn4.bind("<Button-1>", turn_red)


    # Putting the Buttons on the Window.
    buttonframe.place (x=100, y=300) #stretch into the x dimension


# QUESTION 6
def Q6():
    """Opening a new window after clicking correct answer"""
    for widget in root.winfo_children():
        widget.destroy() 

    root.geometry("500x600")
    root.title("Sixth Question")

    label2 = tk.Label(root, text="What Dog Breed is this?", font=('Comic Sans MS', 30)) #text
    label2.pack(padx=20, pady=20) #putting the text in the window

    image = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Chihuahua.png")
    tk_image = ImageTk.PhotoImage(image)

    resize_image = image.resize((900, 900))

    frame = tk.Frame(root, width=resize_image.width, height=resize_image.height)
    frame.pack()

    label = tk.Label(frame, image=tk_image)
    label.image = tk_image
    label.place(x=300, y=100)

    # A Grid of Buttons.
    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)


    # Each Individual Button in the Grid.
    btn1 = tk.Button(buttonframe, text="Havanese",  font=('Comic Sans MS', 22))
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
    btn1.bind("<Button-1>", turn_red)

    btn2 = tk.Button(buttonframe, text="Chihuahua",  font=('Comic Sans MS', 22), command=Q7)
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)


    btn3 = tk.Button(buttonframe, text="Poodle",  font=('Comic Sans MS', 22))
    btn3.grid(row=1, column=0, sticky=tk.W+tk.E)
    btn3.bind("<Button-1>", turn_red)

    btn4 = tk.Button(buttonframe, text="Rat Terrier",  font=('Comic Sans MS', 22))
    btn4.grid(row=1, column=1, sticky=tk.W+tk.E)
    btn4.bind("<Button-1>", turn_red)


    # Putting the Buttons on the Window.
    buttonframe.place (x=100, y=300) #stretch into the x dimension


# QUESTION 7
def Q7():
    """Opening a new window after clicking correct answer"""
    for widget in root.winfo_children():
        widget.destroy() 

    root.geometry("500x600")
    root.title("Seventh Question")

    label2 = tk.Label(root, text="What Dog Breed is this?", font=('Comic Sans MS', 30)) #text
    label2.pack(padx=20, pady=20) #putting the text in the window

    image = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Beagle.png")
    tk_image = ImageTk.PhotoImage(image)

    resize_image = image.resize((900, 900))

    frame = tk.Frame(root, width=resize_image.width, height=resize_image.height)
    frame.pack()

    label = tk.Label(frame, image=tk_image)
    label.image = tk_image
    label.place(x=250, y=100)

    # A Grid of Buttons.
    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)


    # Each Individual Button in the Grid.
    btn1 = tk.Button(buttonframe, text="Basset Hound",  font=('Comic Sans MS', 22))
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
    btn1.bind("<Button-1>", turn_red)

    btn2 = tk.Button(buttonframe, text="Fox Hound",  font=('Comic Sans MS', 22))
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
    btn2.bind("<Button-1>", turn_red)

    btn3 = tk.Button(buttonframe, text="Beagle",  font=('Comic Sans MS', 22), command=Q8)
    btn3.grid(row=1, column=0, sticky=tk.W+tk.E)

    btn4 = tk.Button(buttonframe, text="Coon Hound",  font=('Comic Sans MS', 22))
    btn4.grid(row=1, column=1, sticky=tk.W+tk.E)
    btn4.bind("<Button-1>", turn_red)


    # Putting the Buttons on the Window.
    buttonframe.place (x=100, y=300) #stretch into the x dimension


# QUESTION 8
def Q8():
    """Opening a new window after clicking correct answer"""
    for widget in root.winfo_children():
        widget.destroy() 

    root.geometry("500x600")
    root.title("Eighth Question")

    label2 = tk.Label(root, text="What Dog Breed is this?", font=('Comic Sans MS', 30)) #text
    label2.pack(padx=20, pady=20) #putting the text in the window

    image = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Malinios.png")
    tk_image = ImageTk.PhotoImage(image)

    resize_image = image.resize((900, 900))

    frame = tk.Frame(root, width=resize_image.width, height=resize_image.height)
    frame.pack()

    label = tk.Label(frame, image=tk_image)
    label.image = tk_image
    label.place(x=300, y=50)

    # A Grid of Buttons.
    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)


    # Each Individual Button in the Grid.
    btn1 = tk.Button(buttonframe, text="Belgian Malinios",  font=('Comic Sans MS', 22), command=Q9)
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

    btn2 = tk.Button(buttonframe, text="German Shepherd",  font=('Comic Sans MS', 22))
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
    btn2.bind("<Button-1>", turn_red)

    btn3 = tk.Button(buttonframe, text="Belgian Sheepdog",  font=('Comic Sans MS', 22))
    btn3.grid(row=1, column=0, sticky=tk.W+tk.E)
    btn3.bind("<Button-1>", turn_red)

    btn4 = tk.Button(buttonframe, text="Dutch Shepherd",  font=('Comic Sans MS', 22))
    btn4.grid(row=1, column=1, sticky=tk.W+tk.E)
    btn4.bind("<Button-1>", turn_red)


    # Putting the Buttons on the Window.
    buttonframe.place (x=100, y=300) #stretch into the x dimension


# QUESTION 9
def Q9():
    """Opening a new window after clicking correct answer"""
    for widget in root.winfo_children():
        widget.destroy() 

    root.geometry("500x600")
    root.title("Ninth Question")

    label2 = tk.Label(root, text="What Dog Breed is this?", font=('Comic Sans MS', 30)) #text
    label2.pack(padx=20, pady=20) #putting the text in the window

    image = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Lab3.png")
    tk_image = ImageTk.PhotoImage(image)

    resize_image = image.resize((1000, 1000))

    frame = tk.Frame(root, width=resize_image.width, height=resize_image.height)
    frame.pack()

    label = tk.Label(frame, image=tk_image)
    label.image = tk_image
    label.place(x=350, y=50)

    # A Grid of Buttons.
    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)


    # Each Individual Button in the Grid.
    btn1 = tk.Button(buttonframe, text="Golden Retriever",  font=('Comic Sans MS', 22))
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
    btn1.bind("<Button-1>", turn_red)

    btn2 = tk.Button(buttonframe, text="Smooth Coat Collie",  font=('Comic Sans MS', 22))
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
    btn2.bind("<Button-1>", turn_red)

    btn3 = tk.Button(buttonframe, text="Vizsla",  font=('Comic Sans MS', 22))
    btn3.grid(row=1, column=0, sticky=tk.W+tk.E)
    btn3.bind("<Button-1>", turn_red)

    btn4 = tk.Button(buttonframe, text="Labrador",  font=('Comic Sans MS', 22), command=Q10)
    btn4.grid(row=1, column=1, sticky=tk.W+tk.E)



    # Putting the Buttons on the Window.
    buttonframe.place (x=100, y=300) #stretch into the x dimension


# QUESTION 10
def Q10():
    """Opening a new window after clicking correct answer"""
    for widget in root.winfo_children():
        widget.destroy() 

    root.geometry("500x600")
    root.title("Tenth Question")

    label2 = tk.Label(root, text="What Dog Breed is this?", font=('Comic Sans MS', 30)) #text
    label2.pack(padx=20, pady=20) #putting the text in the window

    image = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/Aussie.png")
    tk_image = ImageTk.PhotoImage(image)

    resize_image = image.resize((1000, 1000))

    frame = tk.Frame(root, width=resize_image.width, height=resize_image.height)
    frame.pack()

    label = tk.Label(frame, image=tk_image)
    label.image = tk_image
    label.place(x=450, y=100)

    # A Grid of Buttons.
    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)


    # Each Individual Button in the Grid.
    btn1 = tk.Button(buttonframe, text="Australian Shepherd",  font=('Comic Sans MS', 22), command=end_page)
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

    btn2 = tk.Button(buttonframe, text="Bernes Mountain Dog",  font=('Comic Sans MS', 22))
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
    btn2.bind("<Button-1>", turn_red)

    btn3 = tk.Button(buttonframe, text="Border Collie",  font=('Comic Sans MS', 22))
    btn3.grid(row=1, column=0, sticky=tk.W+tk.E)
    btn3.bind("<Button-1>", turn_red)

    btn4 = tk.Button(buttonframe, text="Rough Coat Collie",  font=('Comic Sans MS', 22))
    btn4.grid(row=1, column=1, sticky=tk.W+tk.E)
    btn4.bind("<Button-1>", turn_red)


    # Putting the Buttons on the Window.
    buttonframe.place (x=100, y=300) #stretch into the x dimension

def end_page():
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("500x600")
    root.title("End Screen")

    label = tk.Label(root, text="Congrats! You've Won The Dog Breed Game!", font=('Comic San MS', 35))
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

label = tk.Label(root, text="The Dog Breed Game", font=('Comic San MS', 35)) #opening page text
label.pack(padx=40, pady=40)


button = tk.Button(root, text="Let's Play!", font=('Comic San MS', 22), command=open_new_window) #button that takes you to the next window
button.pack(padx=20, pady=20)


image = Image.open("C:/Users/anare/.vscode/PearlHacks/PearlHacks/MainDogs.png") #opening page image
tk_image = ImageTk.PhotoImage(image)

resize_image = image.resize((800, 800)) #the size of the opening page image

frame = tk.Frame(root, width=resize_image.width, height=resize_image.height)
frame.pack()

label = tk.Label(frame, image=tk_image)
label.image = tk_image
label.place(x=20, y=115)


root.mainloop()