import tkinter as tk
from tkinter import PhotoImage

def calculate_double():
    try:
        n = int(entry_n.get())
        double_n = n * 2
        output_double.delete(0, tk.END)
        output_double.insert(0, str(double_n))
    except ValueError:
        output_double.delete(0, tk.END)
        output_double.insert(0, "Invalid input")

root = tk.Tk()
root.title("Tkinter Double Calculator")
root.geometry("400x300")

photo = PhotoImage(file="photo.png")
photo_label = tk.Label(root, image=photo)
photo_label.grid(row=0, column=0, columnspan=2, pady=10)

label_n = tk.Label(root, text="Entrer N")
label_n.grid(row=1, column=0, padx=10, pady=5)

entry_n = tk.Entry(root)
entry_n.grid(row=1, column=1, padx=10, pady=5)

label_double = tk.Label(root, text="Le double de N =")
label_double.grid(row=2, column=0, padx=10, pady=5)

output_double = tk.Entry(root)
output_double.grid(row=2, column=1, padx=10, pady=5)

button_validate = tk.Button(root, text="Valider l'operation", command=calculate_double)
button_validate.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
