
import random
from . import base_generator as b
import numpy as np

def variar_frase(parte, solicitud):
    variaciones = [
        f'Prescinde de la {parte}, por no {solicitud}.',
        f'Prescinde de la {parte} por no {solicitud}.',
        f'Prescinden, de la {parte}, por no {solicitud}.',
        f'Prescinden (de la {parte}) por no {solicitud}.',
        f'Prescinden  de la {parte} por no {solicitud}.',
        f'La corte prescinde de la {parte} por no {solicitud}.',
        f'Se prescinde, de la {parte}, por no {solicitud}.',
        f'La corte prescinde  de la {parte} por no {solicitud}.',
        f'La corte ha prescindido de la {parte} por no {solicitud}.',
       f'La ica ha prescindido de la {parte} por no {solicitud}.',
        f'La ica de santiago ha prescindido de la {parte} por no {solicitud}.',


    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    parte = random.choice(b.partes)
    solicitud = random.choice(b.solicitudes)
    return variar_frase(parte, solicitud)

def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))