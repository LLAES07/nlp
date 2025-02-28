
import random
from . import base_generator as b
import numpy as np


def variar_frase_tengase(cerifiquese_formas, ica_formas, cortes_chile, tp, parte ):
    variaciones = [
        # Correctas
        f'{cerifiquese_formas} lo solicitado por la {ica_formas} de {cortes_chile}.',
        f'{tp} la certificación por la parte {parte}',



    ]
    return random.choice(variaciones)

def generar_frase_aleatorea():
    cerifiquese_formas = random.choice(b.certifiquese)
    ica_var = random.choice(b.formas_corte_apelaciones)
    cortes_ch = random.choice(b.cortes_de_chile)
    tp_var = random.choice(b.abreviaciones_tp)
    parte_sel = random.choice(b.partes)
    return variar_frase_tengase(cerifiquese_formas, ica_var, cortes_ch, tp_var, parte_sel)

def generar_dataset(n=300):
    return [generar_frase_aleatorea() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))