from tkinter import *

root=Tk()
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT , fill=Y)
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for line in range(30) :
    mylist.insert(END,'this is line number'+str(line))
mylist.pack(side=LEFT , fill=BOTH)
scrollbar.config(command=mylist.yview)
root.mainloop()



