

import random
import base_generator as b
import numpy as np


def variar_frase(item, motivo, tgse, num):
    variaciones = [
        f'{tgse} archivado el recurso'
        f'Al folio {num}: Archívese',
        f'El {item} se archiva por {motivo}.',
        f'El {item} ha sido archivado por {motivo}.',
        f'Se archiva el {item} debido a {motivo}.',
        f'Por {motivo}, se archiva el {item}.',
        f'El {item} es archivado por {motivo}.',
        f'El {item} se ha archivado por {motivo}.',
        f'Debido a {motivo}, el {item} se archiva.',
        f'El {item} se encuentra archivado por {motivo}.',
        f'La {item} se archiva por {motivo}.',
        f'El {item} fue archivado por {motivo}.',
        f'Por {motivo}, el {item} se archivó.',
        f'El archivo del {item} se debe a {motivo}.',
        f'El {item} pasó a archivo por {motivo}.',
        f'El proceso del {item} se archivó por {motivo}.',
        f'El {item} se archiva por {motivo}', 
        f'El {item} ha sido archivado por {motivo}', 
        f'Se archiva el {item} debido a {motivo}',  
        f'Por {motivo}, se archiva el {item}',  
        f'El {item} es archivado por {motivo}', 
        f'El {item} se ha archivado por {motivo}',  
        f'Debido a {motivo}, el {item} se archiva', 
        f'El {item} se encuentra archivado por {motivo}', 
        f'La {item} se archiva por {motivo} ',
        f'El {item}se archiva por {motivo}'
    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    recurso = random.choice(b.recursos)
    motivo = random.choice(b.motivos)
    tgse = random.choice(b.abreviaciones_tengase)
    num = random.choice(np.arange(100))

    return variar_frase(recurso, motivo, tgse, num)


def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))