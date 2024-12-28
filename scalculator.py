from tkinter import *

root=Tk()
root.title("scalculator")
root.geometry("400x600")
label=Label(root,text="")
label.grid(row=0,column=0)

frame=Frame(root)
btn=Button(frame,text="X**2",width=10)
btn.grid(row=3,column=0)
btn=Button(frame,text="X**n",width=10)
btn.grid(row=3,column=1)
btn=Button(frame,text="Log",width=10)
btn.grid(row=3,column=2)
btn=Button(frame,text="C",width=10)
btn.grid(row=3,column=3)
frame.grid(row=1)

















root.mainloop()