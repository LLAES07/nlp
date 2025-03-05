import os
import sys
import numpy as np
import pandas as pd
from dataclasses import dataclass
from datetime import datetime
from src.logger import logging
from src.utils import save_object   
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Nadam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam
from sklearn.utils.class_weight import compute_class_weight
from src.utils import save_metrics
import matplotlib.pyplot as plt

@dataclass
class ModelTrainingConfig:
    trained_model_file_path : str = os.path.join('artifacts', 'model.pkl')
    metrics_path: str = os.path.join('artifacts', 'model_metrics.json')

class ModelTrainer:

    def __init__(self):
        self.config = ModelTrainingConfig()

    def construir_modelo(self, vocab_size, max_sequence_len, num_clases):
        """Función que construye el modelo LSTM BIDIRECCIONAL"""
        try:
            model = Sequential([
                Embedding(input_dim=vocab_size, output_dim=128, input_length=max_sequence_len),
                Bidirectional(LSTM(64, return_sequences=False, kernel_regularizer=l2(0.0005))),
                Dropout(0.4),
                Dense(12, activation='relu', kernel_regularizer=l2(0.0005)),
                BatchNormalization(),
                Dropout(0.3),
                Dense(num_clases, activation='softmax')
            ])

            optimizer = Adam(learning_rate=0.001)
            model.compile(optimizer=optimizer, 
                        loss='categorical_crossentropy', 
                        metrics=['accuracy'])
            
            logging.info("Modelo LSTM bidireccional completado")

            return model

        except Exception as e:
            logging.error("Error al construir el modelo LSTM")
            raise e
        

    def entrenar_modelo(self, X_train, X_test, y_train, y_test, vocab_size, max_sequence_len, num_classes):
        """ Entrena el modelo LSTM con los datos de entrenamiento """
        try:
            model = self.construir_modelo(vocab_size, max_sequence_len, num_classes)
        
            logging.info("Iniciando entrenamiento del modelo LSTM...")

            early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
            reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3, min_lr=1e-6, verbose=1)

            y_train_int = y_train.argmax(axis=1)  # De one-hot a entero
            class_weights = compute_class_weight('balanced', classes=np.unique(y_train_int), y=y_train_int)

            class_weights_dict = dict(enumerate(class_weights))
            history = model.fit(X_train, y_train, 
                                validation_data=(X_test, y_test), 
                                epochs=20, batch_size=32, 
                                class_weight=class_weights_dict,
                                callbacks=[early_stopping, reduce_lr])

            logging.info("Entrenamiento completado.")

            # Evaluación del modelo
            loss, accuracy = model.evaluate(X_test, y_test)
            logging.info(f"Precisión del modelo en test: {accuracy:.4f}")

            metrics = {
            "loss": loss,
            "accuracy": accuracy,
            "epochs": len(history.history['loss']),
            "val_loss": history.history['val_loss'][-1],
            "val_accuracy": history.history['val_accuracy'][-1]
            }
            save_metrics(self.config.metrics_path, 
                         metrics)
            
            logging.info(f"Métricas guardadas en {self.config.metrics_path}")


            # Guardar el modelo
            save_object(self.config.trained_model_file_path, obj=model)
            logging.info(f"Modelo guardado en {self.config.trained_model_file_path}")

            return model, history

        except Exception as e:
            logging.error("Error durante el entrenamiento del modelo LSTM")
            raise e


    def plot_training_history(self, history, file_path="artifacts/training_plot.png"):
        """Genera y guarda un gráfico del historial de entrenamiento."""
        plt.figure(figsize=(10, 5))

        # Pérdida
        plt.subplot(1, 2, 1)
        plt.plot(history.history['loss'], label='Training Loss')
        plt.plot(history.history['val_loss'], label='Validation Loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.title('Training vs Validation Loss')

        # Precisión
        plt.subplot(1, 2, 2)
        plt.plot(history.history['accuracy'], label='Training Accuracy')
        plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.title('Training vs Validation Accuracy')

        plt.tight_layout()
        plt.savefig(file_path)
        plt.close()



    def iniciar_modelaje(self, X, y): 
        try:
            logging.info("Dividiendo datos en conjunto de entrenamiento y prueba...")
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            logging.info(f"Shape de X_train: {X_train.shape}, X_test: {X_test.shape}")
            logging.info(f"Shape de y_train: {y_train.shape}, y_test: {y_test.shape}")

            # Cargar el Tokenizer guardado
            from src.utils import load_object
            tokenizer = load_object("artifacts/tokenizer.pkl")  

            # Obtener tamaño correcto del vocabulario
            vocab_size = len(tokenizer.word_index) + 1  
            max_sequence_len = X.shape[1]
            num_classes = y.shape[1]

            # Construir y entrenar el modelo
            logging.info("Construyendo y entrenando el modelo LSTM...")
            model, history = self.entrenar_modelo(X_train, X_test, y_train, y_test, vocab_size, max_sequence_len, num_classes)

            logging.info("Modelo entrenado exitosamente.")

            self.plot_training_history(history, "artifacts/training_plot.png")
            logging.info("Gráfica de entrenamiento guardada en artifacts/training_plot.png")
         
            return model, history

        except Exception as e:
            logging.error("Error en el modelaje y entrenamiento")
            raise e
        
if __name__ == "__main__":
    from src.components.data_transformation import DataTransformation

    # Cargar datos preprocesados
    train_path = "Notebooks/data/processed_data.csv"
    data_transformer = DataTransformation()
    X, y, preprocessor_path, _ = data_transformer.iniciando_transformacion_datos(train_path)

    # Inicializar el modelaje y entrenamiento en un solo paso
    trainer = ModelTrainer()
    model, history = trainer.iniciar_modelaje(X, y)
