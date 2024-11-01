import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont

Ventana = tk.Tk()
Ventana.title("Prueba")
Ventana.geometry("350x500")
Ventana.resizable(False, False)
#Ventana.overrideredirect(True)

Img_f = Image.open("Imagen1.jpg")
Img_f = Img_f.resize((Ventana.winfo_screenwidth(), Ventana.winfo_screenheight()))
fondo = ImageTk.PhotoImage(Img_f)
canvas = tk.Canvas(Ventana, width=Img_f.size[0], height=Img_f.size[1])
canvas.pack(fill= "both", expand=True)
canvas.create_image(0, 0, image=fondo, anchor="nw")

#Crear imagen del logo
Img_Co = Image.open("logo2.jpg")
an_Co= 100
alt_Co=100
Img_Co = Img_Co.resize((an_Co, alt_Co))
ConterTitle = ImageTk.PhotoImage(Img_Co)
canvas.create_image(180, 100, image= ConterTitle)

# Crear una imagen transparente para el texto
text_image2 = Image.new("RGBA", (220, 50), (255, 255, 255, 0))
draw2 = ImageDraw.Draw(text_image2)
font2 = ImageFont.truetype("arialbd.ttf", 16)
draw2.text((10, 10), "USUARIO", font=font2, fill=(255, 255, 255, 255))
# Convertir la imagen de texto a PhotoImage
text_photo2 = ImageTk.PhotoImage(text_image2)
# Añadir la imagen de texto al Canvas
canvas.create_image(242, 200, anchor=tk.CENTER, image=text_photo2)

# Crear una imagen transparente para el texto
text_image = Image.new("RGBA", (220, 50), (255, 255, 255, 0)) #Con esta linea se maneja el fondo del texto
draw = ImageDraw.Draw(text_image) #Con esta linea creamos un lienzo para dibujar
font = ImageFont.truetype("arialbd.ttf", 16) #Con esta linea establecemos la fuente de escritura en el lienzo
draw.text((10, 10), "CONTRASEÑA", font=font, fill=(255, 255, 255, 255)) #Dibujamos el texto sobre el lienzo con la fuente establecida
# Convertir la imagen de texto a PhotoImage
text_photo = ImageTk.PhotoImage(text_image)
# Añadir la imagen de texto al Canvas
canvas.create_image(225, 290, anchor=tk.CENTER, image=text_photo)

Ventana.mainloop()