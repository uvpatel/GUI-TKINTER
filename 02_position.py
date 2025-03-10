from tkinter import *

root = Tk()
root.title("Simple GUI")

# Create a label widget
myLabel = Label(root, text="Hello World!",height=10, width=50, bg="black", fg="white")
myLabel2 = Label(root, text="Hello Patel!",height=10, width=50, bg="black", fg="white")

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
# Shoving it onto the screen
# myLabel.pac  k()

root.mainloop()

  