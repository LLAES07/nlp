import random
from . import base_generator as b
import numpy as np

def variar_frase(peticion, tgse, tp, parte, num):
    variaciones = [
        f'No ha lugar lo {peticion} por lo que se desestima',
        f'de fallo',
        f'Se desestima la {tgse} sin costas',
        f'{tgse} por desestimado el fallo',
        f'{tp} y por desestimado'
        f'Fallo/Desestima',
        f'Fallo/Desestimada',
        f"{tgse} desestimado el recurso.",
        f"Revuelve causa fallada a favor de la parte {parte}",
        f"Resolviendo el folio {num}: {tgse} por desestimado",
        f"desestima sin costas",
        f"desestima con costas"


    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    peticion_sel = random.choice(b.peticion)
    tengase_sel = random.choice(b.abreviaciones_tengase)
    tp_sel = random.choice(b.abreviaciones_tengase)
    parte_sel = random.choice(b.partes)
    num = random.choice(np.arange(100))
    return variar_frase(peticion_sel, tengase_sel, tp_sel, parte_sel, num)


def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))