from tkinter import *
from datetime import datetime#
from PIL import Image , ImageTk
 
root = Tk()
root.title('Digital Clock')

iconimage= Image.open("calculator-icon_34473.ico")
iconphoto= ImageTk.PhotoImage(iconimage)

root.iconphoto(False, iconphoto)
def clk():
    clock = datetime.now().time()
    curclock = clock.strftime("%H:%M:%S")
    lab.config(text=curclock)
    lab.after(1000, clk)
 
lab = Label(font=("Comic Sans MS",50,'bold'))
lab.pack()
 
clk()
 
mainloop()