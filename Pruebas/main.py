import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont

Ventana = tk.Tk()
Ventana.title("Prueba")
# Definir el tamaño de la ventana
ancho_ventana = 350
alto_ventana = 500

# Obtener el tamaño de la pantalla
ancho_pantalla = Ventana.winfo_screenwidth()
alto_pantalla = Ventana.winfo_screenheight()

# Calcular la posición x, y para centrar la ventana
posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
posicion_y = int((alto_pantalla / 2) - (alto_ventana / 2))
# Ajustar las dimensiones y la posición de la ventana
Ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
#Ventana.geometry("350x500")
Ventana.resizable(False, False)
Ventana.overrideredirect(True)


Img_f = Image.open("Imagen1.jpg")
Img_f = Img_f.resize((Ventana.winfo_screenwidth(), Ventana.winfo_screenheight()))
fondo = ImageTk.PhotoImage(Img_f)
canvas = tk.Canvas(Ventana, width=Img_f.size[0], height=Img_f.size[0],highlightthickness=0) #highlightthickness=0 elimina el borde resaltado del canvas.
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

text_image3 = Image.new("RGBA", (400, 50), (255, 255, 255, 0))
draw3 = ImageDraw.Draw(text_image3)
font3 = ImageFont.truetype("arial.ttf", 10)
draw3.text((10, 10), "En caso de algun inconveniente contactarse con Soporte Tecnico", font=font3, fill=(255, 255, 255, 255))
# Convertir la imagen de texto a PhotoImage
text_photo3 = ImageTk.PhotoImage(text_image3)
# Añadir la imagen de texto al Canvas
canvas.create_image(215, 450, anchor=tk.CENTER, image=text_photo3)

def cerrar_ventana(event):
    Ventana.destroy()

text_image4 = Image.new("RGBA", (400, 50), (255, 255, 255, 0))
draw4 = ImageDraw.Draw(text_image4)
font4 = ImageFont.truetype("arialbd.ttf", 16)
draw4.text((10, 10), "X", font=font4, fill=(255, 255, 255, 255))
# Convertir la imagen de texto a PhotoImage
text_photo4 = ImageTk.PhotoImage(text_image4)

#canvas.create_image(520, 20, anchor=tk.CENTER, image=text_photo4)
imagen_id = canvas.create_image(300, 5, anchor="nw", image=text_photo4) 
canvas.tag_bind(imagen_id, "<Button-1>", cerrar_ventana)

btn = tk.Button(Ventana, text="INGRESAR", bg="red4", fg="white", relief="raised", padx=10, pady=2, cursor="hand2", 
                highlightcolor="black", highlightbackground="white", borderwidth=5, highlightthickness=2)
canvas.create_window(185, 380, window=btn)

Ventana.mainloop()

