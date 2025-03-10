from tkinter import *

root = Tk()
root.title("Simple Calculator")


e = Entry(root, width=50, bg="black", fg="white", borderwidth=5)
e.grid(row=0, column=0, columnspan=3,padx=10, pady=10)

def button_add():
    return
# Define Buttons
Button_1 = Button(root, text="1", padx=40, pady=20, fg="black", bg="white",command=button_add)
Button_2 = Button(root, text="2", padx=40, pady=20, fg="black", bg="white",command=button_add)      
Button_3 = Button(root, text="3", padx=40, pady=20, fg="black", bg="white",command=button_add)  
Button_4 = Button(root, text="4", padx=40, pady=20, fg="black", bg="white",command=button_add)
Button_5 = Button(root, text="5", padx=40, pady=20, fg="black", bg="white",command=button_add)
Button_6 = Button(root, text="6", padx=40, pady=20, fg="black", bg="white",command=button_add)
Button_7 = Button(root, text="7", padx=40, pady=20, fg="black", bg="white",command=button_add)
Button_8 = Button(root, text="8", padx=40, pady=20, fg="black", bg="white",command=button_add)
Button_9 = Button(root, text="9", padx=40, pady=20, fg="black", bg="white",command=button_add)
Button_0 = Button(root, text="0", padx=40, pady=20, fg="black", bg="white",command=button_add)
# Put the buttons on the screen

Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)
Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)
Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

button_0 = Button(root, text="0", padx=40, pady=20, fg="black", bg="white",command=button_add)


# myButton = Button(root, text="Enter Your stoke qute",command=  myClick , padx=50, pady=20, fg="crimson", bg="Black")
root.mainloop()