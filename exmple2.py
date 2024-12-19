import tkinter as tk

window = tk.Tk()
window.title("Divisor Calculator")
window.geometry("400x300")

label = tk.Label(window, text="Enter a number:")
label.grid(row=0, column=0)

entry_field = tk.Entry(window)
entry_field.grid(row=0, column=1)


result_label = tk.Label(window, text="")
result_label.grid(row=1, column=0, columnspan=2)


def calculate_divisors():
    try:
        n = int(entry_field.get())
        divisors = [i for i in range(1, n + 1) if n % i == 0]
        result_label.config(text=f"Divisors of {n}: {divisors}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter an integer.")

button = tk.Button(window, text="Calculate Divisors", command=calculate_divisors)
button.grid(row=2, column=0, columnspan=2)

window.mainloop()