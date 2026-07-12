import tkinter as tk

def add():
    result.config(text=str(float(num1.get()) + float(num2.get())))

def subtract():
    result.config(text=str(float(num1.get()) - float(num2.get())))

def multiply():
    result.config(text=str(float(num1.get()) * float(num2.get())))

def divide():
    if float(num2.get()) != 0:
        result.config(text=str(float(num1.get()) / float(num2.get())))
    else:
        result.config(text="Cannot divide by zero")


app = tk.Tk()
app.title("Simple Calculator")
app.geometry("300x300")


tk.Label(app, text="Number 1").pack()
num1 = tk.Entry(app)
num1.pack()

tk.Label(app, text="Number 2").pack()
num2 = tk.Entry(app)
num2.pack()


tk.Button(app, text="Add", command=add).pack()
tk.Button(app, text="Subtract", command=subtract).pack()
tk.Button(app, text="Multiply", command=multiply).pack()
tk.Button(app, text="Divide", command=divide).pack()


result = tk.Label(app, text="Result")
result.pack()


app.mainloop()