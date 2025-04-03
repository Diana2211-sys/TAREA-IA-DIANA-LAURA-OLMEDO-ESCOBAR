#pip install opencv-python ultralytics
#pip install opencv-python pandas numpy ultralytics
#pip install ultralytics


import cv2
import numpy as np
import pandas as pd
from ultralytics import YOLO
import time

# Cargar el modelo YOLOv8
model = YOLO("yolov8n.pt")  

# Inicializar la cámara
cap = cv2.VideoCapture(0)  

# Lista para almacenar detecciones
detections_list = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar objetos en la imagen
    results = model(frame)

    # Procesar los resultados y almacenarlos en pandas
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas del cuadro
            conf = float(box.conf[0])  # Confianza
            cls = int(box.cls[0])  # Clase detectada
            label = model.names[cls]  # Nombre del objeto detectado

            # Guardar en lista para DataFrame
            detections_list.append([label, conf, x1, y1, x2, y2, time.time()])

            # Dibujar el cuadro y la etiqueta en la imagen
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label}: {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostrar la imagen con detecciones
    cv2.imshow("Detección de Objetos", frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Convertir a DataFrame de pandas
df = pd.DataFrame(detections_list, columns=["Objeto", "Confianza", "X1", "Y1", "X2", "Y2", "Tiempo"])

# Guardar a CSV
df.to_csv("detecciones.csv", index=False)

# Mostrar estadística básica
print("\nResumen de detecciones:")
print(df.groupby("Objeto").agg({"Confianza": ["count", "mean"]}))

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
