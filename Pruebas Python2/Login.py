import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import subprocess
from tkinter import messagebox

Ventana = tk.Tk()
Ventana.title("Prueba")

def cerrar_ventana(event):
    Ventana.destroy()
    #Ventana.wm_iconify()

def cargar_usuarios(): 
    usuarios = {} 
    with open('usuarios.txt', 'r') as archivo: 
        for linea in archivo: 
            usuario, contrasena = linea.strip().split(',') 
            usuarios[usuario] = contrasena 
    return usuarios 
         
def registro():
    usuario = caja_usuario.get() 
    contrasena = caja_contra.get()
    if usuario in usuarios and usuarios[usuario] == contrasena: 
        with open('usuario_actual.txt', 'w') as archivo: 
            archivo.write(usuario)
        subprocess.run(['python','prueba4.py'])
        Ventana.destroy()
    else: 
        messagebox.showerror("Error", "Usuario o contraseña incorrectos") 
        
def validar_usuario(): 
    usuario = caja_usuario.get() 
    contrasena = caja_contra.get()
    if usuario in usuarios and usuarios[usuario] == contrasena: 
        subprocess.run(['python','prueba4.py'])
        Ventana.destroy()
    else: 
        messagebox.showerror("Error", "Usuario o contraseña incorrectos") 

usuarios = cargar_usuarios()

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
Ventana.resizable(False, False)
Ventana.overrideredirect(True)

# Crear el Canvas
canvas = tk.Canvas(Ventana, width=ancho_ventana, height=alto_ventana, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Cargar y redimensionar la imagen de fondo
Img_f = Image.open("Imagen1.jpg")
Img_f = Img_f.resize((ancho_ventana, alto_ventana))
fondo = ImageTk.PhotoImage(Img_f)
canvas.create_image(0, 0, image=fondo, anchor="nw")

# Crear imagen del logo
Img_Co = Image.open("logo2.jpg")
Img_Co = Img_Co.resize((100, 100))
ConterTitle = ImageTk.PhotoImage(Img_Co)
canvas.create_image(180, 100, image=ConterTitle)

# Crear imagen de texto "USUARIO"
text_image2 = Image.new("RGBA", (220, 50), (255, 255, 255, 0))
draw2 = ImageDraw.Draw(text_image2)
font2 = ImageFont.truetype("arialbd.ttf", 16)
draw2.text((10, 10), "USUARIO", font=font2, fill=(255, 255, 255, 255))
text_photo2 = ImageTk.PhotoImage(text_image2)
canvas.create_image(242, 200, anchor=tk.CENTER, image=text_photo2)

#Caja de Texto Usuario
caja_usuario = tk.Entry(Ventana)
canvas.create_window(180, 220, window=caja_usuario)

# Crear imagen de texto "CONTRASEÑA"
text_image = Image.new("RGBA", (220, 50), (255, 255, 255, 0))
draw = ImageDraw.Draw(text_image)
font = ImageFont.truetype("arialbd.ttf", 16)
draw.text((10, 10), "CONTRASEÑA", font=font, fill=(255, 255, 255, 255))
text_photo = ImageTk.PhotoImage(text_image)
canvas.create_image(225, 280, anchor=tk.CENTER, image=text_photo)

#Caja de Texto Usuario
caja_contra = tk.Entry(Ventana, show="*")
canvas.create_window(180, 310, window=caja_contra)

# Crear imagen de texto para soporte técnico
text_image3 = Image.new("RGBA", (400, 50), (255, 255, 255, 0))
draw3 = ImageDraw.Draw(text_image3)
font3 = ImageFont.truetype("arial.ttf", 10)
draw3.text((10, 10), "En caso de algun inconveniente contactarse con Soporte Tecnico", font=font3, fill=(255, 255, 255, 255))
text_photo3 = ImageTk.PhotoImage(text_image3)
canvas.create_image(215, 450, anchor=tk.CENTER, image=text_photo3)

# Crear imagen de texto "X" para cerrar la ventana
text_image4 = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
draw4 = ImageDraw.Draw(text_image4)
font4 = ImageFont.truetype("arialbd.ttf", 16)
draw4.text((10, 10), "X", font=font4, fill=(255, 255, 255, 255))
text_photo4 = ImageTk.PhotoImage(text_image4)
imagen_id = canvas.create_image(300, 5, anchor="nw", image=text_photo4)
canvas.tag_bind(imagen_id, "<Button-1>", cerrar_ventana)


# Crear botón "INGRESAR"
btn = tk.Button(Ventana, text="INGRESAR", bg="red4", fg="white", relief="raised", padx=10, pady=2, cursor="hand2",
                 highlightcolor="black", highlightbackground="white", borderwidth=5, highlightthickness=2, command=registro)

canvas.create_window(185, 380, window=btn)

Ventana.mainloop()
