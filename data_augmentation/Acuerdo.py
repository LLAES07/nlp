import random
import base_generator as b
import numpy as np

def variar_frase(abrev_corte, corte_apelaciones_var, cortes, abrev_tp, nombres, apellidos, num):
    """Genera una variación aleatoria de una frase para la clase 'Acuerdo'."""

    variaciones_acuerdo = [
        f"Estése a la disponibilidad de esta corte de apelaciones de {abrev_corte} a su ingreso y prioridad.",
        f"Al folio {num}: Estése a la disponibilidad de esta corte de apelaciones de {abrev_corte} a su ingreso y prioridad.",
        f"Este a la disponibilidad de esta {abrev_corte} de {cortes} a su ingreso y prioridad.",
        "Pase a los ministros del acuerdo.",
        f"Rija el estado de acuerdo {corte_apelaciones_var}.",
        f"{abrev_tp} Acuerdo.",
        "Nota de acuerdo: redacción Erika Villegas.",
        "Certifica alegato y acuerdo.",
        "Cert. de acuerdo.",
        "Certif. alegato y acuerdo.",
        f"Nota de acuerdo: redacción ministra {nombres} {apellidos}.",
        f"Nota acuerdo: redacción {nombres} {apellidos}",
        f"Nota de acuerdo: redacción {nombres} {apellidos}", 
        "Incorpórese a la tabla respectiva de acuerdo a su disponibilidad.",
        "Certificado causa en acuerdo.",
        "Suspensión vista de común acuerdo art. 165 N° 5 C.P.C.",
        "Pase a los ministros del acuerdo a la sala.",
        "Pase a los min del acuerdo.",
        "Pase a ministros del acuerdo.",
        "Nota de acuerdo.",
        "Certificado de acuerdo.",
        "Certificado alegato y acuerdo.",
        "En acuerdo.",
        "Nota acuerdo.",
        "Certificado tránsito del estudio al acuerdo.",
        "Certificación acuerdo.",
        "Certificación causa en acuerdo.",
        "Pase a ministros acuerdo.",
        f"Al folio {num}: por cumplido lo ordenado, rija el estado de acuerdo.",
    ]
    return random.choice(variaciones_acuerdo)

def generar_frase_aleatoria():

    abrev_corte = random.choice(b.abreviaciones_cortes)
    corte_apelaciones_var = random.choice(b.formas_corte_apelaciones)
    cortes = random.choice(b.cortes_de_chile)
    abrev_tp = random.choice(b.abreviaciones_tp)
    nombres = random.choice(b.nombres_)
    apellidos = random.choice(b.apellidos_)
    numero = random.choice(np.arange(120))
  
    return variar_frase(abrev_corte, corte_apelaciones_var, cortes, abrev_tp,nombres, apellidos, numero)

def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))