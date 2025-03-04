
import random
from . import base_generator as b
import numpy as np


def variar_frase_tengase(cumplase_, acciones, tgse, num ):
    variaciones = [
        # Correctas
        f'{cumplase_}/{acciones} .',
        f'{cumplase_} {acciones}.',
        f'{cumplase_} ({acciones}).',
        f'{tgse} por {cumplase_}', 
        # Con errores comunes
        f'{cumplase_}{acciones}',  # Falta espacio
        f'al folio {num}: {cumplase_}/{acciones}'

    ]
    return random.choice(variaciones)

def generar_frase_aleatorea():
    recurso = random.choice(b.cumplase_)
    accion = random.choice(b.acciones_cs)
    tgse_sel = random.choice(b.abreviaciones_tengase)
    num=random.choice(np.arange(100))
    return variar_frase_tengase(recurso, accion, tgse_sel,num)

def generar_dataset(n=300):
    return [generar_frase_aleatorea() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))