import os, sys
from src.exception import CustomExecption
from src.logger import logging
import pandas as pd
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from data_augmentation.main import main

@dataclass
class DataIngestionConfig:
    train_set_path:str = os.path.join('artifacts', 'train.csv')
    raw_data_path:str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()




    def inicia_data_ingestion(self, data):

        logging.info('Iniciando el proceso de lectura de la inyección de componentes')


        df = pd.read_csv(data)

        logging.info('Lectura del archvio exitosa')

        os.makedirs(os.path.dirname(self.ingestion_config.train_set_path), exist_ok=True)
        logging.info('La carpeta ha sido generada o ya está presente')


        logging.info('Comienzo generación datos aumentados')

        df_augmented = main()

        df_augmented.columns=['descripcion', 'CLASIFICACION_CORRECTA']

        logging.info('Datos aumentados generados')

        
        logging.info('Concatenación de los datos originales con los aumentados')

        df = pd.concat([df, df_augmented], ignore_index=True)

        
        logging.info('Datos revueltos')

        df = df.sample(frac=1, random_state=42).reset_index(drop=True)
        


        df.to_csv(self.ingestion_config.train_set_path, index=False, header=True)

        logging.info('Datos Guardados en artifcacts train.data')

        
        logging.info('Archivo raw ha sido creado')

        return (
            self.ingestion_config.train_set_path,
            self.ingestion_config.raw_data_path
        )

    
if __name__=="__main__":

    obj = DataIngestion()
    obj.inicia_data_ingestion('Notebooks/data/base_dataset.csv')

    train_path = "artifacts/train.csv"
    data_transformer = DataTransformation()
    train_set_cleaned, preprocessor_path = data_transformer.iniciando_transformacion_datos(train_path)
    print(train_set_cleaned.head())
    logging.info("Transformación de datos finalizada correctamente.")