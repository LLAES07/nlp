
import random
from . import base_generator as b
import numpy as np
import string


import random

def variar_frase_tengase(agrega_var, planes, num_1, num_2, sigla_):
    variaciones = [
        f'{agrega_var}. {num_1}-{num_2}',
        f'({planes}){agrega_var}. {num_1}-{num_2}',
        f'Agréguese a la 1ra. Sala ({sigla_}',
        f'A.R./Agrégue Extra {num_1}-{num_2}',
        f'Agrégue Extra/A.R. {num_1}-{num_2}',
        f'En Rel./Agreg. extraord.{num_1}-{num_2}-'

  

    ]
    return random.choice(variaciones)

def generar_frase_tengase():
    agrega_var = random.choice(b.agreguese_var)
    planes_var = random.choice(b.planes)
    num1 = random.choice(np.arange(31))
    num2=random.choice(np.arange(12))
    generar_sigla = lambda longitud=2: ''.join(random.choice(string.ascii_uppercase) for _ in range(longitud))
    sigla = generar_sigla()
    return variar_frase_tengase(agrega_var, planes_var, num1, num2, sigla)



def generar_dataset(n=300):
    return [generar_frase_tengase() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))