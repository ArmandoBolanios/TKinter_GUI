from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I cliecked a Button!")
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=myClick, fg="#000", bg="#bbb")
myButton.pack()


root.mainloop()