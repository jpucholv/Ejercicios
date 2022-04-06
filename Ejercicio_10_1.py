import tkinter
from tkinter import ttk

# Crea la ventanay y la cuadrícula
window = tkinter.Tk()
window.columnconfigure(0, weight=1)

# Crea el label para el formulario de selección
label1 = ttk.Label(window, text='Selecciona tu SO:')

# Crea la lógica del Radiobutton
selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text = "Windows", value = "Windows", variable = selected)
r2 = ttk.Radiobutton(window, text = "MacOS", value = "MacOS", variable = selected)
r3 = ttk.Radiobutton(window, text = "Linux", value = "Linux", variable = selected)


# Crea el objeto, la lógica para el botón 'reset'
def reset (event):
    selected.set(None)

button = tkinter.Button(window,text = "Reset")
button.bind('<Button-1>', reset)


# Pinta los elementos en el grid
label1.grid(column=0, row=0, pady=5, padx=5)
r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)
button.grid(column=0, row=5, pady=5, padx=5)


window.mainloop()