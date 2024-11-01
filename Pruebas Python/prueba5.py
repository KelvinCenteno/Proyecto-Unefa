import tkinter as tk
from rounded_rectangle_drawer import RoundedRectangleDrawer

# Crear una ventana y un canvas de Tkinter
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Coordenadas del rectángulo y radio de las esquinas
xy = (20, 20, 200, 60)
radius = 10
line_width = 2  # Grosor de la línea

# Crear el objeto RoundedRectangleDrawer y dibujar en el canvas
drawer = RoundedRectangleDrawer(canvas, xy, radius, outline='white', line_width=line_width)
drawer.display_on_canvas()

root.mainloop()
