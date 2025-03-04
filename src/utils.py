import os, string, unicodedata, re
import os 
import sys
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomExecption
import dill

def save_object(file_path, obj):

    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomExecption(e, sys)
# Función para limpiar los textos
def cleaning_data(text):
    # Reemplazando parentesis y slash por espacios en blanco
    text = text.replace('(', ' ').replace(')', ' ')
    text = text.replace('/', ' ').replace(')', ' ')
    text = text.replace(':', ' ')


    clean_txt = "".join(char for char in text if char not in string.punctuation)
    
    # Normalizar el texto a ASCII
    text_normalized = unicodedata.normalize('NFKD', clean_txt).encode('ascii', 'ignore').decode('ascii')
    
    # Eliminar espacios adicionales y convertir a minúsculas
    text_cleaned = re.sub(r'\s{2,}', ' ', text_normalized).strip().lower()
    
    # Eliminar dígitos y palabras específicas (si no son útiles)
    text_cleaned = re.sub(r'^(\d+)\s|\d+(?=[a-zA-Z])', '', text_cleaned)  # Elimina números
    text_cleaned = re.sub(r'nmv', '', text_cleaned).strip()  # Elimina "nmv"
    
    return text_cleaned
