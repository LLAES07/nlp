import random
from . import base_generator as b
import numpy as np


def variar_frase(tgse, num, var_corte):
    variaciones = [
        f'{tgse} por informado el numeral °14',
        f'Al folio {num}: comunica articulo n° 125',
        f'transcurrido el plazo de {num} dias dese estricto cumplimiento al articulo 125',
        f'Al folio n {num}: art 216',
        f'Al folio n {num}: art 125',
        f'{var_corte} informa numeral 14'

     
    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():

    tgse = random.choice(b.abreviaciones_tengase)
    num = random.choice(np.arange(100))
    var_corte_sel =  random.choice(b.formas_corte_apelaciones)

    return variar_frase(tgse, num, var_corte_sel)


def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))