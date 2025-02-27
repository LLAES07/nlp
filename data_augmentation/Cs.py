
import random
import base_generator as b
import numpy as np


def variar_frase_tengase(cumplase_, acciones, ):
    variaciones = [
        # Correctas
        f'{cumplase_}/{acciones} .',
        f'{cumplase_} {acciones}.',
        f'{cumplase_} ({acciones}).',
        
        # Con errores comunes
        f'{cumplase_}{acciones}',  # Falta espacio

    ]
    return random.choice(variaciones)

def generar_frase_aleatorea():
    recurso = random.choice(b.cumplase_)
    accion = random.choice(b.acciones)
    return variar_frase_tengase(recurso, accion)

def generar_dataset(n=300):
    return [generar_frase_aleatorea() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))