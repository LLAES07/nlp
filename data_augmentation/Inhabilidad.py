
import random
from . import base_generator as b
import numpy as np

def variar_frase(profesion, causal, titulos, nombres, apellido_):
    variaciones = [
        # Correctas
        f'El {profesion} se declara inhábil {causal}.',
        f'El {profesion} se declara inhábil, {causal}.',
        f'El {profesion} se declara inhábil (por {causal}).',
        f'El {profesion} se declara inhábil  {causal}.',
        f'La inhabilidad del {profesion} se fundamenta en {causal}.',
        f'La inhabilidad del {profesion}, se fundamenta en {causal}.',
        f'La inhabilidad del {profesion} (se fundamenta en {causal}).',
        f'La inhabilidad del {profesion}  se fundamenta en {causal}.',
        f'Debido a {causal}, el {profesion} se inhabilita.',
        f'El {profesion} manifiesta inhabilidad por {causal}.',
        f'La causa de inhabilidad del {profesion} es {causal}.',
        f'Por {causal}, el {profesion} declara su inhabilidad.',
        f'El {profesion} está inhabilitado debido a {causal}.',
        f'La inhabilidad del {profesion} se basa en {causal}.',
        f'Declara inab. {titulos} {nombres}',
        f'Inhabilid {titulos} {nombres} {apellido_}',
        f'Inhabilidad {titulos} {nombres} {apellido_}',
        f'Inhabilidad de {profesion}. Int. JOA'
        
        # Con errores comunes
        f'El {profesion} se declara inhábil {causal}',  # Falta de punto al final
        f'El {profesion} se declara inhábil, {causal}',  # Falta de punto al final
        f'El {profesion} se declara inhábil (por {causal})',  # Falta de punto al final
        f'El {profesion} se declara inhábil  {causal}',  # Espacio extra
        f'La inhabilidad del {profesion} se fundamenta en {causal}',  # Falta de punto al final
        f'La inhabilidad del {profesion}, se fundamenta en {causal}',  # Coma incorrecta
        f'La inhabilidad del {profesion} (se fundamenta en {causal})',  # Falta de punto al final
        f'La inhabilidad del {profesion}  se fundamenta en {causal}',  # Espacio extra
        f'Debido a {causal}, el {profesion} se inhabilita',  # Falta de punto al final
        f'El {profesion}se declara inhábil {causal}',  # Espacio faltante
        f'El {profesion} se declara inhábil, {causal}.',  # Punto extra al final
        f'La inhabilidad del {profesion}, se fundamenta en {causal}.',  # Punto extra al final
        f'Debido a {causal} el {profesion} se inhabilita.',  # Espacio faltante
        f'El {profesion} se declara inhábil {causal} ',  # Espacio extra al final

        f"Inhabilidad {titulos} {nombres}",
        f"Se declara inhábil {titulos} {nombres}",
        f"Declaración de inhabilidad de {titulos} {nombres}",
        f"Inhabilidad declarada por {titulos} {nombres}",
        f"{titulos} {nombres} - Inhabilidad",
        f"Inhabilidad - {titulos} {nombres}",
        f"Se inhabilita {titulos} {nombres}",
        f'Decl.inh',
        f'Decl.inh minis. roberto',
        f'Decl.inh minis. Maria Tereza',
        f'Decl.inh abog.',
        'Decl.inh abogado integrante'
    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    profesion = random.choice(b.profesiones)
    causal = random.choice(b.causales)
    titulo = random.choice(b.titulos)
    nombre = random.choice(b.nombres)
    apellido = random.choice(b.apellidos_)
    return variar_frase(profesion, causal, titulo, nombre, apellido)

# Generar varias frases aleatorias
def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))