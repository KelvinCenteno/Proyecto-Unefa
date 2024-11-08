import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os

# Crear la ventana principal
ventana2 = tk.Tk()
ventana2.title("SISTEMA DE INVENTARIO PARA BIENES NACIONALES")
ventana2.geometry("400x500")

#Para el manejo de cierre
def abrir_inicio():
    subprocess.Popen(["python", "inicio.py" ])
    ventana2.destroy()

ventana2.protocol("WM_DELETE_WINDOW", abrir_inicio)

# Obtener dimensiones de la pantalla
ancho_pantalla = ventana2.winfo_screenwidth()
alto_pantalla = ventana2.winfo_screenheight()

# Calcular la posición x e y para centrar la ventana
x = (ancho_pantalla // 2) - (400 // 2)
y = (alto_pantalla // 2) - (500 // 2)

# Establecer la posición de la ventana
ventana2.geometry(f"400x500+{x}+{y}")

# Cargar la imagen de fondo
imagen_fondo = Image.open("Imagen1.jpg")
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un Canvas para la imagen de fondo
canvas = tk.Canvas(ventana2, width=400, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=imagen_fondo, anchor="nw")

# Crear y configurar las etiquetas y entradas sobre el Canvas
canvas.create_text(200, 50, text="REGISTRO DE BIENES", font=("Times New Roman", 18, "bold"), fill="white")
canvas.create_text(70, 100, text="NOMBRE PRODUCTO:", fill="white")

# Crear entradas (no pueden ser directas en el Canvas, se colocan encima)
texto2 = tk.Entry(ventana2)
canvas.create_window(200, 100, window=texto2)

canvas.create_text(100, 150, text="COLOR:", fill="white")
texto3 = tk.Entry(ventana2)
canvas.create_window(200, 150, window=texto3)

canvas.create_text(100, 200, text="UBICACION:", fill="white")
texto4 = tk.Entry(ventana2)
canvas.create_window(200, 200, window=texto4)

def Generar_codigo():
    # Datos para generar el QR
    datos = f"Producto: {texto2.get()}\nColor: {texto3.get()}\nUbicacion: {texto4.get()}"

    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(datos)
    qr.make(fit=True)
    # Crear una imagen del QR
    imagen_qr = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen QR en un archivo
    name = f"Producto{texto2.get()}Color{texto3.get()}Ubicacion{texto4.get()}"
    qr_path = name + ".png" 
    imagen_qr.save(qr_path)
    print(qr_path)

    # Crear una nueva ventana de Tkinter para mostrar el QR
    ventana_qr = tk.Toplevel(ventana2)
    ventana_qr.title("Código QR")
    ventana_qr.geometry("400x400")
    ventana_qr.resizable(False, False)  # Hacer que la ventana no se pueda redimensionar

    # Cargar y mostrar la imagen del QR en la nueva ventana
    imagen = Image.open(qr_path)
    imagen = imagen.resize((400, 400))  # Redimensionar la imagen para que ocupe toda la ventana
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen = tk.Label(ventana_qr, image=imagen_tk)
    etiqueta_imagen.image = imagen_tk  # Guardar una referencia de la imagen para evitar que se recolecte
    etiqueta_imagen.pack()

# Crear el botón de registro
bt_registro = tk.Button(ventana2, text="Registrar", command=Generar_codigo)
canvas.create_window(200, 250, window=bt_registro)

# Iniciar el bucle de la ventana principal
ventana2.mainloop()

