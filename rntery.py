from tkinter import *
a=Tk()
Label(a,text="first name").grid(row=0)
Label(a,text="last name").grid(row=1)
b=Entry(a)
c=Entry(a)
b.grid(row=0,column=1)
c.grid(row=1,column=1)
mainloop()