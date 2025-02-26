import random
import base_generator as b
import numpy as np

def variar_frase(concepto, medida, valor, corte, parte_):
    variaciones = [
        # Variaciones con nombres de Cortes de Apelaciones
        f'La Corte de Apelaciones de {corte} fija los {concepto} en {valor} {medida}.',
        f'Fija las costas en contra de la parte {parte_}',
        f'Por resolución de la Corte de Apelaciones de {corte}, se fijan los {concepto} en {valor} {medida}.',
        f'Los {concepto} han sido fijados por la Corte de Apelaciones de {corte} en {valor} {medida}.',
        f'La Corte de Apelaciones de {corte} determina los {concepto} en {valor} {medida}.',
        f'En {corte}, la Corte de Apelaciones establece los {concepto} en {valor} {medida}.',
        f'Se informa que la Corte de Apelaciones de {corte} ha fijado los {concepto} en {valor} {medida}.',
        f'Por auto acordado de la Corte de Apelaciones de {corte}, los {concepto} quedan en {valor} {medida}.',
        f'La Corte de Apelaciones de {corte} manifiesta que los {concepto} están fijados en {valor} {medida}.',
        
        # Con errores comunes
        f'La Corte de Apelaciones de {corte} fija los {concepto} en {valor} {medida}', 
        f'Por resolución de la Corte de Apelaciones de {corte}, se fijan los {concepto} en {valor} {medida}',  
        f'Los {concepto} han sido fijados por la Corte de Apelaciones de {corte} en {valor} {medida}', 
        f'La Corte de Apelaciones de {corte} determina los {concepto} en {valor} {medida}',  
        f'En {corte}, la Corte de Apelaciones establece los {concepto} en {valor} {medida}',  
        f'Se informa que la Corte de Apelaciones de {corte} ha fijado los {concepto} en {valor} {medida}',  
        f'Por auto acordado de la Corte de Apelaciones de {corte}, los {concepto} quedan en {valor} {medida} ',  
        f'La Corte de Apelaciones de {corte} manifiesta que los{concepto} están fijados en {valor} {medida}',  
    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    concepto = random.choice(b.conceptos)
    medida = random.choice(b.medidas)
    valor = random.choice(b.valores)
    corte = random.choice(b.cortes)
    parte = random.choice(b.partes)
    return variar_frase(concepto, medida, valor, corte, parte)

# Generar varias frases aleatorias
def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))