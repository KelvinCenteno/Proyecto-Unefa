import tkinter as tk
from tkinter import Canvas
import cv2
from PIL import Image, ImageTk, ImageDraw, ImageFont
import subprocess 

Ventana2 = tk.Tk()
Ventana2.title("Prueba")

def cerrar_ventana(event):
    Ventana2.destroy()
    #Ventana.wm_iconify()
  
# Definir el tamaño de la ventana
ancho_ventana = Ventana2.winfo_screenwidth() - 80
alto_ventana = Ventana2.winfo_screenheight() - 50

# Obtener el tamaño de la pantalla
ancho_pantalla = Ventana2.winfo_screenwidth()
alto_pantalla = Ventana2.winfo_screenheight()

# Calcular la posición x, y para centrar la ventana
posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
posicion_y = int((alto_pantalla / 2) - (alto_ventana / 1.9))

# Ajustar las dimensiones y la posición de la ventana
Ventana2.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
Ventana2.resizable(False, False)
Ventana2.overrideredirect(True)

# Crear el Canvas
canvas = tk.Canvas(Ventana2, width=ancho_ventana, height=alto_ventana, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Cargar y redimensionar la imagen de fondo
Img_f = Image.open("Imagen1.jpg")
Img_f = Img_f.resize((ancho_ventana, alto_ventana))
fondo = ImageTk.PhotoImage(Img_f)
canvas.create_image(0, 0, image=fondo, anchor="nw")

Ub_close = ancho_pantalla - 120
# Crear imagen de texto "X" para cerrar la ventana
text_image4 = Image.new("RGBA", (60, 50), (255, 255, 255, 0))
draw4 = ImageDraw.Draw(text_image4)
font4 = ImageFont.truetype("arialbd.ttf", 16)
draw4.text((10, 10), "X", font=font4, fill=(255, 255, 255, 255))
text_photo4 = ImageTk.PhotoImage(text_image4)
imagen_id = canvas.create_image(Ub_close, 5, anchor="nw", image=text_photo4)
canvas.tag_bind(imagen_id, "<Button-1>", cerrar_ventana)

# Crear imagen del logo
Img_Co = Image.open("logo2.jpg")
Img_Co = Img_Co.resize((100, 100))
ConterTitle = ImageTk.PhotoImage(Img_Co)
canvas.create_image(170, 100, image=ConterTitle)

canvas.create_line(272, 0, 272, alto_pantalla, fill="white", width=2, dash=(8,2))

text_image5 = Image.new("RGBA", (24, alto_pantalla), (255, 112, 0, 10))
text_photo5 = ImageTk.PhotoImage(text_image5)
imagen_id2 = canvas.create_image(260, 0, anchor="nw", image=text_photo5)

text_image6 = Image.new("RGBA", (22, alto_pantalla), (255, 112, 0, 10))
text_photo6 = ImageTk.PhotoImage(text_image6)
imagen_id3 = canvas.create_image(261, 0, anchor="nw", image=text_photo6)

text_image7 = Image.new("RGBA", (20, alto_pantalla), (255, 112, 0, 10))
text_photo7 = ImageTk.PhotoImage(text_image7)
imagen_id4 = canvas.create_image(262, 0, anchor="nw", image=text_photo7)

text_image8 = Image.new("RGBA", (18, alto_pantalla), (255, 112, 0, 10))
text_photo8 = ImageTk.PhotoImage(text_image8)
imagen_id5 = canvas.create_image(263, 0, anchor="nw", image=text_photo8)

text_image9 = Image.new("RGBA", (16, alto_pantalla), (255, 112, 0, 10))
text_photo9 = ImageTk.PhotoImage(text_image9)
imagen_id6 = canvas.create_image(264, 0, anchor="nw", image=text_photo9)

text_image10 = Image.new("RGBA", (14, alto_pantalla), (255, 112, 0, 10))
text_photo10 = ImageTk.PhotoImage(text_image10)
imagen_id7 = canvas.create_image(265, 0, anchor="nw", image=text_photo10)

def update_frame():
    global cap
    ret, frame = cap.read()
    if not ret:  # Si no se puede leer el frame, reiniciar el vídeo
        cap.release()
        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
        canvas.imgtk = imgtk  # Mantener una referencia a la imagen
    root.after(15, update_frame)  # Ajustar el intervalo de tiempo para mejorar la fluidez

# Configuración de la ventana principal
root = tk.Tk()
root.title("Reproductor de Vídeo")
canvas = Canvas(root, width=640, height=480)
canvas.pack()

# Ruta del vídeo
video_path = 'VideoLogo3.mp4'

# Cargar el vídeo
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error al abrir el archivo de vídeo")

# Iniciar la actualización de frames
update_frame()

#Ventana2.deiconify(True)

Ventana2.mainloop()

# Liberar el vídeo cuando se cierre la ventana
cap.release()