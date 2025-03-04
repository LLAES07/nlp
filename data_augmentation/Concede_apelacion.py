import random
from . import base_generator as b
import numpy as np

def variar_frase(motivos, corte_abrev, cortes_chile, partes_, num, planes):
    variaciones = [
        f'concede recurso interconexión',
        f'concede apelacion {motivos}',
        f'según lo estipulado por la {corte_abrev} de {cortes_chile} se concede la apelación elévense',
        f'En vista y consideración lo informado por la {corte_abrev} de {cortes_chile} concédase la apelación',
        f'En vista y consideración lo informado por la {corte_abrev} de {cortes_chile} concédase el recurso vista',
        f'Concedida la apelacion de la parte {partes_}',
        f'(PR{num}/{planes})Concede Recurso(GC)',
        f'({planes})C.Recurso/R.R(ma)',
        f'({planes})Concede Recurso(LALL)',
        f'F.{num} Rep. Rech/Concede Ap.'



    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    motivos = random.choice(b.concede_apelacion_motivos)
    abreviacion_corte = random.choice(b.formas_corte_apelaciones)
    cortes_chile_sel = random.choice(b.formas_corte_apelaciones)
    partes_sel = random.choice(b.partes)
    num = random.choice(np.arange(30))
    planes_var = random.choice(b.planes)
    return variar_frase(motivos, abreviacion_corte, cortes_chile_sel, partes_sel, num, planes_var)


def generar_dataset(n=300):
    return [generar_frase_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))