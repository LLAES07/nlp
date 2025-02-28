
import random
from . import base_generator as b
import numpy as np


def variar_frase(accion, motivo, accion_corte, tgse, ca_abrev):
    variaciones = [
        # Correctas
        f'La {ca_abrev} {accion_corte} la {accion}, {motivo}.',
        f'{accion_corte} la {accion} {motivo}.',
        f'La {ca_abrev} {accion_corte}, la {accion}, {motivo}.',
        f'{tgse} por {accion_corte} (la {accion}) {motivo}.',
        f'La corte {accion_corte}  la {accion} {motivo}.',
        f'La {accion} es {accion_corte}a, {motivo}.',
        f'La {accion} es {accion_corte}a  {motivo}.',
        f'La {accion} es {accion_corte}a, {motivo}.',
        f'La {accion} es {accion_corte}a (por {motivo}).',
        f'La {accion} ha sido {accion_corte}a por {motivo}.',
        f'La {accion} fue {accion_corte}a {motivo}.',
        f'La {accion} se considera {accion_corte}a, {motivo}.',
        f'Debido a {motivo}, la {accion} es {accion_corte}a.',
        f'Por {motivo}, la {accion} se {accion_corte}a.',
        f'La corte ha {accion_corte} la {accion} por {motivo}.',
        
        # Con errores comunes
        f'La corte {accion_corte} la {accion}, {motivo}', 
        f'La corte {accion_corte} la {accion} {motivo}',  
        f'La corte {accion_corte}, la {accion}, {motivo}', 
        f'La corte {accion_corte} (la {accion}) {motivo}',  
        f'La corte {accion_corte}  la {accion} {motivo}',  
        f'La {accion} es {accion_corte}a, {motivo}', 
        f'La {accion} es {accion_corte}a  {motivo}', 
        f'La {accion} es {accion_corte}a, {motivo}', 
        f'La {accion} es {accion_corte}a (por {motivo})',  
        f'La {accion} es {accion_corte}a por {motivo}',  
        f'La {accion}es {accion_corte}a {motivo}',  
        f'La corte {accion_corte} la {accion}, {motivo}.',  
        f'La corte {accion_corte} la {accion} {motivo}.',  
        f'La corte {accion_corte} la {accion}, {motivo} ', 
        f'La corte {accion_corte} la {accion} {motivo} ',  
    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    accion = random.choice(b.acciones)
    motivo = random.choice(b.motivos)
    accion_corte = random.choice(['declara inadmisible', 'omite pronunciamiento sobre', 'omte proncunc.', 'inadmis.', 'inadmisible.'])
    tgse_ = random.choice(b.abreviaciones_tengase)
    ca = random.choice(b.abreviaciones_cortes)
    return variar_frase(accion, motivo, accion_corte, tgse_, ca)

def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))