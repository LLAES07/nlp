import random
from . import base_generator as b
import numpy as np

# Función para generar variaciones de frases de apercibimiento
def variar_frase(nhl, num, abrev_corte, cortes_chile, pidase_formas, partes_formas):
    # Lista de plantillas de frases con variaciones
    variaciones = [
        f'{nhl} lo obrado por la {abrev_corte} de {cortes_chile}',
        f'al folio {num}: {nhl} lo {pidase_formas} ',
        f'Al escrito de la {partes_formas} téngase por enterado que se declara {nhl}',
        f'Según lo informado por {partes_formas} en el folio {num}: {nhl}'
    ]
    return random.choice(variaciones)

# Función para generar una frase aleatoria de apercibimiento
def genera_frase_aleatorea():
    nhl_sel = random.choice(b.variaciones_no_ha_lugar)
    num = random.choice(np.arange(100))
    abrevia_corte_sel =  random.choice(b.formas_corte_apelaciones)
    corte_sel = random.choice(b.cortes_de_chile)
    pidase_sel = random.choice(b.peticion)
    partes_sel = random.choice(b.partes)


    return variar_frase(nhl_sel, num, abrevia_corte_sel, corte_sel, pidase_sel, partes_sel)

def generar_dataset(n=300):
    return [genera_frase_aleatorea() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))