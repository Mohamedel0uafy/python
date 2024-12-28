from tkinter import *

    
root=Tk()
root.title("timer")
root.geometry("300x200")
label=Label(root,text="Minutes:").grid(row=0,column=1)
label=Label(root,text="Seconds:").grid(row=1,column=1)

minutes_entry=Entry(root)
minutes_entry.grid(row=0,column=2)

seconds_entry=Entry(root)
seconds_entry.grid(row=1,column=2)

button=Button(root,text="start",command=converter)
button.grid(row=2,column=2)

button=Button(root,text="stop",command=converter)
button.grid(row=2,column=2)

root.mainloop()


