import tkinter as tk
from tkinter import Canvas
import cv2
from PIL import Image, ImageTk

def update_frame():
    ret, frame = cap.read()
    if ret:
        print("Frame leído correctamente")
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
        canvas.imgtk = imgtk  # Mantener una referencia a la imagen
    else:
        print("Error al leer el frame")
    root.after(5, update_frame)  # Llamar a update_frame nuevamente después de 10 ms

# Configuración de la ventana principal
root = tk.Tk()
root.title("Reproductor de Vídeo")
canvas = Canvas(root, width=640, height=480)
canvas.pack()

# Cargar el vídeo
cap = cv2.VideoCapture('VideoLogo3.mp4')
if not cap.isOpened():
    print("Error al abrir el archivo de vídeo")

# Mostrar el primer frame en una ventana de OpenCV para depuración
ret, frame = cap.read()
if ret:
    cv2.imshow("Frame de depuración", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Iniciar la actualización de frames
update_frame()

# Ejecutar la aplicación
root.mainloop()

# Liberar el vídeo cuando se cierre la ventana
cap.release()