import tkinter as tk
from tkinter import messagebox, filedialog
import json
from crud_menu import CRUDApp
from crud_operations import CRUDOperations


class HomeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application d'accueil")
        self.geometry("400x200")
        
        self.db = CRUDOperations()
        
        self.create_menu()
        
        welcome_label = tk.Label(self, text="Bienvenue dans l'application CRUD", font=("Arial", 16))
        welcome_label.pack(pady=50)

    def create_menu(self):
        menu_bar = tk.Menu(self)
        
        main_menu = tk.Menu(menu_bar, tearoff=0)
        main_menu.add_command(label="Afficher CRUD App", command=self.open_crud_app)
        main_menu.add_command(label="Sauvegarder les données", command=self.save_data)
        menu_bar.add_cascade(label="Menu", menu=main_menu)
        
        self.config(menu=menu_bar)

    def open_crud_app(self):
        self.destroy()
        app = CRUDApp()
        app.mainloop()

    def save_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            try:
                data = self.db.read_all()
                data_list = [
                    {
                        "id": row[0], 
                        "title": row[1], 
                        "description": row[2], 
                        "priority": row[3], 
                        "status": row[4], 
                        "created_date": row[5], 
                        "due_date": row[6]
                    }
                    for row in data
                ]
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(data_list, file, indent=4)
                messagebox.showinfo("Succès", "Données sauvegardées avec succès!")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de la sauvegarde : {e}")


if __name__ == "__main__":
    app = HomeApp()
    app.mainloop()
