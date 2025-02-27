
import random
import base_generator as b
import numpy as np

def variar_frase_tramitacion(recurso, corte_chile):
    """
    Genera una frase aleatoria para indicar el inicio de tramitación
    de un recurso, con variaciones en tildes, errores ortográficos y formato.
    """
    variaciones = [
        f"Inicio de tramitación del {recurso}.",
        f"Inicio de tramitación del {recurso}",  # sin punto
        f"Inicio de tramitacion del {recurso}.",   # sin tilde en 'tramitacion'
        f"Iniciado la tramitación del {recurso}.",
        f"Iniciado la tramtiacion del {recurso}.",  # error: 'tramtiacion' en vez de 'tramitación'
        f"Por iniciado la tramitación del {recurso}.",
        f"Por iniciado la tramtiacion del {recurso}.",
        f"Iniciado la tramitación en la corte de {corte_chile} del {recurso}.",
        f"Comienza tramitación del {recurso}.",
        f"Comenzada la tramitación del {recurso}.",
        f"Inicia la tramtiacion del {recurso}.",
        f"El inicio de tramitación del {recurso} se realizó.",
        f"El inicio de tramtiacion del {recurso} se realizó.",
        f"Se inicia la tramitación del {recurso}.",
        f"Se inicia la tramtiacion del {recurso}.",
        f"El {recurso} inicia su tramitación.",
        f"El {recurso} inicia su tramtiacion.",
        f"Por el inicio de tramitación del {recurso}.",
        f"Por el inicio de tramtiacion del {recurso}.",
        f"Inicio de tramitación en el {recurso}.",
        f"Inicio de tramtiacion en el {recurso}.",
        # Agregar variantes con errores de separación o puntuación
        f"El inicio del {recurso} es por tramitación.",
        f"El inicio del {recurso} es por tramtiacion.",
        f"Inicio, tramitación del {recurso}.",
        f"Inicio tramitación, del {recurso}.",
    ]
    return random.choice(variaciones)

def generar_frase_inicio():
    recurso = random.choice(b.recursos)
    corte_ch = random.choice(b.cortes_de_chile)
    return variar_frase_tramitacion(recurso, corte_ch)

def generar_dataset(n=300):
    return [generar_frase_inicio() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))