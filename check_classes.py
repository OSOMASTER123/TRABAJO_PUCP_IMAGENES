# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 14:52:08 2023

@author: Hubble
"""
import torch

def get_classes(model_path):
    # Cargar el modelo YOLOv5
    model = torch.load(model_path, map_location=torch.device('cpu'))

    # Obtener la lista de nombres de clases
    class_names = model['model'].names

    return class_names

# Reemplaza 'weights/yolov5s.pt' con la ruta de tu modelo .pt
model_path = '/content/yolov5/runs/train/exp2/weights/last.pt'
class_names = get_classes(model_path)

print(f'Número de clases: {len(class_names)}')
print(f'Nombres de las clases: {class_names}')