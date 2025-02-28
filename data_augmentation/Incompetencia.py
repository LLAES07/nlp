import random
from . import base_generator as b
import numpy as np

# Función para generar variaciones de frases de apercibimiento
def variar_frase_apercibe(razon_inadmisible, num, corte, inadmisible_):
    # Lista de plantillas de frases con variaciones
    variaciones = [
        f"Se declara {inadmisible_} por {razon_inadmisible}",
        f"{razon_inadmisible} es {inadmisible_}",
        f"Al folio {num}: declara {inadmisible_}",
        f"Declara {inadmisible_} por la corte de {corte}",
        f"Inadm. {razon_inadmisible}",
        f"Por {razon_inadmisible} a lo solicitado por la corte de {corte} téngase por declarado la {inadmisible_}",

    ]
    return random.choice(variaciones)

# Función para generar una frase aleatoria de apercibimiento
def genera_frase_aleatorea():
    inadmisible_razones = random.choice(b.motivos_inadmisible)
    num = random.choice(np.arange(100))
    corte_sel = random.choice(b.cortes_de_chile)
    inadmisible = random.choice(b.inadmisible_formas)
    return variar_frase_apercibe(inadmisible_razones, num, corte_sel, inadmisible)

def generar_dataset(n=300):
    return [genera_frase_aleatorea() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))