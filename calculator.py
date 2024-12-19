from tkinter import *
from PIL import Image, ImageTk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(str(screen.get()))
            screen.set(value)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = Tk()
root.title("Calculator")
iconimage= Image.open("calculator-icon_34473.ico")
iconphoto= ImageTk.PhotoImage(iconimage)
root.iconphoto(False,iconphoto)


screen = StringVar()
entry = Entry(root, textvar=screen, font="Arial 20")
entry.pack(fill=BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in buttons:
    frame = Frame(root)
    frame.pack()
    for char in row:
        button = Button(frame, text=char, font="Arial 15", padx=10, pady=10)
        button.pack(side=LEFT, padx=10, pady=10)
        button.bind("<Button-1>", click)

root.mainloop()
