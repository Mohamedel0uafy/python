import tkinter as tk

root = tk.Tk()
root.title("Registration Form")#
root.geometry("400x300")

tk.Label(root, text="Name:", font=("Arial", 12)).grid(row=0, column=0, pady=5, sticky="e")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="Gender:", font=("Arial", 12)).grid(row=1, column=0, pady=5, sticky="e")
gender_entry = tk.Entry(root, width=30)
gender_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="City:", font=("Arial", 12)).grid(row=2, column=0, pady=5, sticky="e")
city_entry = tk.Entry(root, width=30)
city_entry.grid(row=2, column=1, pady=5)

tk.Label(root, text="Email:", font=("Arial", 12)).grid(row=3, column=0, pady=5, sticky="e")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=3, column=1, pady=5)

tk.Label(root, text="Phone:", font=("Arial", 12)).grid(row=4, column=0, pady=5, sticky="e")
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=4, column=1, pady=5)

tk.Label(root, text="Course:", font=("Arial", 12)).grid(row=5, column=0, pady=5, sticky="e")
course_entry = tk.Entry(root, width=30)
course_entry.grid(row=5, column=1, pady=5)

tk.Button(root, text="Submit", bg="green", fg="white", font=("Arial", 12)).grid(row=6, column=0, pady=10, padx=40)
tk.Button(root, text="Cancel", bg="red", fg="white", font=("Arial", 12), command=root.destroy).grid(row=6, column=1, pady=10)










root.mainloop()
