import random
import base_generator as b
import numpy as np

# Función para generar variaciones de frases de fallo/desestima
def variar_frase_fallo(abrev_tengase, corte_apelaciones_var, num, recursos):
    variaciones = [
        f"{abrev_tengase} desestimado el recurso.",
        f"{abrev_tengase} desestimada por no cumplir lo solicitado por la {corte_apelaciones_var}.",
        f"{abrev_tengase} desestimado.",
        f"{abrev_tengase} desestimada.",
        "Se desestima el recurso.",
        f"{abrev_tengase} desestimado pb.",
        f"{abrev_tengase} desestimada el recurso ges.",
        f"{abrev_tengase} prima extraordinaria.",
        f"Resolviendo el folio {num}: {abrev_tengase} por desestimado",
        f"Por desestimada {recursos}"
    ]
    return random.choice(variaciones)

# Función para generar una frase aleatoria de fallo/desestima
def generar_frase_fallo():
    abrev_tengase = random.choice(b.abreviaciones_tengase)
    corte_apelaciones_var = random.choice(b.formas_corte_apelaciones)
    numero = random.choice(np.arange(120))
    recurso = random.choice(b.recursos)
    return variar_frase_fallo(abrev_tengase, corte_apelaciones_var,numero, recurso)

def generar_dataset(n=300):
    return [generar_frase_fallo() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))