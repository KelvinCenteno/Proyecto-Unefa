import tkinter as tk
from tkinter import Canvas, Menu, ttk
import cv2, subprocess
from PIL import Image, ImageTk, ImageDraw, ImageFont
from rounded_rectangle_drawer import RoundedRectangleDrawer

# Configuración de la ventana principal
root = tk.Tk()
root.title("Reproductor de Vídeo")
# Definir el tamaño de la ventana
ancho_ventana = root.winfo_screenwidth() - 80
alto_ventana = root.winfo_screenheight() - 50

# Obtener el tamaño de la pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

# Calcular la posición x, y para centrar la ventana
posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
posicion_y = int((alto_pantalla / 2) - (alto_ventana / 1.9))

# Ajustar las dimensiones y la posición de la ventana
root.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
root.resizable(False, False)
root.overrideredirect(True)

# Crear el Canvas en la ventana principal
canvas = tk.Canvas(root, width=ancho_ventana, height=alto_ventana, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Cargar y redimensionar la imagen de fondo
Img_f = Image.open("Imagen1.jpg")
Img_f = Img_f.resize((ancho_pantalla, alto_pantalla))
fondo = ImageTk.PhotoImage(Img_f)
canvas.create_image(0, 0, image=fondo, anchor="nw")

# Función para mostrar el menú desplegable
def show_menu(event):
    menu.post(event.x_root, event.y_root)

def on_select(option):
    if option == "Opción 1":
        print("Seleccionaste la uno")
    elif option == "Opción 2":
        print("Seleccionaste la dos")
    else:
        print("Seleccionaste la tres")

text_image1 = Image.new("RGBA", (ancho_ventana, 120), (255, 255, 255, 0))
draw1 = ImageDraw.Draw(text_image1)
font1 = ImageFont.truetype("arialbd.ttf", 16)
draw1.text((10, 10), "SISTEMA DE\nINVENTARIO PARA\nBIENES NACIONALES\n(SIBIN)", font=font1, fill=(255, 255, 255, 255), align="center")
text_photo1 = ImageTk.PhotoImage(text_image1)
canvas.create_image(787, 90, anchor=tk.CENTER, image=text_photo1)

with open('usuario_actual.txt', 'r') as archivo:
    usuario = archivo.read().strip()

usuario_image40 = Image.new("RGBA", (300, 50), (255, 255, 255, 0))
Us_draw40 = ImageDraw.Draw(usuario_image40)
Us_font40 = ImageFont.truetype("arialbd.ttf", 16)
Us_draw40.text((10, 10), "¡Bienvenido Usuario " + usuario + "!", font=Us_font40, fill=(255, 255, 255, 255))
Us_photo40 = ImageTk.PhotoImage(usuario_image40)
Us_id = canvas.create_image(ancho_ventana - 300, 5, anchor="nw", image=Us_photo40)

# Crear imagen de texto "X" para cerrar la ventana
text_image40 = Image.new("RGBA", (60, 50), (255, 255, 255, 0))
draw40 = ImageDraw.Draw(text_image40)
font40 = ImageFont.truetype("arialbd.ttf", 16)
draw40.text((10, 10), "X", font=font40, fill=(255, 255, 255, 255))
text_photo40 = ImageTk.PhotoImage(text_image40)
imagen_id = canvas.create_image(ancho_ventana - 40, 5, anchor="nw", image=text_photo40)
canvas.tag_bind(imagen_id, "<Button-1>", lambda event: root.destroy())

# Crear imagen del logo
Img_Co = Image.open("logo2.jpg")
Img_Co = Img_Co.resize((100, 100))
ConterTitle = ImageTk.PhotoImage(Img_Co)
canvas.create_image(60, 80, image=ConterTitle)

def highlight_image(event):
    global text_photo2_highlighted
    highlighted_image = Image.new("RGBA", (160, 50), (255, 255, 255, 0))
    highlighted_draw = ImageDraw.Draw(highlighted_image)
    highlighted_draw.text((10, 10), "REGISTRO", font=font2, fill="green", align="center")
    text_photo2_highlighted = ImageTk.PhotoImage(highlighted_image)
    canvas.itemconfig(uno, image=text_photo2_highlighted)
    drawer.update_color('green')
    canvas.config(cursor="hand2")

def reset_image(event):
    global text_photo2
    # Restaurar la imagen original
    text_photo2 = ImageTk.PhotoImage(text_image2)
    canvas.itemconfig(uno, image=text_photo2)
    drawer.update_color('white')
    canvas.config(cursor="")
#Iluminación Asignarlo
def highlight_asig(event):
    global text_photo3_highlighted
    highlighted_image = Image.new("RGBA", (200, 50), (255, 255, 255, 0))
    highlighted_draw = ImageDraw.Draw(highlighted_image)
    highlighted_draw.text((10, 10), "ASIGNACIÓN", font=font3, fill="green", align="center")
    text_photo3_highlighted = ImageTk.PhotoImage(highlighted_image)
    canvas.itemconfig(asig, image=text_photo3_highlighted)
    drawer1.update_color('green')
    canvas.config(cursor="hand2")

def reset_asig(event):
    global text_photo3
    # Restaurar la imagen original
    text_photo3 = ImageTk.PhotoImage(text_image3)
    canvas.itemconfig(asig, image=text_photo3)
    drawer1.update_color('white')
    canvas.config(cursor="")

#Iluminación Consulta
def highlight_consulta(event):
    global text_photo4_highlighted
    highlighted_image = Image.new("RGBA", (200, 50), (255, 255, 255, 0))
    highlighted_draw = ImageDraw.Draw(highlighted_image)
    highlighted_draw.text((10, 10), "CONSULTA", font=font4, fill="green", align="center")
    text_photo4_highlighted = ImageTk.PhotoImage(highlighted_image)
    canvas.itemconfig(cons, image=text_photo4_highlighted)
    drawer2.update_color('green')
    canvas.config(cursor="hand2")

def reset_consulta(event):
    global text_photo4
    # Restaurar la imagen original
    text_photo4 = ImageTk.PhotoImage(text_image4)
    canvas.itemconfig(cons, image=text_photo4)
    drawer2.update_color('white')
    canvas.config(cursor="")

#iluminado desincorporación
def highlight_desincorp(event):
    global text_photo20_highlighted
    highlighted_image = Image.new("RGBA", (500, 50), (255, 255, 255, 0))
    highlighted_draw = ImageDraw.Draw(highlighted_image)
    highlighted_draw.text((10, 10), "DESINCORPORACIÓN", font=font20, fill="green", align="center")
    text_photo20_highlighted = ImageTk.PhotoImage(highlighted_image)
    canvas.itemconfig(des, image=text_photo20_highlighted)
    drawer3.update_color('green')
    canvas.config(cursor="hand2")

def reset_desincorp(event):
    global text_photo20
    # Restaurar la imagen original
    text_photo20 = ImageTk.PhotoImage(text_image20)
    canvas.itemconfig(des, image=text_photo20)
    drawer3.update_color('white')
    canvas.config(cursor="")

#iluminado reporte
def highlight_reporte(event):
    global text_photo21_highlighted
    highlighted_image = Image.new("RGBA", (160, 50), (255, 255, 255, 0))
    highlighted_draw = ImageDraw.Draw(highlighted_image)
    highlighted_draw.text((10, 10), "REPORTE", font=font21, fill="green", align="center")
    text_photo21_highlighted = ImageTk.PhotoImage(highlighted_image)
    canvas.itemconfig(rep, image=text_photo21_highlighted)
    drawer4.update_color('green')
    canvas.config(cursor="hand2")

def reset_reporte(event):
    global text_photo21
    # Restaurar la imagen original
    text_photo21 = ImageTk.PhotoImage(text_image21)
    canvas.itemconfig(rep, image=text_photo21)
    drawer4.update_color('white')
    canvas.config(cursor="")

# CREAR LISTA DE BOTONES LATERALES
xy = (20, 20, 285, 80)
radius = 10
line_width = 3  # Grosor de la línea
position = (6, 200)
# Crear el objeto RoundedRectangleDrawer y dibujar en el canvas

drawer = RoundedRectangleDrawer(canvas, xy, radius, outline='white', line_width=line_width, position=position)
drawer.display_on_canvas()

text_image2 = Image.new("RGBA", (160, 50), (255, 255, 255, 0))
draw2 = ImageDraw.Draw(text_image2)
font2 = ImageFont.truetype("arialbd.ttf", 26)
draw2.text((10, 10), "REGISTRO", font=font2, fill=(255, 255, 255, 255), align="center")
text_photo2 = ImageTk.PhotoImage(text_image2)

uno = canvas.create_image(160, 250, anchor=tk.CENTER, image=text_photo2)

canvas.tag_bind(uno, "<Enter>", highlight_image) 
canvas.tag_bind(uno, "<Leave>", reset_image)

def asignacion(event):
    subprocess.run(['python','asignacion.py'])

def consulta_Asig():
    subprocess.run(['python','consulta_asig.py'])

def consulta_Disp():
    subprocess.run(['python','consulta_asig.py'])

#def on_enter(event):
#def on_leave(event):
#canvas.tag_bind(uno, "<Enter>", on_enter)
#canvas.tag_bind(uno, "<Leave>", on_leave)

xy1 = (20, 20, 285, 80)
radius1 = 10
line_width1 = 3  # Grosor de la línea
position1 = (6, 300)
# Crear el objeto RoundedRectangleDrawer y dibujar en el canvas
drawer1 = RoundedRectangleDrawer(canvas, xy1, radius1, outline='white', line_width=line_width1, position=position1)
drawer1.display_on_canvas()

text_image3 = Image.new("RGBA", (200, 50), (255, 255, 255, 0))
draw3 = ImageDraw.Draw(text_image3)
font3 = ImageFont.truetype("arialbd.ttf", 26)
draw3.text((10, 10), "ASIGNACIÓN", font=font2, fill=(255, 255, 255, 255), align="center")
text_photo3 = ImageTk.PhotoImage(text_image3)
asig =  canvas.create_image(65, 325, anchor="nw", image=text_photo3)

canvas.tag_bind(asig, "<Button-1>", asignacion)
canvas.tag_bind(asig, "<Enter>", highlight_asig)
canvas.tag_bind(asig, "<Leave>", reset_asig)

xy2 = (20, 20, 285, 80)
radius2 = 10
line_width2 = 3  # Grosor de la línea
position2 = (6, 400)
# Crear el objeto RoundedRectangleDrawer y dibujar en el canvas
drawer2 = RoundedRectangleDrawer(canvas, xy2, radius2, outline='white', line_width=line_width2, position=position2)
drawer2.display_on_canvas()

def show_menu2(event):
    menu2.post(event.x_root, event.y_root)
    
menu2 = Menu(root, tearoff=0, bg="firebrick4", fg="white")
menu2.configure(font=("arial", 18 ))
menu2.add_command(label="Bienes Disponibles", command=consulta_Disp)
menu2.add_separator()
menu2.add_command(label="Bienes Asignados", command=consulta_Asig)

text_image4 = Image.new("RGBA", (200, 50), (255, 255, 255, 0))
draw4 = ImageDraw.Draw(text_image4)
font4 = ImageFont.truetype("arialbd.ttf", 26)
draw4.text((10, 10), "CONSULTA", font=font4, fill=(255, 255, 255, 255), align="center")
text_photo4 = ImageTk.PhotoImage(text_image4)
cons = canvas.create_image(280, 450, anchor= "e", image=text_photo4)
#bad anchor position "left": must be n, ne, e, se, s, sw, w, nw, or center
canvas.tag_bind(cons, "<Button-1>", show_menu2)
canvas.tag_bind(cons, "<Enter>", highlight_consulta)
canvas.tag_bind(cons, "<Leave>", reset_consulta)

xy3 = (20, 20, 285, 80)
radius3 = 10
line_width3 = 3  # Grosor de la línea
position3 = (6, 500)
# Crear el objeto RoundedRectangleDrawer y dibujar en el canvas
drawer3 = RoundedRectangleDrawer(canvas, xy3, radius3, outline='white', line_width=line_width3, position=position3)
drawer3.display_on_canvas()

text_image20 = Image.new("RGBA", (500, 50), (255, 255, 255, 0))
draw20 = ImageDraw.Draw(text_image20)
font20 = ImageFont.truetype("arialbd.ttf", 24)
draw20.text((10, 10), "DESINCORPORACIÓN", font=font20, fill=(255, 255, 255, 255), align="center")
text_photo20 = ImageTk.PhotoImage(text_image20)
des = canvas.create_image(270, 550, anchor=tk.CENTER, image=text_photo20)

canvas.tag_bind(des, "<Enter>", highlight_desincorp)
canvas.tag_bind(des, "<Leave>", reset_desincorp)

xy4 = (20, 20, 285, 80)
radius4 = 10
line_width4 = 3  # Grosor de la línea
position4 = (6, 600)
# Crear el objeto RoundedRectangleDrawer y dibujar en el canvas
drawer4 = RoundedRectangleDrawer(canvas, xy4, radius4, outline='white', line_width=line_width4, position=position4)
drawer4.display_on_canvas()

text_image21 = Image.new("RGBA", (160, 50), (255, 255, 255, 0))
draw21 = ImageDraw.Draw(text_image21)
font21 = ImageFont.truetype("arialbd.ttf", 26)
draw21.text((10, 10), "REPORTE", font=font21, fill=(255, 255, 255, 255), align="center")
text_photo21 = ImageTk.PhotoImage(text_image21)
rep = canvas.create_image(160, 650, anchor=tk.CENTER, image=text_photo21)

canvas.tag_bind(rep, "<Enter>", highlight_reporte)
canvas.tag_bind(rep, "<Leave>", reset_reporte)
canvas.tag_bind(rep,"<Button-1>", lambda event: root.destroy())
# Añadir líneas y decoraciones
canvas.create_line(330, 0, 330, alto_ventana, fill="white", width=2, dash=(9,3))

def crear_text_image(width, height, color):
    text_image = Image.new("RGBA", (width, height), color)
    return ImageTk.PhotoImage(text_image)

text_photo5 = crear_text_image(24, alto_ventana, (255, 112, 0, 10))
text_photo6 = crear_text_image(22, alto_ventana, (255, 112, 0, 10))
text_photo7 = crear_text_image(20, alto_ventana, (255, 112, 0, 10))
text_photo8 = crear_text_image(18, alto_ventana, (255, 112, 0, 10))
text_photo9 = crear_text_image(16, alto_ventana, (255, 112, 0, 10))
text_photo10 = crear_text_image(14, alto_ventana, (255, 112, 0, 10))

canvas.create_image(320, 0, anchor="nw", image=text_photo5)
canvas.create_image(321, 0, anchor="nw", image=text_photo6)
canvas.create_image(322, 0, anchor="nw", image=text_photo7)
canvas.create_image(323, 0, anchor="nw", image=text_photo8)
canvas.create_image(324, 0, anchor="nw", image=text_photo9)
canvas.create_image(325, 0, anchor="nw", image=text_photo10)

def inicio():
    root.destroy()
    subprocess.run(['python','Login.py'])
   
#def boton_video():
    
# Crear el menú desplegable
img_close = Image.open("Cerrar_Sección.png")
img_close = img_close.resize((20, 20))
icon_close = ImageTk.PhotoImage(img_close)

img_contra = Image.open("Seguridad.png")
img_contra = img_contra.resize((25, 18))
icon_contra = ImageTk.PhotoImage(img_contra)

menu = Menu(root, tearoff=0)
menu.add_command(label="   Opción 1", command=lambda: on_select("Opción 1"),)
menu.add_command(label="Contraseña", command=lambda: on_select("Opción 2"), image=icon_contra, 
                 compound=tk.LEFT)
menu.add_separator()
menu.add_command(image=icon_close, command=inicio, compound=tk.BOTTOM, 
                 label="Cerrar Sección", foreground="red")

# Crear imagen del logo del usuario
Img_Co2 = Image.open("Usuario2.png")
Img_Co2 = Img_Co2.resize((30, 30))
ConterTitle2 = ImageTk.PhotoImage(Img_Co2)
usuario = canvas.create_image(ancho_ventana - 60, 20, image=ConterTitle2)

# Vincular el evento de clic a la imagen del usuario
canvas.tag_bind(usuario, "<Button-1>", show_menu)

# Ruta del vídeo
video_path = 'VideoLogo5.mp4'
# Cargar el vídeo
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error al abrir el archivo de vídeo")

def update_frame():
    global cap, imgtk
    ret, frame = cap.read()
    if not ret:  # Si no se puede leer el frame, reiniciar el vídeo
        cap.release()
        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        canvas.create_image(ancho_ventana/3, alto_ventana/3, anchor=tk.NW, image=imgtk)
        canvas.imgtk = imgtk  # Mantener una referencia a la imagen
    root.after(5, update_frame)  # Ajustar el intervalo de tiempo para mejorar la fluidez

# Iniciar la actualización de frames

update_frame()

# Crear imagen del logo del usuario
Img_Home = Image.open("Home.png")
Img_Home = Img_Home.resize((30, 30))
Home = ImageTk.PhotoImage(Img_Home)
usuario2 = canvas.create_image(420, 26, image=Home)
#canvas.tag_bind(usuario2, "<Button-1>", Inicio_video)

#canvas.tag_bind(asig, "<Button-1>", Inicio_video)


root.mainloop()

# Liberar el vídeo cuando se cierre la ventana
cap.release()
