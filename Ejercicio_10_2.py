import tkinter
from tkinter import ttk

# Crea la ventanay y la cuadrícula
window = tkinter.Tk()
window.columnconfigure(0, weight=1)

# Crea el label para el formulario de selección
label1 = ttk.Label(window, text='Selecciona el número de habitaciones:')

# Crea la lógica del Radiobutton
value1 = tkinter.BooleanVar()
value2 = tkinter.BooleanVar()
value3 = tkinter.BooleanVar()

check1 = ttk.Checkbutton(window, text = "1", variable = value1)
check2 = ttk.Checkbutton(window, text = "2", variable = value2)
check3 = ttk.Checkbutton(window, text = "3", variable = value3)

# Pinta los elementos en el grid
label1.grid(column=0, row=0, pady=5, padx=5)
check1.grid(column=0, row=1, pady=5, padx=5)
check2.grid(column=0, row=2, pady=5, padx=5)
check3.grid(column=0, row=3, pady=5, padx=5)

window.mainloop()