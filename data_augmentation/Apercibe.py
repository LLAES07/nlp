import random
import base_generator as b
import numpy as np

# Función para generar variaciones de frases de apercibimiento
def variar_frase_apercibe(apercibe_var, parte_var):
    # Lista de plantillas de frases con variaciones
    variaciones = [
        f"hace efectivo {apercibe_var} a {parte_var}.",
        f"Previo a proveer, hágase coincidir la suma con el cuerpo del escrito, dentro del plazo establecido, bajo {apercibe_var}.",
        f"Atendido el tiempo transcurrido, se hace efectivo el {apercibe_var} decretado.",
        f"Se notifica {apercibe_var} a la parte {parte_var}.",
        "Se impone apercibimiento conforme a lo resuelto en autos.",
        f"No habiendo informado, se procede al apercibimiento de {parte_var}.",
        f"Apercibimiento: se deja sin efecto la resolución y se ordena {apercibe_var}.",
        f"Se ordena apercibimiento a la parte para que cumpla en plazo {apercibe_var}.",
        f"Ante la inactividad, se declara {apercibe_var} y se procede a archivar la causa.",
        f"Se realiza {apercibe_var} y se advierte multa en caso de incumplimiento.",
        f"Apercibimiento efectivo a la parte {parte_var}, comuníquese y archívese.",
        f"Se notifica {apercibe_var} a la parte para cumplir con lo ordenado.",
        f"Se procede al {apercibe_var}, solicitando informe dentro del plazo establecido.",
        f"{apercibe_var} decretado, a falta de respuesta.",
        f"Bajo {apercibe_var}, se requiere respuesta en cinco días hábiles.",
        f"El {apercibe_var} se efectúa debido a la inacción de la parte {parte_var}.",
        f"Apercibimiento: se deja constancia en autos de la inacción de {parte_var}.",
        f"Se notifica a la parte, bajo {apercibe_var}, que de no responder se procederá a archivar la causa.",
        f"Por falta de respuesta, se hace efectivo el {apercibe_var}.",
        f"Se ordena el {apercibe_var}, advirtiendo medidas en caso de incumplimiento de {parte_var}."
    ]
    return random.choice(variaciones)

# Función para generar una frase aleatoria de apercibimiento
def generar_frase_apercibe():
    apercibe_var = random.choice(b.variaciones_apercibe)
    parte_var = random.choice(b.variaciones_recurrente_recurrida)
    return variar_frase_apercibe(apercibe_var, parte_var)

def generar_dataset(n=300):
    return [generar_frase_apercibe() for _ in range(n)]

if __name__ == "__main__":
    frases = generar_dataset(10)
    print("\n".join(frases))