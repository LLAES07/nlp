import os, sys
from src.exception import CustomExecption
from src.logger import logging
import pandas as pd
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from data_augmentation.main import main

PROYECTO_DJANGO = os.path.join(os.path.dirname(__file__), '..', '..', 'django_app')
sys.path.append(PROYECTO_DJANGO)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')


import django
django.setup()

from nlp_app.models import ByPass

@dataclass
class DataIngestionConfig:
    train_set_path:str = os.path.join('artifacts', 'train.csv')
    raw_data_path:str = os.path.join('artifacts', 'data.csv')




class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def obtener_df_aprobados(self):
        """Consulta ByPass con status=True y retorna un DataFrame."""
        approved_bypass = ByPass.objects.filter(status=True).select_related('formsending')
        rows = []
        for bypass in approved_bypass:
            fs = bypass.formsending
            if fs:
                rows.append({
                    'descripcion': fs.descripcion,
                    'CLASIFICACION_CORRECTA': fs.category.clasificacion if fs.category else '',
                })
        return pd.DataFrame(rows)

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

        logging.info('Consultando datos aprobados de ByPass')
        df_nlp_app = self.obtener_df_aprobados()
        print(df_nlp_app)

        logging.info('Concatenación de los datos originales con los aumentados')

        df = pd.concat([df, df_augmented, df_nlp_app], ignore_index=True)

        
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
    train_data, raw_data = obj.inicia_data_ingestion('Notebooks/data/base_dataset.csv')
    print(pd.read_csv(train_data).head())

    train_path = "artifacts/train.csv"
    data_transformer = DataTransformation()
    X, y, preprocessor_path, train_data_transformed = data_transformer.iniciando_transformacion_datos(train_path)
    print(X)
    logging.info("Transformación de datos finalizada correctamente.")