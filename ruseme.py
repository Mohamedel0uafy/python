from tkinter import *

root=Tk()
root.geometry("300x200")
w =Label(root,text="hello world")
w.grid(row=0)
button=Button(root,text="shut down",width=30,command=root.destroy).grid(row=1)
Label(root,text="first name").grid(row=2 ,column=0)
Label(root,text="last name").grid(row=3)
a=Entry(root)
b=Entry(root)
a.grid()
b.grid()







root.mainloop()