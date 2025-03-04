
import random
from . import base_generator as b
import numpy as np



import random

def variar_frase_tengase(tp, pide, partes, planes):
    variaciones = [
        # Correctas
        f'{tp} y por acompañados los documentos',
        f'{tp} por cumplida la sentencia',
        f'{tp} por cumplida lo {pide} por la corte',
        f'{tp} el mandato de el ab. recurrido',
        f'{tp} el mandato de el ab. recurrente',
        f'{tp} el pago de costas por la suma de',
        f'se {tp} las costas solicitadas pro el recurrente', 
        f'{tp} lo informado por {partes}',
        f'({planes})T.pte/v.e.forma (JBC)',
        f'({planes})T.pte/v.e.forma (GC)',
        f'({planes}){tp} (GC)',
        f'{tp} inf {partes}(costas)'
 

    ]
    return random.choice(variaciones)

def generar_frase_tengase():
    tengase_sel = random.choice(b.abreviaciones_tp)
    pide_sel = random.choice(b.peticion)
    partes_sel = random.choice(b.partes)
    planes_var = random.choice(b.planes)
    return variar_frase_tengase(tengase_sel, pide_sel, partes_sel, planes_var)



def generar_dataset(n=300):
    return [generar_frase_tengase() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))