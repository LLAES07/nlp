import os
import sys
import numpy as np
import pandas as pd
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from src.exception import CustomExecption
from src.logger import logging
from src.utils import save_object, cleaning_data
import nltk
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder


@dataclass
class DataTransformationConfig:
    processor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')
    tokenizer_file_path = os.path.join('artifacts', 'tokenizer.pkl')
    label_encoder_path = os.path.join('artifacts', 'label_encoder.pkl') 

class RemoveDuplicatesAndColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns=None):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X = X.drop_duplicates(subset=self.columns)
        X = X[self.columns]
        return X

class TextProcessor(BaseEstimator, TransformerMixin):
    def __init__(self, columns=None, new_columns=None):
        self.columns = columns
        self.new_columns = new_columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        nltk.download('stopwords')
        stop_words_es = set(stopwords.words('spanish'))
        
        def process_text(text):
            if text == 'Unknown':
                return "" 
            cleaned_text = cleaning_data(text)
            words = cleaned_text.split()
            filtered_words = [word for word in words if word not in stop_words_es]
            return " ".join(filtered_words)

        target_col = self.new_columns if self.new_columns else self.columns
        X[target_col] = X[self.columns].apply(process_text)
        return X

class TokenizationProcess(BaseEstimator, TransformerMixin):
    def __init__(self, num_words=None):
        self.tokenizer = None
        self.num_words = num_words
        self.max_sequence_len = None

    def fit(self, X, y=None):
        unique_words = set(word for sentence in X for word in sentence.split())
        total_words = len(unique_words) + 1  # +1 para incluir OOV token

        logging.info(f"Número total de palabras únicas en el corpus: {len(unique_words)}")
        logging.info(f"Total de palabras consideradas en el tokenizador: {total_words}")

        self.tokenizer = Tokenizer(num_words=total_words, oov_token="<OOV>")
        self.tokenizer.fit_on_texts(X)

        save_object(
            file_path=DataTransformationConfig.tokenizer_file_path,
            obj=self.tokenizer
        )
        logging.info(f"Tokenizer guardado correctamente en {DataTransformationConfig.tokenizer_file_path}")
        logging.info(f"Tamaño del vocabulario (incluyendo OOV): {len(self.tokenizer.word_index) + 1}")

        return self

    def transform(self, X):
        sequences = self.tokenizer.texts_to_sequences(X)
        max_sequence_len = max(len(seq) for seq in sequences)
        padded_sequences = pad_sequences(sequences, maxlen=max_sequence_len, padding='pre')

        logging.info(f"Longitud máxima de una oración antes del padding: {max(len(seq) for seq in sequences)}")
        logging.info(f"Longitud máxima establecida para padding: {max_sequence_len}")
        
        return padded_sequences

class DataTransformation:
    """Clase principal de transformación de datos"""
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def iniciando_transformacion_datos(self, train_path):
        try:
            train_data = pd.read_csv(train_path)
            logging.info('Leyendo los datos de entrenamiento')

            pipeline = Pipeline([
                ('remove_duplicates', RemoveDuplicatesAndColumns(columns=['descripcion', 'CLASIFICACION_CORRECTA'])),
                ('text_processing', TextProcessor(columns='descripcion'))
            ])
            train_data_transformed = pipeline.fit_transform(train_data)

            tokenizer_pipeline = Pipeline([
                ('tokenizer', TokenizationProcess())
            ])
            padded_sequences = tokenizer_pipeline.fit_transform(train_data_transformed['descripcion'])

            # Generación de X
            X = np.array(padded_sequences)

            # Convertimos las etiquetas en números enteros
            label_encoder = LabelEncoder()
            
            train_data_transformed['CLASIFICACION_NUM'] = label_encoder.fit_transform(train_data_transformed['CLASIFICACION_CORRECTA'])
            

            save_object(
                file_path=self.data_transformation_config.label_encoder_path, obj=label_encoder
            )

            logging.info(f"Label Encoder guardado en {self.data_transformation_config.label_encoder_path}")

            logging.info(f"Cantidad de clases únicas en CLASIFICACION_CORRECTA: {len(label_encoder.classes_)}")
            logging.info(f"Distribución de clases:\n{train_data_transformed['CLASIFICACION_CORRECTA'].value_counts()}")

            # 2. Convertir etiquetas numéricas a one-hot encoding
            y = to_categorical(train_data_transformed['CLASIFICACION_NUM'], num_classes=len(label_encoder.classes_))

        
            save_object(
                file_path=self.data_transformation_config.processor_obj_file_path,
                obj=pipeline
            )
            logging.info(f"Pipeline guardado en {self.data_transformation_config.processor_obj_file_path}")

            logging.info(f"Forma final de X (padded sequences): {X.shape}")
            logging.info(f"Forma final de y (one-hot encoded labels): {y.shape}")
            logging.info("Transformación de datos finalizada correctamente.")

            

            return X, y, self.data_transformation_config.processor_obj_file_path, train_data_transformed

        except Exception as e:
            logging.error("Error en iniciando_transformacion_datos")
            raise CustomExecption(e, sys)


if __name__ == "__main__":
    train_path = "Notebooks/data/processed_data.csv"
    data_transformer = DataTransformation()
    X, y, preprocessor_path, train_data_transformed = data_transformer.iniciando_transformacion_datos(train_path)
    
    # Mostramos información relevante
    print("Shape de X (padded sequences):", X.shape)
    print("Shape de y (labels):", y.shape)  # Debe ser (8109, 29)
    print("Primeros 20 registros del DataFrame transformado:")
    print(train_data_transformed.head(20))
