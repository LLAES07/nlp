
                            
                            
import random
from . import base_generator as b
import numpy as np
import string


def variar_frase_tengase(planes_var, sigla_2, evacua_formas, sigala_3):
    variaciones = [

        f"({planes_var}){evacua_formas}({sigla_2}",
        f'({planes_var}){evacua_formas}({sigla_2})',
        f"({planes_var}){evacua_formas}({sigala_3}",
        f'({planes_var}){evacua_formas}({sigala_3})',


        f"({planes_var}){evacua_formas}({sigla_2} duplicidad",
        f'({planes_var}){evacua_formas}({sigla_2}) duplicidad',
        f"({planes_var}){evacua_formas}({sigala_3} duplicidad",
        f'({planes_var}){evacua_formas}({sigala_3}) duplicidad'
    ]
    return random.choice(variaciones)

def generar_frase_aleatorea():
    planes = random.choice(b.planes)
    generar_sigla2 = lambda longitud=2: ''.join(random.choice(string.ascii_uppercase) for _ in range(longitud))
    sigla2 = generar_sigla2()
    generar_sigla3 = lambda longitud=3: ''.join(random.choice(string.ascii_uppercase) for _ in range(longitud))
    sigla3 = generar_sigla3()
    evacua_formas = random.choice(b.evacua_infome_var)
    return variar_frase_tengase(planes, sigla2, evacua_formas, sigla3)

def generar_dataset(n=300):
    return [generar_frase_aleatorea() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))