
import random
import base_generator as b
import numpy as np



import random

def variar_frase_tengase(tp, pide):
    variaciones = [
        # Correctas
        f'{tp} y por acompañados los documentos',
        f'{tp} por cumplida la sentencia',
        f'{tp} por cumplida lo {pide} por la corte',
        f'{tp}'

    ]
    return random.choice(variaciones)

def generar_frase_tengase():
    tengase_sel = random.choice(b.abreviaciones_tp)
    pide_sel = random.choice(b.peticion)
    return variar_frase_tengase(tengase_sel, pide_sel)



def generar_dataset(n=300):
    return [generar_frase_tengase() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))