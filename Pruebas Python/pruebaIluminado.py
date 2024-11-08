import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageDraw, ImageFont, ImageTk

class RoundedRectangleDrawer:
    def __init__(self, canvas, xy, radius, outline='black', line_width=1, position=(0, 0)):
        self.canvas = canvas
        self.xy = xy
        self.radius = radius
        self.outline = outline
        self.line_width = line_width
        self.position = position
        self.rect = None

    def display_on_canvas(self):
        x1, y1, x2, y2 = self.xy
        self.rect = self.canvas.create_oval(x1 + self.position[0], y1 + self.position[1],
                                            x2 + self.position[0], y2 + self.position[1],
                                            outline=self.outline, width=self.line_width)

    def update_color(self, new_color):
        self.canvas.itemconfig(self.rect, outline=new_color)

def highlight_image(event):
    global text_photo2_highlighted
    # Cambiar tamaño o iluminar la imagen
    highlighted_image = Image.new("RGBA", (500, 50), "blue")
    highlighted_draw = ImageDraw.Draw(highlighted_image)
    highlighted_draw.text((10, 10), "REGISTRO", font=font2, fill="black", align="center")
    text_photo2_highlighted = ImageTk.PhotoImage(highlighted_image)
    canvas.itemconfig(cons, image=text_photo2_highlighted)
    # Cambiar color del objeto drawer
    drawer.update_color('red')

def reset_image(event):
    global text_photo2
    # Restaurar la imagen original
    text_photo2 = ImageTk.PhotoImage(text_image2)
    canvas.itemconfig(cons, image=text_photo2)
    # Restaurar color del objeto drawer
    drawer.update_color('black')

# Crear la ventana principal
root = tk.Tk()
root.geometry("600x400")

# Crear y configurar el Canvas
canvas = Canvas(root, width=600, height=300, bg='white')
canvas.pack(pady=20)

# Crear el objeto RoundedRectangleDrawer y dibujar en el canvas
xy = (20, 20, 285, 80)
radius = 10
line_width = 2  # Grosor de la línea
position = (6, 200)
drawer = RoundedRectangleDrawer(canvas, xy, radius, outline='Black', line_width=line_width, position=position)
drawer.display_on_canvas()

# Crear la imagen de texto en el Canvas
text_image2 = Image.new("RGBA", (500, 50), (255, 255, 255, 0))
draw2 = ImageDraw.Draw(text_image2)
font2 = ImageFont.truetype("arialbd.ttf", 26)
draw2.text((10, 10), "REGISTRO", font=font2, fill=("black"), align="center")
text_photo2 = ImageTk.PhotoImage(text_image2)
cons = canvas.create_image(6, 200, anchor="nw", image=text_photo2)

# Asociar eventos al elemento de la imagen en el Canvas
canvas.tag_bind(cons, "<Enter>", highlight_image)
canvas.tag_bind(cons, "<Leave>", reset_image)

# Ejecutar la ventana principal
root.mainloop()
