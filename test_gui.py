import tkinter as tk

def on_submit():
    user_input = entry.get()
    result_label.config(text=f'Hello, {user_input}!')

app = tk.Tk()
app.title("Simple GUI")

label = tk.Label(app, text="Enter your name:")
label.pack()

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Submit", command=on_submit)
button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
