import ttkbootstrap as ttk
from tkinter import StringVar, IntVar, DoubleVar, W, E, DISABLED, NORMAL, END

class BankAccountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account Management")
        self.account_number = 1


        self.owner = StringVar()
        self.initial_balance = DoubleVar()
        self.account_type = StringVar(value="Courant")
        self.interest_rate = DoubleVar()
        self.overdraft_limit = DoubleVar()
        

        self.create_widgets()


        self.accounts = []

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill="both", expand=True)


        self.var=IntVar(value=0)
        ttk.Label(frame, text="Numéro:").grid(row=0, column=0, sticky=W, pady=5)
        self.number_entry = ttk.Entry(frame, textvariable=self.var, state=DISABLED,width=40)
        self.number_entry.grid(row=0, column=1, sticky=W, pady=5)


        ttk.Label(frame, text="Propriétaire:").grid(row=1, column=0, sticky=W, pady=5)
        ttk.Entry(frame, textvariable=self.owner,width=40).grid(row=1, column=1, sticky=W, pady=5)


        ttk.Label(frame, text="Solde Initial:").grid(row=2, column=0, sticky=W, pady=5)
        ttk.Label(frame, text="Euro").place(x=745,y=105)
        ttk.Entry(frame, textvariable=self.initial_balance,width=40).grid(row=2, column=1, sticky=W, pady=5)


        ttk.Label(frame, text="Type:").grid(row=3, column=0, sticky=W, pady=5)
        ttk.Radiobutton(frame, text="Courant", variable=self.account_type, value="Courant", command=self.update_fields).grid(row=3, column=1, sticky=W, pady=5)
        ttk.Radiobutton(frame, text="Epargne", variable=self.account_type, value="Epargne", command=self.update_fields).grid(row=3, column=2, sticky=W, pady=5)


        ttk.Label(frame, text="Taux Intérêt (%):").grid(row=4, column=0, sticky=W, pady=5)
        self.interest_rate_entry = ttk.Entry(frame, textvariable=self.interest_rate,width=40)
        self.interest_rate_entry.grid(row=4, column=1, sticky=W, pady=5)


        ttk.Label(frame, text="M. Découvert:").grid(row=5, column=0, sticky=W, pady=5)
        self.overdraft_limit_entry = ttk.Entry(frame, textvariable=self.overdraft_limit,width=40)
        self.overdraft_limit_entry.grid(row=5, column=1, sticky=W, pady=5)


        ttk.Button(frame, text="Création Compte", command=self.create_account).grid(row=6, column=0, columnspan=3, pady=10)
        self.table = ttk.Treeview(frame, columns=("Numéro", "Propriétaire", "Solde", "Type", "Taux Intérêt", "Montant Découvert"), show="headings")
        self.table.grid(row=7, column=0, columnspan=3, pady=10, sticky=W+E)
        self.table.heading("Numéro", text="Numéro")
        self.table.heading("Propriétaire", text="Propriétaire")
        self.table.heading("Solde", text="Solde")
        self.table.heading("Type", text="Type")
        self.table.heading("Taux Intérêt", text="Taux Intérêt")
        self.table.heading("Montant Découvert", text="Montant Découvert")

        self.update_fields()

    def update_fields(self):
        if self.account_type.get() == "Courant":
            self.interest_rate_entry.config(state=DISABLED)
            self.overdraft_limit_entry.config(state=NORMAL)
          
        else:
            self.interest_rate_entry.config(state=NORMAL)
            self.overdraft_limit_entry.config(state=DISABLED)

    def create_account(self):
        account = {
            "Numéro": self.account_number,
            "Propriétaire": self.owner.get(),
            "Solde": self.initial_balance.get(),
            "Type": self.account_type.get(),
            "Taux Intérêt": self.interest_rate.get() if self.account_type.get() == "Epargne" else "-",
            "Montant Découvert": self.overdraft_limit.get() if self.account_type.get() == "Courant" else "-",
        }

        self.table.insert("", END, values=(account["Numéro"], account["Propriétaire"], account["Solde"], account["Type"], account["Taux Intérêt"], account["Montant Découvert"]))
        self.account_number += 1

        
        self.number_entry.config(state=NORMAL)
        self.var.set(str(self.account_number))
        self.number_entry.config(state=DISABLED)
        
        
        


root = ttk.Window(themename="darkly")
app = BankAccountApp(root)

    
root.mainloop()
