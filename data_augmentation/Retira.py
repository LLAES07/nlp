
import random
import base_generator as b
import numpy as np


def variar_frase(item, motivo, tgse):
    variaciones = [
        # Correctas
        f'{tgse} retirado',
        f'Retira el {item}, por {motivo}.',
        f'Retira el {item}, por {motivo}.',
        f'El recurrido retira {item}, por {motivo}.',
        f'Retira el {item} por {motivo}.',
        f'Retira (el {item}) por {motivo}.',
        f'Retira  el {item} por {motivo}.',
        f'El {item} es retirado por {motivo}.',
        f'El {item} es retirado, por {motivo}.',
        f'El {item} es retirado (por {motivo}).',
        f'El {item} es retirado  por {motivo}.',
        f'Se ha retirado el {item} por {motivo}.',
        f'Se ha retirado, el {item}, por {motivo}.',
        f'Por {motivo}, se retira el {item}.',
        f'El {item} fue retirado debido a {motivo}.',
        f'La parte retira el {item} por {motivo}.',
        f'Retira el {item}, por {motivo}',  
        f'El recurrido retira {item}, por {motivo}',  
        f'Retira el {item} por {motivo}',  
        f'Retira (el {item}) por {motivo}',  
        f'Retira  el {item} por {motivo}',  
        f'El {item} es retirado por {motivo}',  
        f'El {item} es retirado, por {motivo}',  
        f'El {item} es retirado (por {motivo})', 
        f'El {item} es retirado  por {motivo}',  
        f'Se ha retirado el {item} por {motivo}',  
        f'Se ha retirado, el {item}, por {motivo}', 
        f'Por {motivo}, se retira el {item}', 
        f'El {item} fue retirado debido a {motivo}',  
        f'La parte retira el {item} por {motivo} '
    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    recurso = random.choice(b.recursos)
    motivo = random.choice(b.motivos)
    tgse = random.choice(b.abreviaciones_tengase)
    return variar_frase(recurso, motivo, tgse)

def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))