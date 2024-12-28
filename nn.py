from tkinter import *

# Create main window
root = Tk()
root.title("Canvas Example")

# Create a Canvas widget
canvas = Canvas(root, width=500, height=500)
canvas.pack()

# Draw shapes on the canvas
canvas.create_line(10, 10, 200, 200, fill="blue", width=5)  # Draw line
canvas.create_rectangle(50, 50, 150, 150, fill="red")       # Draw rectangle
canvas.create_oval(200, 50, 350, 200, fill="green")         # Draw oval
canvas.create_text(250, 250, text="Hello Canvas!", font=("Arial", 20))  # Draw text

# Run the application
root.mainloop()


