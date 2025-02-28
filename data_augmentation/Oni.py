import random
from . import base_generator as b
import numpy as np

# Función para generar variaciones de frases de apercibimiento
def variar_frase(oni_formas, num, corte, desecuenta_formas):
    # Lista de plantillas de frases con variaciones
    variaciones = [
        f"Concede {oni_formas}",
        f"Téngase por concedida la {oni_formas}",
        f"la corte de {corte} de por aceptada la {oni_formas}"
        f"A la resolución del folio {num}: aceptada la {oni_formas}",
        f"dcta {oni_formas}",
        f"{desecuenta_formas} la {oni_formas}",
        f"Según lo revisado por el sistema computacional {desecuenta_formas} la {oni_formas}"

    ]
    return random.choice(variaciones)

# Función para generar una frase aleatoria de apercibimiento
def genera_frase_aleatorea():
    oni_sel = random.choice(b.oni_variaciones)
    num = random.choice(np.arange(100))
    corte_sel = random.choice(b.cortes_de_chile)
    desecuenta_sel = random.choice(b.variaciones_dese_cuenta)
    return variar_frase(oni_sel, num, corte_sel, desecuenta_sel)

def generar_dataset(n=300):
    return [genera_frase_aleatorea() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))