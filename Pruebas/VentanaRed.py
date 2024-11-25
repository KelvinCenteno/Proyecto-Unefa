import tkinter as tk

def miniVen(event):
    Ventana.overrideredirect(False)
    Ventana.iconify()

def on_state_change(event):
    if Ventana.wm_state() == 'normal':
        Ventana.overrideredirect(True)

Ventana = tk.Tk()
Ventana.geometry("300x200")

# Botón para minimizar
boton = tk.Button(Ventana, text="Minimizar", command=lambda: miniVen(None))
boton.pack(pady=20)

# Conectar el evento de cambio de estado con la función on_state_change
Ventana.bind("<Map>", on_state_change)
Ventana.bind("<Unmap>", on_state_change)

Ventana.mainloop()
