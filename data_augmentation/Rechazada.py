import random
from . import base_generator as b
import numpy as np


def variar_frase(item, decision, costo, motivo, planes):
    variaciones = [
        # Correctas
        f'El {item} se {decision}a {costo}, por {motivo}.',
        f'El {item} es {decision}o {costo}, debido a {motivo}.',
        f'Se {decision}a el {item} {costo} por {motivo}.',
        f'Se ha {decision}o el {item} {costo} por {motivo}.',
        f'Debido a {motivo}, el {item} se {decision}a {costo}.',
        f'El {item} ha sido {decision}o {costo} por {motivo}.',
        f'Rechaza, sin costas',
        f'Rechaza con costas reguladas en 200',
        f'({planes})Rechazada (JQQ)'
        f'NMV Litis/Rechazada {planes}',
        f'({planes})Rechazada/MasVida(JQQ)'
        
        # Con errores comunes
        f'El {item} se {decision}a {costo}, por {motivo}',  # Falta de punto al final
        f'El {item} es {decision}o {costo}, debido a {motivo}',  # Falta de punto al final
        f'Se {decision}a el {item} {costo} por {motivo}',  # Falta de punto al final
        f'Se ha {decision}o el {item} {costo} por {motivo}',  # Falta de punto al final
        f'Debido a {motivo}, el {item} se {decision}a {costo}',  # Falta de punto al final
        f'El {item} ha sido {decision}o {costo} por {motivo}',  # Falta de punto al final
        f'El {item} se {decision}a {costo} por {motivo} ',  # Espacio extra al final
        f'El {item}se {decision}a {costo}, por {motivo}',  # Espacio faltante
    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    recurso = random.choice(b.recursos)
    decision, costo = random.choice(b.decisiones_rechaza)
    motivo = random.choice(b.motivos_rechaza)
    planes_var = random.choice(b.planes)
    return variar_frase(recurso, decision, costo, motivo, planes_var)


def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))