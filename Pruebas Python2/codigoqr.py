import qrcode
import tkinter as tk
from PIL import Image, ImageTk

# Datos para generar el QR
datos = "Este es un ejemplo de texto para generar un código QR"

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
imagen_qr.save("codigo_qr.png")

# Crear una ventana de Tkinter para mostrar el QR
root = tk.Tk()
root.title("Código QR")

# Cargar y mostrar la imagen del QR en la ventana
imagen = Image.open("codigo_qr.png")
imagen_tk = ImageTk.PhotoImage(imagen)
etiqueta_imagen = tk.Label(root, image=imagen_tk)
etiqueta_imagen.pack()

# Iniciar el bucle de la ventana
root.mainloop()
