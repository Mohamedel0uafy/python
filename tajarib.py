from tkinter import *
import math

def on_click(text):
    global expression
    if text == "C":
        expression = ""
    elif text == "=":
        try:
            expression = str(eval(expression))
        except Exception as e:
            expression = "Error"
    elif text == "π":
        expression += str(math.pi)
    elif text == "X**2":
        try:
            expression = str(eval(expression + "**2"))
        except:
            expression = "Error"
    elif text == "sin":
        try:
            expression = str(math.sin(math.radians(float(expression))))
        except:
            expression = "Error"
    elif text == "cos":
        try:
            expression = str(math.cos(math.radians(float(expression))))
        except:
            expression = "Error"
    elif text == "tan":
        try:
            expression = str(math.tan(math.radians(float(expression))))
        except:
            expression = "Error"
    elif text == "X!":
        try:
            expression = str(math.factorial(int(expression)))
        except:
            expression = "Error"
    elif text == "Racine":
        try:
            expression = str(math.sqrt(float(expression)))
        except:
            expression = "Error"
    elif text == "dell":
        expression = expression[:-1]
    elif text == "Degree":
        try:
            expression = str(math.degrees(float(expression)))
        except:
            expression = "Error"
    elif text == "+-":
        try:
            if expression.startswith('-'):
                expression = expression[1:]
            else:
                expression = '-' + expression
        except:
            expression = "Error"
    else:
        expression += text

    label.config(text=expression)

root = Tk()
root.title("Calculator")
root.geometry("400x600")

expression = ""
label = Label(root, text="", font=("Helvetica", 20), anchor='e', bg="white", fg="black", relief="sunken", height=2)
label.grid(row=0, column=0, columnspan=4, sticky="we")

btn = [
    ("X**2", 2, 0), ("X**n", 2, 1), ("Log", 2, 2), ("C", 2, 3),
    ("sin", 3, 0), ("cos", 3, 1), ("tan", 3, 2), ("dell", 3, 3),
    ("SWITCH", 4, 0), ("X!", 4, 1), ("Racine", 4, 2), ("π", 4, 3),
    ("7", 5, 0), ("8", 5, 1), ("9", 5, 2), ("÷", 5, 3),
    ("4", 6, 0), ("5", 6, 1), ("6", 6, 2), ("*", 6, 3),
    ("1", 7, 0), ("2", 7, 1), ("3", 7, 2), ("-", 7, 3),
    ("+-", 8, 0), ("0", 8, 1), (".", 8, 2), ("+", 8, 3),
    ("(", 9, 0), (")", 9, 1), ("=", 9, 2), ("Degree", 9, 3),
]

for txt, rw, col in btn:
    button = Button(root, text=txt, width=10, padx=11, pady=11,
                    command=lambda text=txt: on_click(text))
    button.grid(row=rw, column=col)
    
    if txt in ["X**2", "X**n", "Log", "C", "sin", "cos", "tan", "dell", "SWITCH", "X!", "Racine", "π", "Degree"]:
        button.config(bg="#FFA500", fg="black")
    if txt in ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", "(", ")"]:
        button.config(bg="#b3cccc", fg="black")






root.mainloop()
