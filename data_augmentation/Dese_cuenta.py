
import random
from . import base_generator as b
import numpy as np


def variar_frase_tengase(dese_cuent_var, corte_formas, num, partes):
    variaciones = [

        f"{dese_cuent_var} lo solicitado por la corte de {corte_formas}",
        f"al folio {num}: {dese_cuent_var}",
        f"{dese_cuent_var} el escrito de la {partes}",
        f"A la ampliación: {dese_cuent_var}",
        f"A la apelación {dese_cuent_var}"

    ]
    return random.choice(variaciones)

def generar_frase_aleatorea():
    dese_cuenta = random.choice(b.variaciones_dese_cuenta)
    cortes_ = random.choice(b.formas_corte_apelaciones)
    num=random.choice(np.arange(100))
    partes_sel = random.choice(b.partes)
    return variar_frase_tengase(dese_cuenta, cortes_,num, partes_sel)

def generar_dataset(n=300):
    return [generar_frase_aleatorea() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))