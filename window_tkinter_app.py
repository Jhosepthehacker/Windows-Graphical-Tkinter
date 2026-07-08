from tkinter import *
from tkinter import messagebpx, Toplevel, ttk

app = Tk()
app.title("Window")
app.geometry("400x400")

widget_text = Label(text="Hola")
widget_text.grid(row=0, column=0)

app.conffig(bg="#ff0000")

app.mainloop()