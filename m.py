from tkinter import *

root = Tk()
root.title("Store Management")

Label(root, text="Store Name", font=("Helvetica", 20)).grid(row=0, column=1, sticky=W, pady=10)
Label(root, text="ID").grid(row=1, column=0, sticky=W, pady=5)
Label(root, text="Name").grid(row=2, column=0, sticky=W, pady=5)
Label(root, text="Price").grid(row=3, column=0, sticky=W, pady=5)
Label(root, text="Quantity").grid(row=4, column=0, sticky=W, pady=5)

a = Entry(root, width=35)
b = Entry(root, width=35)
c = Entry(root, width=35)
d = Entry(root, width=35)

a.grid(row=1, column=1, pady=5)
b.grid(row=2, column=1, pady=5)
c.grid(row=3, column=1, pady=5)
d.grid(row=4, column=1, pady=5)

btn_entry = Button(root, text="Enter", width=10, bg="deepskyblue", fg="black", font=("Arial", 10, "bold"))
btn_entry.grid(row=5, column=1, pady=20, padx=5)

btn_update = Button(root, text="Update", width=10, bg="yellow", fg="black", font=("Arial", 10, "bold"))
btn_update.grid(row=5, column=2, pady=20, padx=5)

btn_delete = Button(root, text="Delete", width=10, bg="red", fg="black", font=("Arial", 10, "bold"))
btn_delete.grid(row=5, column=3, pady=20, padx=5)

e = Entry(root, width=60)
e.grid(row=0, column=5, padx=20)


root.mainloop()
