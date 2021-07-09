from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I cliecked a Button!")
    myLabel.pack()


myButton = Button(root, text="Click Me!")

myButton.pack()

root.mainloop()