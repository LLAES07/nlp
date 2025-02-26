# CLASIFICACIÓN DE TEXTOS JUDICIALES CON REDES NEURONALES RECURRENTES LSTM


## Descripción del Proyecto
Sistema de clasificación automática de textos jurídicos mediante una red neuronal LSTM (Long Short-Term Memory) para categorizar descripciones de casos legales en 29 clases diferentes. El modelo permite procesar textos diarios de seguimiento de casos judiciales y asignarles automáticamente categorías específicas basadas en su contenido.

## Contexto de los Datos
### Fuentes de Datos:
1. **`df_csv`**: 
   - Registros diarios de estados de casos judiciales (1+ año de datos)
   - Columnas relevantes: 
     - `Trámite` (Filtro: solo "Resolución" y "Sentencia")
     - `Descripción` (textos a clasificar)

2. **`df_clasificador`**:
   - Dataset etiquetado con 2,000+ ejemplos clasificados manualmente
   - Estructura:
     - `Descripción`: Texto de entrada
     - `CLASIFICADOR_CORRECTA`: Etiqueta de categoría (29 clases posibles)


## Implementación Técnica

### Preprocesamiento de Datos

1. **Reclasificación df_csv**:

    - Generación de diccionario reclasificador usando df_clasificador

2. **Limpieza de Texto**:
   - Normalización de caracteres
   - Eliminación de stopwords y términos no relevantes
   - Corrección de abreviaturas legales

3. **Tokenización y Padding**:

4. **Data Augmentation**:
   - Generación de variaciones sintéticas de textos
   - Inclusión de errores comunes (omisión de puntos, espacios inconsistentes)
   - Modificaciones léxicas controladas

