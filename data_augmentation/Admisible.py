
import random
from . import base_generator as b
import numpy as np
import string


import random

def variar_frase_tengase(admisibles_var, planes, siglas):
    variaciones = [
        # Correctas
        f'({planes}){admisibles_var} ({siglas})',
        f'({planes}){admisibles_var}({siglas})',


    ]
    return random.choice(variaciones)

def generar_frase_tengase():
    admisibles_var = random.choice(b.admisible_formas)
    planes_var = random.choice(b.planes)
    generar_sigla = lambda longitud=2: ''.join(random.choice(string.ascii_uppercase) for _ in range(longitud))
    sigla = generar_sigla()
    return variar_frase_tengase(admisibles_var,  planes_var, sigla)



def generar_dataset(n=300):
    return [generar_frase_tengase() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))