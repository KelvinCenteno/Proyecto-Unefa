import tkinter as tk
from tkinterweb import HtmlFrame

# Crear la ventana principal de tkinter
ventana = tk.Tk()
ventana.title("Visor de Página Web Completa")
ventana.geometry("1024x768")

# Crear el HtmlFrame
frame = HtmlFrame(ventana, messages_enabled=False)
frame.pack(fill="both", expand=True)

# Cargar una página web completa
url = "https://es.wallpapers.com/fondods-de-sitio-web"  # Reemplaza con la URL de la página web que deseas cargar
frame.load_website(url)

# Ejecutar la ventana principal
ventana.mainloop()
