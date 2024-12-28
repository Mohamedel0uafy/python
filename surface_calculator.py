from customtkinter import *
import customtkinter
import math

def calculer():
    shape = v.get()
    
    if shape == 3:
        try:
            longueur = float(entry_longueur.get())
            largeur = float(entry_largeur.get())
            surface = longueur * largeur
            Circonférence = 2 * (longueur + largeur)  
            result_text = f"Surface (Rectangle) = {surface:.2f}"
        except ValueError:
            result_text = "Erreur: Veuillez entrer des nombres valides."
    
    elif shape == 2:
        try:
            surface = math.pi *float( entry_longueur.get()) ** 2
            volume = (4 / 3) * math.pi * float(entry_longueur.get()) ** 3
            result_text = f"Surface (Cercle) = {surface:.2f}\nVolume (Sphere) = {volume:.2f}"
        except ValueError:
            result_text = "Erreur: Veuillez entrer un rayon valide."
    
    else:
        result_text = "Veuillez sélectionner une forme."
    
    result_label.configure(text=result_text)

root = CTk()
root.geometry("400x400")
customtkinter.set_appearance_mode("light")

v = IntVar(value=1) 

radio_rectangle = customtkinter.CTkRadioButton(root, text="Rectangle", variable=v, value=3)
radio_rectangle.grid(row=0, padx=60, pady=10, sticky=W)

radio_cercle = customtkinter.CTkRadioButton(root, text="Cercle", variable=v, value=2)
radio_cercle.grid(row=0, column=1, pady=10, sticky=W)

label_longueur = CTkLabel(root, text="Longueur / Rayon :")
label_longueur.grid(row=1, padx=10, pady=10, sticky=W)
entry_longueur = CTkEntry(root)
entry_longueur.grid(row=1, column=1, pady=10, sticky=W)

label_largeur = CTkLabel(root, text="Largeur (Rectangle uniquement) :")
label_largeur.grid(row=2, padx=10, pady=10, sticky=W)
entry_largeur = CTkEntry(root)
entry_largeur.grid(row=2, column=1, pady=10, sticky=W)

btn_calculer = CTkButton(root, text="Calculer", command=calculer)
btn_calculer.grid(row=3, column=1, pady=10, sticky=W)

result_label = CTkLabel(root, text="")
result_label.grid(row=4, columnspan=2, pady=20)

root.mainloop()
