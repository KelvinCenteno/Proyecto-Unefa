import cv2

# Cargar el vídeo
cap = cv2.VideoCapture('VideoLogo.mp4')
if not cap.isOpened():
    print("Error al abrir el archivo de vídeo")

# Obtener la resolución original
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Resolución original: {width}x{height}")

# Reducir la resolución
new_width = 920
new_height = 450
print(f"Resolución reducida: {new_width}x{new_height}")

# Crear un nuevo archivo de vídeo con la resolución reducida
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('VideoLogo6.mp4', fourcc, 20.0, (new_width, new_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame_resized = cv2.resize(frame, (new_width, new_height)) 
    out.write(frame_resized)

cap.release()
out.release()
print("Vídeo reducido guardado como 'ruta/al/video_reducido.mp4'")
