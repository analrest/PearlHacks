"""Pearl Hacks - Ana Restrepo"""
import tkinter as tk

def turn_red(event):
    event.widget.config(bg="red") 

# Window.
root = tk.Tk() #name for the window

# Window name and size.
root.geometry("500x600") #size of window
root.title("Dog Breed Game") #name of window

# Text Inside Window.
label = tk.Label(root, text="The Dog Breed Game", font=('Comic Sans MS', 18)) #text
label.pack(padx=20, pady=20) #putting the text in the window

# A Textbox.
textbox = tk.Text(root, height=3, font=('Arial', 16)) #creating a textbox that is height of 3 that users can text into
textbox.pack(padx=10) #applying the textbook on the window with space between previous text

# NOT USED - One-lined Textbox.
# myentry = tk.Entry(root) #doesn't let user go into multi-line (used for one lie entry)
# myentry.pack() 

# Button.
button = tk.Button(root, text="Let's Play!", font=('Arial', 18))
button.pack(padx=10, pady=10)

# A Grid of Buttons.
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)


# Each Individual Button in the Grid.
btn1 = tk.Button(buttonframe, text="1",  font=('Comic Sans MS', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn1.bind("<Button-1>", turn_red)

btn2 = tk.Button(buttonframe, text="2",  font=('Comic Sans MS', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn2.bind("<Button-1>", turn_red)

btn3 = tk.Button(buttonframe, text="3",  font=('Comic Sans MS', 18))
btn3.grid(row=1, column=0, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4",  font=('Comic Sans MS', 18), command=buttonframe.config(bg="red"))
btn4.grid(row=1, column=1, sticky=tk.W+tk.E)




# Putting the Buttons on the Window.
buttonframe.pack(fill='x', pady=40) #stretch into the x dimension

# Putting a Button Anywhere.
# anotherbtn = tk.Button(root, text="TEST") #creating the button
# anotherbtn.place(x=200, y=200, height=100, width=100) #placing the button at cordinates x and y




root.mainloop() #constructor

