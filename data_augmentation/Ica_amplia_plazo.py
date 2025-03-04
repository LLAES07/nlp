import random
from . import base_generator as b
import numpy as np

# Función para generar variaciones de frases de apercibimiento
def variar_frase(concede_ampliacion,planes, num, comunica, peticion):
    # Lista de plantillas de frases con variaciones
    variaciones = [
        
        f'F.{num} Rep. Rech/{concede_ampliacion}.',
        f'({planes}){concede_ampliacion}plazo (GC)',
        f'{concede_ampliacion}. Plazo/TP PyP'

    ]
    return random.choice(variaciones)

# Función para generar una frase aleatoria de apercibimiento
def genera_frase_aleatorea():
    concede_ampliacion_var = random.choice(b.planes)
    planes_var = random.choice(b.planes)
    num = random.choice(np.arange(100))
    comunica_sel = random.choice(b.comunica_var)
    peticion_sel = random.choice(b.peticion)
    return variar_frase(concede_ampliacion_var, planes_var, num, comunica_sel, peticion_sel)

def generar_dataset(n=300):
    return [genera_frase_aleatorea() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))