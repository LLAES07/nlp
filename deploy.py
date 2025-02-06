# deploy.py

import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from preprocessing import cleaning_data  # Asegúrate de tener este módulo con la función cleaning_data
from docx import Document  # Necesitas instalar python-docx: pip install python-docx
import pandas as pd 


max_sequence_len = 163  # Usado en entreanamiento

# 1. Cargar el modelo guardado
model = load_model('modelo_fis.h5')

# 2. Cargar el tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# 3. Cargar el label encoder
with open('label_encoder.pickle', 'rb') as handle:
    label_encoder = pickle.load(handle)

# Función para procesar un nuevo texto y obtener la predicción
def predict_text(text):
    # Limpieza del texto
    cleaned_text = cleaning_data(text)
    
    # Tokenización y padding
    tokenized_text = tokenizer.texts_to_sequences([cleaned_text])
    padded_text = pad_sequences(tokenized_text, maxlen=max_sequence_len, padding='pre')
    
    # Realizar la predicción
    prediction = model.predict(padded_text)
    
    # Obtener las 3 clases con mayor probabilidad
    top_3_indices = prediction[0].argsort()[-3:][::-1]
    top_3_labels = label_encoder.inverse_transform(top_3_indices)
    top_3_probabilities = prediction[0][top_3_indices]
    
    # Mostrar resultados
    print("Top 3 predicciones más probables:")
    for i in range(3):
        print(f"{i+1}. Clase: {top_3_labels[i]} - Probabilidad: {top_3_probabilities[i]:.2f}")

def predict_label(text):
    """
    Retorna la etiqueta (clase) con mayor probabilidad para un texto dado.
    """
    cleaned_text = cleaning_data(text)
    tokenized_text = tokenizer.texts_to_sequences([cleaned_text])
    padded_text = pad_sequences(tokenized_text, maxlen=max_sequence_len, padding='pre')
    prediction = model.predict(padded_text)
    top_index = prediction[0].argmax()
    predicted_label = label_encoder.inverse_transform([top_index])[0]
    return predicted_label

def extract_heading3_from_docx(docx_path):
    """
    Extrae y retorna un set de textos únicos que sean de estilo 'Heading 3' de un documento de Word.
    """
    document = Document(docx_path)
    headings = set()
    for paragraph in document.paragraphs:
        # Verifica que el párrafo tenga estilo y que sea 'Heading 3'
        if paragraph.style and paragraph.style.name == 'Heading 3':
            # Agregamos el texto limpio al set (esto eliminará duplicados)
            headings.add(paragraph.text.strip())
    return headings

# Ejemplo de uso
if __name__ == '__main__':
    # Nuevo texto para probar
    new_text = "Pide informe al tenor del recurso dentro de 05 días hábiles"
    predict_text(new_text)

    # -------------------------------
    # Nueva funcionalidad: Procesar un documento de Word
    # -------------------------------
    
    # Ruta al documento de Word (ajusta el nombre del archivo según corresponda)
    docx_path = "D:/Llanos/ED_05-02-2025.docx"
    
    # Extraer los títulos de nivel 3 únicos
    unique_headings = extract_heading3_from_docx(docx_path)
    
    # Lista para almacenar los resultados
    resultados = []
    
    # Para cada título extraído, se predice la etiqueta y se guarda el resultado
    for heading in unique_headings:
        etiqueta_predicha = predict_label(heading)
        resultados.append({'Título': heading, 'Etiqueta_Predicha': etiqueta_predicha})
    
    # Crear un DataFrame con los resultados
    df_resultados = pd.DataFrame(resultados)
    
    # Guardar el DataFrame en un archivo Excel
    output_excel = 'predicciones.xlsx'
    df_resultados.to_excel(output_excel, index=False)
    
    print(f"\nSe ha generado el archivo Excel '{output_excel}' con los resultados de las predicciones.")