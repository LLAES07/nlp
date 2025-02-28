
import random
from . import base_generator as b
import numpy as np


def variar_frase_ica(recurso, accion, motivo, solicita, num):
    variaciones = [
        # Correctas
        f'{recurso} {solicita} {accion} {motivo}.',
        f'solicita {accion} {motivo}.',
        f'pide {accion} {motivo}.',
        f'{recurso} requiere {accion} {motivo} en un plazo de {num} días.',
        f'requiere {accion} {motivo} en {num} días hábiles.',
        f'{recurso} ordena {accion} {motivo}.',
        f'ordena {accion} {motivo}.',
        f'{recurso} exige {accion} {motivo}.',
        f'exige {accion} {motivo}.',
        f'{recurso} demanda {accion} {motivo}.',
        f'demanda {accion} {motivo}.',
        f' ER/Cumple lo {solicita}'

    ]
    return random.choice(variaciones)

def generar_frase_ica_aleatoria():
    recurso = random.choice(b.recursos_ica)
    accion = random.choice(b.acciones_ica)
    motivo = random.choice(b.motivos_ica)
    peticion = random.choice(b.peticion)
    dias = random.choice(np.arange(10))
    return variar_frase_ica(recurso, accion, motivo, peticion, dias)

def generar_dataset(n=300):
    return [generar_frase_ica_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))