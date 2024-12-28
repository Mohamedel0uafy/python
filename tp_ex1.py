from tkinter import *
def click():
    G.config(text="button clicked !")
root=Tk()
root.geometry("300x200")
G=Label(root,text="Click the button and check the message text :")
G.pack()
btn=Button(root,text="Click me",width=30,command=click).pack()


        

root.mainloop()
