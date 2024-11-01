import tkinter as tk
from tkinter import Canvas
import cv2
from PIL import Image, ImageTk

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

# Ejecutar la aplicación
root.mainloop()

# Liberar el vídeo cuando se cierre la ventana
cap.release()