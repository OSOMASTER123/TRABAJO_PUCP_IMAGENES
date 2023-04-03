IA PUCP - Diplomatura de Desarrollo de Aplicaciones de Inteligencia Artificial
DESARROLLO EN APLICACIONES CON VISIÓN ARTIFICIAL PUCP
============
Implementación de un sistema de detección de cascos para seguridad en el sector industrial mediante el uso de la arquitectura YOLO y el dispositivo Jetson Nano
----------------------------------
Integrantes:
AÑANCA ARANGO , PEDRO CHRISTIAN
DÍAZ VILLANUEVA, JULIO LEONARDO

----------------------------------
Contenido
Introducción
Entrenamiento del modelo
Implementación en Jetson Nano
Uso
Introducción
Este proyecto tiene como objetivo detectar si una persona lleva casco o no usando un modelo de YOLOv5. El uso de cascos es esencial en muchos entornos laborales, y este proyecto puede ayudar a garantizar la seguridad en el lugar de trabajo.

El proyecto se divide en dos partes principales:

Entrenamiento del modelo YOLOv5 con un conjunto de datos de Kaggle.
Implementación del modelo en una Jetson Nano de NVIDIA para la detección en tiempo real.
Entrenamiento del modelo
Para entrenar el modelo, utilizamos un conjunto de datos de Kaggle que contiene imágenes etiquetadas de personas con y sin casco. Puedes encontrar el conjunto de datos aquí: [enlace al conjunto de datos de Kaggle]

Para entrenar el modelo YOLOv5, sigue estos pasos:

Clona el repositorio YOLOv5 de Ultralytics:
git clone https://github.com/ultralytics/yolov5.git
cd yolov5

Prepara tu conjunto de datos en el formato YOLOv5. Divide tus imágenes y anotaciones en carpetas train y val, y crea un archivo data.yaml que incluya la información de las rutas y las clases.

Entrena el modelo con el siguiente comando:
python train.py --img 640 --batch 16 --epochs 100 --data data.yaml --weights yolov5s.pt --cache

Ajusta los parámetros según tus necesidades y recursos disponibles. Después del entrenamiento, encontrarás tus archivos de pesos entrenados en el directorio runs/train.

Implementación en Jetson Nano
Una vez que hayas entrenado el modelo, puedes implementarlo en una Jetson Nano de NVIDIA para la detección en tiempo real. Sigue estos pasos:

Configura tu Jetson Nano y conecta una cámara compatible.
Instala las dependencias necesarias en la Jetson Nano:
pip install torch torchvision
Transfiere el archivo de pesos entrenado .pt a tu Jetson Nano.
Utiliza el código de detección en tiempo real proporcionado en una respuesta anterior, y modifica la ruta del archivo de pesos y las clases según sea necesario.

Uso
Una vez que hayas implementado el modelo en tu Jetson Nano, ejecuta el script para comenzar la detección en tiempo real. El programa mostrará un video en vivo con cuadros delimitadores y etiquetas que indican si una persona lleva casco o no.

Si deseas detener el programa, presiona 'q' en la ventana del video en vivo.

Conclusión
Este proyecto demuestra cómo entrenar e implementar un modelo YOLOv5 en una Jetson


----------------------------------
Referencias:
1)https://towardsdatascience.com/how-to-train-a-custom-object-detection-model-with-yolo-v5-917e9ce13208
2) https://github.com/DavidReveloLuna/YoloV5
