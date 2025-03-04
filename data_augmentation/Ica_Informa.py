import random
from . import base_generator as b
import numpy as np

# Función para generar variaciones de frases de apercibimiento
def variar_frase(planes, num, comunica, peticion, tengase_var):
    # Lista de plantillas de frases con variaciones
    variaciones = [
        
        f"Al folio {num}, agréguese a estos antecedentes.",
        f'agrega informe/plazo',
        f'Notif.Estado Diario (JBC)',
        f'Notif.Estado Diario (JP)',
        f'Notif.Estado Diario (ESTLL)',
        f'{comunica} recursos',
        f'{comunica} sentencias',
        f'{comunica} resolución',
        f'({planes})suspende AER(rbf)',
        f'({planes})suspende AER(JQL)',
        f'({planes})suspende AER(LMN)'
        f'{comunica} (JBC)',
        f'{comunica} (PQ)',
        f'{comunica} (LLQ)',
        f'{comunica} cumplimiento',
        f'Rectifica Recurso de Protecció',
        f'ratifica Recurso de Protección',
        f'comunica Recurso de Protección',
        f'({planes}) Este al mérito (JQQ)',
        f'({planes}) Este al mérito (rbf)',
        f'{comunica} Sentencia (LUC)'
        f'{comunica} Sentencia (LQL)',
        f'{comunica} Sentencia (FP)',
        f'Como se {peticion}',
        f'{tengase_var} por reacusado',
        f'Reposición Rechaza(rbf)',
        f'Reposición Rechaza(JQQ)',
        f'({planes}) Reposición Rechaza(LLQ)',
        f'Habilita alegatos',
        f'hab. alegatos del ministro',
        f'hab. alegatos de la recurrida',
        f'habilita alegatos parte recurrente',
        f'Comunca inhabilidades',
        f'comunica inhabilidades',
        f'Remitido recurso a la isapre',
        f'Remitido recurso a la corte'
        f'Remitido documento',
        f'Por no presentado escrito {tengase_var} presente'
        f'No presenta carta {tengase_var} presente'



    ]
    return random.choice(variaciones)

# Función para generar una frase aleatoria de apercibimiento
def genera_frase_aleatorea():
    planes_var = random.choice(b.planes)
    num = random.choice(np.arange(100))
    comunica_sel = random.choice(b.comunica_var)
    peticion_sel = random.choice(b.peticion)
    tgse = random.choice(b.abreviaciones_tengase)
    return variar_frase(planes_var, num, comunica_sel, peticion_sel, tgse)

def generar_dataset(n=300):
    return [genera_frase_aleatorea() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))