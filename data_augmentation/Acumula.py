import random
from . import base_generator as b
import numpy as np

# Genera un número aleatorio de 3 dígitos
def generar_num_3():
    return str(random.randint(100, 999))

# Genera un número aleatorio de 4 dígitos
def generar_num_4():
    return str(random.randint(2000, 2050))

# Genera roles en el formato xxx-yyyy
def generar_rol():
    return f"{generar_num_3()}-{generar_num_4()}"

def generar_frase_aleatoria():
    rol1 = generar_rol()
    rol2 = generar_rol()
    abreviaturas = ['Acum.', 'Acumula', 'Acum. a', 'Se acumula a', 'Acumulado a', 'acumúlese', 'tengase por acumulado', 'tgse acumla', 'acumulación']
    abreviatura = random.choice(abreviaturas)  # Escoge una sola abreviatura
    variaciones = [
        f'{abreviatura}:{rol1} con {rol2} de la corte de {random.choice(b.cortes_de_chile)}.',
        f'{abreviatura} {rol1}, con {rol2} de la corte de {random.choice(b.abreviaciones_cortes)}',
        f'{random.choice(b.cortes_de_chile)} {abreviatura} {rol1} (con {rol2}).',
        f'{abreviatura} {rol1}  con {rol2}.',
        f'{abreviatura} al rol {rol1}',
        f'El rol {rol1} {abreviatura} {rol2}.',
        f'El rol {rol1}, {abreviatura} {rol2}.',
        f'El rol {rol1} ({abreviatura} {rol2}).',
        f'El rol {rol1}  {abreviatura} {rol2}.',
        f'Acum:Protección-{rol1}',
        f'{abreviaturas} Autos'
    ]
    return random.choice(variaciones)


def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))