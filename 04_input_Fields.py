from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="black", fg="white", borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name")

def myClick():
    myLabel = Label(root, text="Hello"+e.get())
    myLabel.pack()


myButton = Button(root, text="Enter Your Name", padx=50, pady=20,command=myClick ,fg="crimson", bg="Black")
myButton.pack()

root.mainloop()