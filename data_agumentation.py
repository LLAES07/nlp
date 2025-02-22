import random
import numpy as np


random.seed(42)


partes = [
    "Demandante", "Dte.", "Dmte.", "Dmant.",
    "Demandado", "Ddo.", "Dmdo.", "Dmand.",
    "Tercero interesado", "Terc.", "Terc. Int.", "T.I.",
    "Acusado", "Acus.", "Acsdo.",
    "Fiscalía", "Fisc.", "Fcal.", "Fcía.", 
    "Recurrida", "Rda.", "Rcrda.", "Recurr.",
    "Recurrente", "Rte.", "Rcte.", "Rcrte.",
    
    "Apelante", "Apel.", "Aplte.",
    "Apelado", "Apdo.", "Apldo.",
    "Querellante", "Qte.", "Qllte.", "Quer.",
    "Querellado", "Qdo.", "Qlldo.",
    "Interviniente", "Intv.", "Interv.",
    "Actor", "Act.", "Atr.",
    "Imputado", "Imp.", "Imptdo.",
    "Denunciante", "Den.", "Dnte.",
    "Denunciado", "Dndo.", "Denunc.",
    "Testigo", "Test.", "Tstgo."
]

cortes_de_chile = [
    "Arica",
    "Iquique",
    "Antofagasta",
    "Copiapó",
    "La Serena",
    "Valparaíso",
    "Santiago",
    "Rancagua",
    "Talca",
    "Chillán",
    "Concepción",
    "Temuco",
    "Valdivia",
    "Puerto Montt",
    "Coyhaique",
    "Punta Arenas"
]

abreviaciones_cortes = [
    "ARC",  # Arica
    "IQQ",  # Iquique
    "ANT",  # Antofagasta
    "COP",  # Copiapó
    "SER",  # La Serena
    "VALP",  # Valparaíso (también se usa "VALPO")
    "STGO",  # Santiago
    "RCGA",  # Rancagua (también se usa "RANC")
    "TAL",  # Talca
    "CHILL",  # Chillán
    "CCP",  # Concepción
    "TEM",  # Temuco
    "VALD",  # Valdivia
    "PMO",  # Puerto Montt (también se usa "PTOM")
    "COY",  # Coyhaique
    "PA"  # Punta Arenas
]


formas_corte_apelaciones = [
    "C.A.",
    "CA",
    "Corte Apel.",
    "Ilma. C.A.",
    "Ilustrísima Corte de Apelaciones",
    "Excelentísima Corte de Apelaciones",
    "Corte de Apelaciones de",
    "Corte de",
    "Apelaciones de",
    "Tribunal de Apelaciones"
]

variaciones_recurrente_recurrida = [
    "Recurrida",
    "Recurrente",
    "Rte.",  
    "Rcta.",  
    "Rcte.",  
    "Rcrte.", 
    "Rcrda.",  
    "Recurrda",  
    "Recurr.",  
    "Rdo.",  
    "Rda.", 
    "Recur.",  
    "Demandante recurrente",
    "Demandado recurrente",
    "Apelante",
    "Impugnante"
]


variaciones_inhabilidad = [
    "Inhab.",
    "Inh.",
    "Inhb.",
    "Inhabil.",
    "Inhabl.",
    "Inhabilid.",
    "Inhbd.",
    "Inhblt.",
    "Inhabilit.",
    "Inabilidad",
    "Inab.",

]


variaciones_apercibe = [
    "Apercibe",
    "Apercibimiento",
    "Aperc.",
    "Apc.",
    "Aper.",
    "Apcb.",
    "Apercb.",
    "Apercib.",
    "Apercibim.",
    "Apercbmto."
]

nombres_ = [
    "Mateo", "Sofía", "Benjamín", "Isabella", "Santiago", 
    "Catalina", "Lucas", "Valentina", "Maximiliano", "Emilia",
    "Diego", "Florencia", "Tomás", "Antonia", "Joaquín",
    "María Paz", "Vicente", "Camila", "Martín", "Agustina"
]

apellidos_ = [
    "González", "Muñoz", "Rojas", "Díaz", "Pérez",
    "Soto", "Contreras", "Silva", "Martínez", "Araya",
    "Sepúlveda", "Morales", "Rodríguez", "López", "Fuentes",
    "Torres", "Hernández", "Espinoza", "Castillo", "Flores"
]



abreviaciones_tengase = [
    "Téngase",         
    "Tgse.",            
    "Tgs.",             
    "Tngse.",           
    "Tng.",             
    "Téng.",            
    "Tse.",             
    "Teng.",            
    "Tgsa.",            

]


abreviaciones_tp = [

    "Téngase presente", 
    "T.P.",            
    "Tgse. pres.",      
    "Teng. pres.",     
    "Téngase por",      
    "T.Por",            
    "Tgse. por",        
    "Teng. por"         
]
peticion = [
  "Petición",
    "Pet.",
    "Ptcn.",
    "Ptn.",
    "Pide",
    "Pde.",
    "Pd.",
    "Solicita",
    "Sol.",
    "Scta.",
    "Solicitud",
    "Solcd.",
    "Scd.",
    "Requiere",
    "Req.",
    "Rqre.",
    "Demanda",
    "Dda.",
    "Peticiona",
    "Ptcna.",
    "Exige",
    "Exg.",
    "Petic.",
    "Solic."
]

conceptos = ['costos', 'valores', 'tarifas', 'precios', 'cotizaciones']
medidas = ['UTM', 'UF', 'pesos', 'dólares', 'unidades']
valores = ['100.000', '200.000', '300.000', '400.000', '500.000', '3', '5', '7', '10', '15']
cortes = ['Santiago', 'Concepción', 'Ccp', 'stgo', 'Arica', 'Puerto Montt', 'Punta Arenas']


motivos = [
    'falta de pruebas',
    'error procesal',
    'desistimiento',
    'prescripción',
    'incumplimiento de cobertura por parte de la isapre',
    'negativa de trámite por parte de la isapre',
    'falta de información proporcionada por la isapre',
    'aumento injustificado de costos por la isapre',
    'discrepancia en el cálculo de planes por la isapre',
    'incumplimiento de plazos administrativos por la isapre',
    'por no dar cumplimiento a lo solicitado'
    
]
recursos = ['recurso', 'demanda', 'apelación', 'solicitud', 'acción', 'la presente acción']


def variar_frase(abrev_corte, corte_apelaciones_var, cortes, abrev_tp, nombres, apellidos):

    variaciones_acuerdo = [
        f"Estése a la disponibilidad de esta corte de apelaciones de {abrev_corte} a su ingreso y prioridad.",
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
        "Al folio 52: por cumplido lo ordenado, rija el estado de acuerdo.",
    ]
    return random.choice(variaciones_acuerdo)

def generar_frase_aleatoria():

    abrev_corte = random.choice(abreviaciones_cortes)
    corte_apelaciones_var = random.choice(formas_corte_apelaciones)
    cortes = random.choice(cortes_de_chile)
    abrev_tp = random.choice(abreviaciones_tp)
    nombres = random.choice(nombres_)
    apellidos = random.choice(apellidos_)
  
    return variar_frase(abrev_corte, corte_apelaciones_var, cortes, abrev_tp,nombres, apellidos )

# Generar varias frases para la clase "Acuerdo"
frases_acuerdo = [generar_frase_aleatoria() for _ in range(200)]
print(frases_acuerdo[:10])



# Función para generar variaciones de frases de apercibimiento
def variar_frase_apercibe(apercibe_var, parte_var):
    # Lista de plantillas de frases con variaciones
    variaciones = [
        f"Para apercibe hace efectivo {apercibe_var} a {parte_var}.",
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
    apercibe_var = random.choice(variaciones_apercibe)
    parte_var = random.choice(variaciones_recurrente_recurrida)
    return variar_frase_apercibe(apercibe_var, parte_var)

frases_apercibe = [generar_frase_apercibe() for _ in range(200)]


print(frases_apercibe[:10])


# Función para generar variaciones de frases de fallo/desestima
def variar_frase_fallo(abrev_tengase, corte_apelaciones_var):
    variaciones = [
        f"{abrev_tengase} desestimado el recurso.",
        f"{abrev_tengase} desestimada por no cumplir lo solicitado por la {corte_apelaciones_var}.",
        f"{abrev_tengase} desestimado.",
        "Se desestima el recurso.",
        f"{abrev_tengase} desestimado pb.",
        f"{abrev_tengase} desestimada el recurso ges.",
        f"{abrev_tengase} prima extraordinaria."
    ]
    return random.choice(variaciones)

# Función para generar una frase aleatoria de fallo/desestima
def generar_frase_fallo():
    abrev_tengase = random.choice(abreviaciones_tengase)
    corte_apelaciones_var = random.choice(formas_corte_apelaciones)
    return variar_frase_fallo(abrev_tengase, corte_apelaciones_var)

# Generar varias frases para la clase "Fallo"
frases_fallo_resultado = [generar_frase_fallo() for _ in range(200)]

# Mostrar las primeras 10 frases generadas
print(frases_fallo_resultado[:10])



# FIJA COSTAS

def variar_frase(concepto, medida, valor, corte):
    variaciones = [
        # Variaciones con nombres de Cortes de Apelaciones
        f'La Corte de Apelaciones de {corte} fija los {concepto} en {valor} {medida}.',
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
    concepto = random.choice(conceptos)
    medida = random.choice(medidas)
    valor = random.choice(valores)
    corte = random.choice(cortes)
    return variar_frase(concepto, medida, valor, corte)

# Generar varias frases aleatorias
frases_fijacion = [generar_frase_aleatoria() for _ in range(200)]
print(frases_fijacion[:10])






infracciones = [
    'no cumplir con la normativa migratoria',
    'infringir leyes laborales',
    'falta de seguridad laboral',
    'incumplimiento de normas de protección al consumidor',
    'contaminación ambiental',
    'infracciones viales graves',
    'incumplimiento en entrega de información a afiliados de isapres',
    'negativa injustificada de cobertura por parte de isapres',
    'aumento desproporcionado de planes de isapres',
    'falta de transparencia en contratos de isapres',
    'no cumple lo ordenado'
]

rangos_utm = [
    'de 10 a 50 UTM',
    'de 50 a 100 UTM',
    'de 1 a 10 UTM',
    'de 20 a 200 UTM',
    'de 5 a 25 UTM',
    'de 1 a 5 UTM',
    'de 100 a 300 UTM',
    'de 500 a 1000 UTM'
]

def variar_frase(infraccion, rango, corte):
    variaciones = [
        f'La {corte} impone una multa de {rango}'
        f'La multa por {infraccion} es de {rango}.',
        f'La multa por {infraccion}, es de {rango}.',
        f'La multa por {infraccion} (de {rango}) será aplicada.',
        f'La multa por {infraccion}  es de {rango}.',
        f'Se impuso una multa de {rango} por {infraccion}.',
        f'Por {infraccion}, se sancionó con una multa de {rango}.',
        f'Por {infraccion}, se multó con un rango de {rango}.',
        f'El monto de la multa por {infraccion} será de {rango}.',
        f'La infracción de {infraccion} conlleva una multa de {rango}.',
        f'Debido a {infraccion}, se determinó una multa de {rango}.',
        f'La sanción por {infraccion} consiste en una multa de {rango}.',
        f'Por {infraccion}, se establece una multa de {rango}.',
        f'Se aplicará una multa de {rango} por {infraccion}.',
        f'Por no cumplir con {infraccion}, la multa es de {rango}.',
        f'La multa por la infracción de {infraccion} asciende a {rango}.',
        f'La comisión de {infraccion} se multa con {rango}.',
        # Incluyendo errores comunes
        f'La multa por {infraccion} es de {rango}',  
        f'Se impuso una multa de {rango} por {infraccion}'
    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    infraccion = random.choice(infracciones)
    rango = random.choice(rangos_utm)
    corte = random.choice(formas_corte_apelaciones)
    return variar_frase(infraccion, rango, corte)

# Generar varias frases aleatorias
frases_multa = [generar_frase_aleatoria() for _ in range(300)]
print(frases_multa[:10])





def variar_frase(peticion, corte, recurrente, var_corte):
    variaciones = [
        f'No ha lugar lo {peticion}',
        f'NHL {peticion}',
        f"Se rechaza lo {peticion} por la {recurrente} en la {corte}.",
        f"Se niega lo solicitado por la {recurrente} en la {corte}.",
        f"No ha lugar a la {peticion} de la {recurrente} en la {corte}.",
        f"Se desestima la solicitud de la {recurrente} presentada en la {corte}.",
        f"La {corte} rechaza lo {peticion} por la {recurrente}.",
        f"No se da lugar a lo {peticion} por la {recurrente} en la {corte}.",
        f"Se deniega la solicitud de la {recurrente} en la {corte}.",
        f"La solicitud presentada por la {recurrente} ha sido rechazada en la {corte}.",
        f"La {corte} ha decidido no dar lugar a lo solicitado por la {recurrente}.",
        f"La {corte} {var_corte} ha decidido no dar lugar a lo solicitado por la {recurrente}."


    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    peticion_sel = random.choice(peticion)
    corte_sel = random.choice(formas_corte_apelaciones)
    recurrente_sel = random.choice(variaciones_recurrente_recurrida)
    var_corte_sel = random.choice(abreviaciones_cortes)
    return variar_frase(peticion_sel, corte_sel, recurrente_sel, var_corte_sel)

# Generar varias frases aleatorias
frases_fallo_desestima = [generar_frase_aleatoria() for _ in range(300)]
print(frases_fallo_desestima[:10])




solicitudes = ['presentar pruebas', 'comparecer', 'notificar', 'cumplir con la orden judicial', 'pagar la fianza','dar cumplimiento']

def variar_frase(parte, solicitud, tengase, corte):
    variaciones = [
        f'Prescinde de la {parte}, por no {solicitud}.',
        f'Prescinde de la {parte} por no {solicitud}.',
        f'Prescinden, de la {parte}, por no {solicitud}.',
        f'Prescinden (de la {parte}) por no {solicitud}.',
        f'Prescinden  de la {parte} por no {solicitud}.',
        f'La corte prescinde de la {parte} por no {solicitud}.',
        f'Se prescinde, de la {parte}, por no {solicitud}.',
        f'{tengase}  (de la {parte}) por no {solicitud}.',
        f'La {corte} prescinde  de la {parte} por no {solicitud}.',
        f'La corte ha prescindido de la {parte} por no {solicitud}.',
       f'La ica ha prescindido de la {parte} por no {solicitud}.',
        f'La ica de santiago ha prescindido de la {parte} por no {solicitud}.',


    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    parte = random.choice(partes)
    solicitud = random.choice(solicitudes)
    tgse = random.choice(solicitudes)
    corte_sel = random.choice(cortes)

    return variar_frase(parte, solicitud, tgse, corte_sel)

# Generar varias frases aleatorias
frases_prescinde = [generar_frase_aleatoria() for _ in range(300)]
frases_prescinde[:10]




def variar_frase(item, motivo, tgse):
    variaciones = [
        # Correctas
        f'{tgse} retirado',
        f'Retira el {item}, por {motivo}.',
        f'Retira el {item}, por {motivo}.',
        f'El recurrido retira {item}, por {motivo}.',
        f'Retira el {item} por {motivo}.',
        f'Retira (el {item}) por {motivo}.',
        f'Retira  el {item} por {motivo}.',
        f'El {item} es retirado por {motivo}.',
        f'El {item} es retirado, por {motivo}.',
        f'El {item} es retirado (por {motivo}).',
        f'El {item} es retirado  por {motivo}.',
        f'Se ha retirado el {item} por {motivo}.',
        f'Se ha retirado, el {item}, por {motivo}.',
        f'Por {motivo}, se retira el {item}.',
        f'El {item} fue retirado debido a {motivo}.',
        f'La parte retira el {item} por {motivo}.',
        f'Retira el {item}, por {motivo}',  
        f'El recurrido retira {item}, por {motivo}',  
        f'Retira el {item} por {motivo}',  
        f'Retira (el {item}) por {motivo}',  
        f'Retira  el {item} por {motivo}',  
        f'El {item} es retirado por {motivo}',  
        f'El {item} es retirado, por {motivo}',  
        f'El {item} es retirado (por {motivo})', 
        f'El {item} es retirado  por {motivo}',  
        f'Se ha retirado el {item} por {motivo}',  
        f'Se ha retirado, el {item}, por {motivo}', 
        f'Por {motivo}, se retira el {item}', 
        f'El {item} fue retirado debido a {motivo}',  
        f'La parte retira el {item} por {motivo} '
    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    recurso = random.choice(recursos)
    motivo = random.choice(motivos)
    tgse = random.choice(abreviaciones_tengase)
    return variar_frase(recurso, motivo, tgse)

# Generar varias frases aleatorias
frases_retira = [generar_frase_aleatoria() for _ in range(300)]
print(frases_retira[:10])



def variar_frase(item, motivo, tgse):
    variaciones = [
        f'{tgse} archivado el recurso'
        f'El {item} se archiva por {motivo}.',
        f'El {item} ha sido archivado por {motivo}.',
        f'Se archiva el {item} debido a {motivo}.',
        f'Por {motivo}, se archiva el {item}.',
        f'El {item} es archivado por {motivo}.',
        f'El {item} se ha archivado por {motivo}.',
        f'Debido a {motivo}, el {item} se archiva.',
        f'El {item} se encuentra archivado por {motivo}.',
        f'La {item} se archiva por {motivo}.',
        f'El {item} fue archivado por {motivo}.',
        f'Por {motivo}, el {item} se archivó.',
        f'El archivo del {item} se debe a {motivo}.',
        f'El {item} pasó a archivo por {motivo}.',
        f'El proceso del {item} se archivó por {motivo}.',
        f'El {item} se archiva por {motivo}', 
        f'El {item} ha sido archivado por {motivo}', 
        f'Se archiva el {item} debido a {motivo}',  
        f'Por {motivo}, se archiva el {item}',  
        f'El {item} es archivado por {motivo}', 
        f'El {item} se ha archivado por {motivo}',  
        f'Debido a {motivo}, el {item} se archiva', 
        f'El {item} se encuentra archivado por {motivo}', 
        f'La {item} se archiva por {motivo} ',
        f'El {item}se archiva por {motivo}'
    ]
    return random.choice(variaciones)

def generar_frase_aleatoria():
    recurso = random.choice(recursos)
    motivo = random.choice(motivos)
    tgse = random.choice(abreviaciones_tengase)

    return variar_frase(recurso, motivo, tgse)



# Generar varias frases aleatorias
frases_archivo = [generar_frase_aleatoria() for _ in range(200)]
print(frases_archivo[:10])

# Genera un número aleatorio de 3 dígitos
def generar_num_3():
    return str(random.randint(100, 999))

# Genera un número aleatorio de 4 dígitos
def generar_num_4():
    return str(random.randint(2000, 2050))

# Genera roles en el formato xxx-yyyy
def generar_rol():
    return f"{generar_num_3()}-{generar_num_4()}"

def generar_frase_aleatoria():
    rol1 = generar_rol()
    rol2 = generar_rol()
    abreviaturas = ['Acum.', 'Acumula', 'Acum. a', 'Se acumula a', 'Acumulado a', 'acumúlese', 'tengase por acumulado', 'tgse acumla', 'tp acum0']
    abreviatura = random.choice(abreviaturas)  # Escoge una sola abreviatura
    variaciones = [
        f'{abreviatura} {rol1} con {rol2} de la corte de {random.choice(cortes_de_chile)}.',
        f'{abreviatura} {rol1}, con {rol2} de la corte de {random.choice(abreviaciones_cortes)}',
        f'{random.choice(cortes_de_chile)} {abreviatura} {rol1} (con {rol2}).',
        f'{abreviatura} {rol1}  con {rol2}.',
        f'El rol {rol1} {abreviatura} {rol2}.',
        f'El rol {rol1}, {abreviatura} {rol2}.',
        f'El rol {rol1} ({abreviatura} {rol2}).',
        f'El rol {rol1}  {abreviatura} {rol2}.',
    ]
    return random.choice(variaciones)

# Generar 10 frases aleatorias
frases_acumula = [generar_frase_aleatoria() for _ in range(300)]
frases_acumula[:10]
