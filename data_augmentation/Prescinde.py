
import random
from . import base_generator as b
import numpy as np
import string

def variar_frase(parte, solicitud, planes, siglas, prescinde_var):
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
        f'En Relación Prescinde Informe',
        f'({planes}) prescinde informe',
        f"({planes}) Presc.Inf Aer ({siglas})",
        f'prescinde informe',
        f'({planes})AER pres. Fun ({siglas}c)',
        f'({planes}){prescinde_var})({siglas})'


    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    parte = random.choice(b.partes)
    solicitud = random.choice(b.solicitudes)
    planes_sel = random.choice(b.planes)
    generar_sigla = lambda longitud=2: ''.join(random.choice(string.ascii_uppercase) for _ in range(longitud))
    sigla = generar_sigla()
    presinde_sel = random.choice(b.prescinde_informe_variaciones)
    return variar_frase(parte, solicitud, planes_sel, sigla, presinde_sel)

def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))