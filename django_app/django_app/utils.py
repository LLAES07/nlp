import os, string, unicodedata, re
from pathlib import Path
import pickle 
from tensorflow.keras.preprocessing.sequence import pad_sequences
import nltk
from nltk.corpus import stopwords

# Descargar las stopwords si no lo has hecho antes
nltk.download('stopwords')

# Obtener las stopwords en español
stop_words_es = set(stopwords.words('spanish'))


DJANGO_APP_DIR = Path(__file__).resolve().parent.parent  # donde está settings.py
PROJECT_ROOT = DJANGO_APP_DIR.parent  

max_sequence_len = 120  # Usado en entreanamiento

MODEL_PATH = PROJECT_ROOT / 'artifacts' / 'model.pkl'

TOKENIZER_PATH = PROJECT_ROOT / 'artifacts' / 'tokenizer.pkl'

LABEL_ENCODER = PROJECT_ROOT / 'artifacts' / 'label_encoder.pkl'

# Función para limpiar los textos


with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)


with open(TOKENIZER_PATH, 'rb') as f:
    tokenizer = pickle.load(f)
    
with open(LABEL_ENCODER, 'rb') as f:
    label_encoder = pickle.load(f)

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


def predict_label(text):
    """
    Retorna la etiqueta (clase) con mayor probabilidad para un texto dado.
    """
    cleaned_text = cleaning_data(text)

    words = cleaned_text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words_es]
    cleaned_no_stop = ' '.join(filtered_words)

    tokenized_text = tokenizer.texts_to_sequences([cleaned_no_stop])
    padded_text = pad_sequences(tokenized_text, maxlen=max_sequence_len, padding='pre')
    prediction = model.predict(padded_text)
    #top_index = prediction[0].argmax()
    #predicted_label = label_encoder.inverse_transform([top_index])[0]

    top_3_indices = prediction[0].argsort()[-3:][::-1]
    top_3_labels = label_encoder.inverse_transform(top_3_indices)
    top_3_probabilities = prediction[0][top_3_indices]

    top_3_results = [
        {"clasificacion": label, "probabilidad": float(prob)}
        for label, prob in zip(top_3_labels, top_3_probabilities)
    ]

    return top_3_results