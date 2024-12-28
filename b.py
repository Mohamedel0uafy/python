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


        ttk.Label(frame, text="Numéro:").grid(row=0, column=0, sticky=W, pady=5)
        ttk.Entry(frame, textvariable=IntVar(value=self.account_number), state=DISABLED).grid(row=0, column=1, sticky=W, pady=5)


        ttk.Label(frame, text="Propriétaire:").grid(row=1, column=0, sticky=W, pady=5)
        ttk.Entry(frame, textvariable=self.owner).grid(row=1, column=1, sticky=W, pady=5)


        ttk.Label(frame, text="Solde Initial:").grid(row=2, column=0, sticky=W, pady=5)
        ttk.Entry(frame, textvariable=self.initial_balance).grid(row=2, column=1, sticky=W, pady=5)