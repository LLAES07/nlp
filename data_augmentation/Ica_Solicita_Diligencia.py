
import random
from . import base_generator as b
import numpy as np
import string


def variar_frase_ica(recurso, accion, motivo, solicita, num, planes, sigla_, partes):
    variaciones = [
        # Correctas
        f'{recurso} {solicita} {accion} {motivo}.',
        f'solicita {accion} {motivo}.',
        f'pide {accion} {motivo}.',
        f'{recurso} requiere {accion} {motivo} en un plazo de {num} días.',
        f'requiere {accion} {motivo} en {num} días hábiles.',
        f'{recurso} ordena {accion} {motivo}.',
        f'ordena {accion} {motivo}.',
        f'{recurso} exige {accion} {motivo}.',
        f'exige {accion} {motivo}.',
        f'{recurso} demanda {accion} {motivo}.',
        f'demanda {accion} {motivo}.',
        f' ER/Cumple lo {solicita}',
        f'({planes})NHL/pide cuenta({sigla_})',
        f'Pide FUN dentro del plazo de {num} dias',
        f'Informa domicilio contractual',
        f'({planes}) Certifíquese/Oficie ({sigla_})',
        f'({planes}) pide cta.({sigla_})',
        f'reitéra informe/oficio',
        f'vuelve a solicitar informe',
        f'({planes})cta ONI/Plazo({sigla_})',
        f'({planes}) Nhl/P.Cta.Inf ({sigla_})',
        f'({planes})Nhl/P.Cta.Inf ({sigla_})',
        f'Trámite - pide informes',
        f'Trámite - pide FUN',
        f'Venga en forma',
        f'rectifica {partes}/oficio',
        f'informa {partes}/diligencia',
        f'Venga de la forma correcta el recurso',
        f'p.proveer indique lo solicitado',
        f'p.proveer indique lo pedido',
        f'({planes})DSE/pide cta({sigla_})',
        f'Ofíciese (JQQ)',
        f'Ofíciese (JLL)',
        f'Ofíciese (rbf)',
        f'Pide cumplimiento de sentencia en especifico lo referido al folio 24 dentro del 5to día',
        f'Pide cumplimiento de sentencia en especifico lo referido al folio 5 dentro del 03 días'
        f'({planes})ofíciese({sigla_})',
        f'Certi.Sr.Secretario-Pide cuenta',
        f'Certi.Sr.Secretario-Pide informe',
        f'Aclarado lo del folio {num}: de la {partes}',
        f'(..{num}) Cumplimiento con Citaci',
        f'(..{num}) Cumplimiento con Citacion',
        f'({planes}) Ac.Fun/Aer ({sigla_})',
        f'{solicita} Infor. Cumpl. Sent. NMV',
        f'({planes}) {solicita}.Informe ({sigla_})',
        f'({planes}) Conciliese Suma',
        f'({planes}) Pide Cta.Informe ({sigla_})',
        f'solicita informe a la {partes}',
        f'{solicita} cuenta a la Isapre del informe ordenado remitir',
        f'Reposición Rechaza/{solicita} inform',
        f'Reposición Rechaza/{solicita} informe',
        f'{solicita} Inf. Cumplimiento',
        f'{solicita} Inf. cumplimiento de sentencia'







    ]
    return random.choice(variaciones)

def generar_frase_ica_aleatoria():
    recurso = random.choice(b.recursos_ica)
    accion = random.choice(b.acciones_ica)
    motivo = random.choice(b.motivos_ica)
    peticion = random.choice(b.peticion)
    dias = random.choice(np.arange(10))
    planes_var = random.choice(b.planes)
    generar_sigla = lambda longitud=2: ''.join(random.choice(string.ascii_uppercase) for _ in range(longitud))
    sigla = generar_sigla()
    partes_sel = random.choice(b.partes)

    return variar_frase_ica(recurso, accion, motivo, peticion, dias, planes_var, sigla, partes_sel)

def generar_dataset(n=300):
    return [generar_frase_ica_aleatoria() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))