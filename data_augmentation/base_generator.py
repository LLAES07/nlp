
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
acciones = ['demanda', 'recurso', 'solicitud', 'apelación', 'petición']



infracciones = [
    'no cumplir lo ordenado por SIS',
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
