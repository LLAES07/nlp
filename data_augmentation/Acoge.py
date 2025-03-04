import random
from . import base_generator as b
import numpy as np

def variar_frase_acoge(recurso, resolucion, isapre, plan, pronunciamiento):

    variaciones = [
        f"Se acoge {recurso} {resolucion}.",
        f"acogido el {recurso} interpuesto contra {isapre} {resolucion}.",
        f"Se acogió el {recurso} y se ordena a {isapre} que {pronunciamiento}.",
        f"Acogida la acción, se dispone mantener {plan} sin alza, {resolucion}.",
        f"{recurso} acogido {resolucion}, ordenando a {isapre} que {pronunciamiento}.",
        f"Se acoge el {recurso} {resolucion}, obligando a {isapre} a respetar el {plan}.",
        f"Acógese la demanda contra {isapre} {resolucion}, respecto del {plan}.",
        f"Se acoge la reclamación y se instruye a {isapre} {pronunciamiento}.",
        f"Queda acogido el {recurso} {resolucion}; {isapre} debe cumplir el {plan}.",
        f"Se acoge el {recurso} en todas sus partes {resolucion}, debiendo {isapre} {pronunciamiento}.",
        f'(NC) Acogida...(JBC)',
        f'(TF) Acogida...(JPM)'
    ]
    return random.choice(variaciones)

def generar_frase_acoge_aleatoria():


    
    recurso = random.choice(b.recursos)
    resolucion = random.choice(b.resoluciones_acoge)
    isapre = random.choice(b.isapres)
    plan = random.choice(b.planes)
    pronunciamiento = random.choice(b.pronunciamientos)
    
    return variar_frase_acoge(recurso, resolucion, isapre, plan, pronunciamiento)

def generar_dataset(n=300):
    """
    Genera un dataset de n frases sobre la acogida de un recurso/acción,
    usando la lógica definida en generar_frase_acoge_aleatoria.
    """
    return [generar_frase_acoge_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))
