import tkinter as tk
from PIL import ImageTk

bg_colour = "#7AB800"

# initialise app
root = tk.Tk()
root.title("New South Wales Convict History Database")

# get screen width and height
x = root.winfo_screenwidth() //2 - (700//2) # width of screen
y = int(root.winfo_screenheight() * 0.1) # height of screen

# x/y coords for Tk root window
root.geometry('500x600+' + str(x) + '+' + str(y))

#Create a frame widget
frame1 = tk.Frame(root, width = 500, height = 600, bg=bg_colour)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

#frame1 widgets
logo_img = ImageTk.PhotoImage(file="UNELogo.png")
logo_widget = tk.Label(frame1, image = logo_img, bg=bg_colour)
logo_widget.image = logo_img
logo_widget.pack()

tk.Label(frame1, 
         text="UNE - NSW Convict History Database",
         bg = bg_colour,
         fg="white",
         font = ("TkMenuFont", 14)
         ).pack()


#Set dimension of screen and where it is placed
#root.geometry('%dx%d+%d+%d' % (rWidth, rHeight, x, y))

# run app
root.mainloop()


