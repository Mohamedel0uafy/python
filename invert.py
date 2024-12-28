from tkinter import *

# Function to invert colors
def invert_colors():
    current_bg = root["bg"]
    current_fg = label["fg"]
    new_bg = "white" if current_bg == "black" else "black"
    new_fg = "black" if current_fg == "white" else "white"

    root.config(bg=new_bg)
    label.config(bg=new_bg, fg=new_fg)
    button.config(bg=new_fg, fg=new_bg)

# Main window
root = Tk()
root.title("Invert Colors Example")
root.geometry("300x200")
root.config(bg="black")  # Default background color

# Label
label = Label(root, text="Hello, World!", bg="black", fg="white", font=("Arial", 14))
label.pack(pady=20)

# Button to invert colors
button = Button(root, text="Invert Colors", command=invert_colors, bg="white", fg="black")
button.pack(pady=20)

root.mainloop()
