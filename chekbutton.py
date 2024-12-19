from tkinter import *
a= Tk()
a.title("chekbutton")
var1=IntVar()
Checkbutton(a,text="male",variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(a,text="female",variable=var2).grid(row=1,sticky=W)
mainloop()

a=Tk()
v=IntVar()
Radiobutton(a,text="1",variable=v,value=1).pack(anchor=W)
Radiobutton(a,text="2",variable=v,value=2).pack(anchor=W)
a.mainloop()
