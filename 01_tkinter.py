from tkinter import *

root = Tk()
root.title("Simple GUI")

# Create a label widget
myLabel = Label(root, text="Hello World!")

# Shoving it onto the screen
myLabel.pack()

root.mainloop()

# Run the script and you will see a window with the text "Hello World!" in it.

# The first thing we need to do is import the Tkinter module.

# Next, we create a root window. This is the main window that will contain all of our widgets.

# We then create a label widget. This is a widget that just displays some text.

# Finally, we use the pack method to put the label widget into the root window.

