import os
import sys
import re
import numpy as np
import pandas as pd
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from src.exception import CustomExecption
from src.logger import logging
from src.utils import save_object
from src.utils import cleaning_data
import nltk
from nltk.corpus import stopwords


@dataclass
class DataTransformationConfig:
    processor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')


class RemoveDuplicatesAndColumns(BaseEstimator, TransformerMixin):

    def __init__(self, columns=None):
        self.columns= columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X = X.drop_duplicates(subset=self.columns)
        X = X[self.columns]
        return X
    

class TextProcessor(BaseEstimator, TransformerMixin):
    
    

    def __init__(self, columns=None, new_columns=None):
        self.columns= columns
        self.new_columns= new_columns


    def fit(self, X, y=None):
        return self

    def transform(self, X):
        nltk.download('stopwords')
        # Obtener las stopwords en español
        stop_words_es = set(stopwords.words('spanish'))
        sentences =  [ line for line in X[self.columns].values if line != 'Unknown']
        clean_data = [cleaning_data(t) for t in sentences]
        clean_data = [word for word in clean_data if word not in stop_words_es]

        target_col = self.new_columns if self.new_columns else self.columns
        
        X[target_col] = clean_data

        return X

        

class DataTransformation:

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def iniciando_transformacion_datos(self, train_path):


        try:
            train_data = pd.read_csv(train_path)
            print(train_data)

            logging.info('Leyendo los datos de entrenamiento')

            pipeline = Pipeline([
                ('remove_duplicates', RemoveDuplicatesAndColumns(columns=['descripcion', 'CLASIFICACION_CORRECTA'])),
                ('text_processing', TextProcessor(columns='descripcion', new_columns=None)),
            ])
            train_data_transformed = pipeline.fit_transform(train_data)

            save_object(
                    file_path=self.data_transformation_config.processor_obj_file_path,
                    obj=pipeline
                )
            logging.info(f"Pipeline guardado en {self.data_transformation_config.processor_obj_file_path}")

            print(train_data_transformed)
            return train_data_transformed, self.data_transformation_config.processor_obj_file_path

        except Exception as e:
            logging.error("Error en iniciando_trasnformacion_datos")
            raise CustomExecption(e, sys)


            
if __name__=="__main__":

    train_path = "Notebooks/data/processed_data.csv"
    data_transformer = DataTransformation()
    train_set_cleaned, preprocessor_path = data_transformer.iniciando_transformacion_datos(train_path)
    print(train_set_cleaned)
    logging.info(" Transformación de datos finalizada correctamente.")