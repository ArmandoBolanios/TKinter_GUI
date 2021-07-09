from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="#ff0101", fg="white")
e.pack()


def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()
    
myButton = Button(root, text="Click Me!", command=myClick)    
myButton.pack()

root.mainloop()

