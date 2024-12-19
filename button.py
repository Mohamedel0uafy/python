import tkinter as tk
r= tk.Tk()
r.title("convertor")
button=tk.Button(r,text="stop",width=30,command=r.destroy)
button.pack()
r.mainloop()