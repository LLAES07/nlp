import random
from . import base_generator as b
import numpy as np


def variar_frase(infraccion, rango, corte, tgse, parte):
    variaciones = [
        f'La {corte} impone una multa de {rango}'
        f'La multa por {infraccion} es de {rango}.',
        f'La multa por {infraccion}, es de {rango}.',
        f'{tgse} por aplicada la multa.',
        f'Aplica multa por {infraccion}  es de {rango}.',
        f'Se impuso una multa de {rango} por {infraccion}.',
        f'Por {infraccion}, se sancionó con una multa de {rango}.',
        f'Por {infraccion}, se multó con un rango de {rango}.',
        f'El monto de la multa por {infraccion} será de {rango}.',
        f'La infracción de {infraccion} conlleva una multa de {rango}.',
        f'Debido a {infraccion}, se determinó una multa de {rango}.',
        f'La sanción por {infraccion} consiste en una multa de {rango}.',
        f'Por {infraccion}, se establece una multa de {rango}.',
        f'Se aplicará una multa de {rango} por {infraccion}.',
        f'Por no cumplir con {infraccion}, la multa es de {rango}.',
        f'La multa por la infracción de {infraccion} asciende a {rango}.',
        f'La comisión de {infraccion} se multa con {rango}.',
        # Incluyendo errores comunes
        f'La multa por {infraccion} es de {rango}',  
        f'Se impuso una multa de {rango} por {infraccion}',
        f'Aplica multa en beneficio fiscal',
        f'Aplica multa en beneficio de la {parte}'
        f'Multa/Pide FUN',
        f'Multa/Solicita FUN contractual'

    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    infraccion_sel = random.choice(b.infracciones)
    rango = random.choice(b.rangos_utm)
    corte = random.choice(b.formas_corte_apelaciones)
    tengase = random.choice(b.abreviaciones_tengase)
    parte_sel = random.choice(b.partes)
    return variar_frase(infraccion_sel, rango, corte, tengase,parte_sel)

def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))