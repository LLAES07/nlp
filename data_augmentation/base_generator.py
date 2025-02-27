
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




acciones = ['demanda', 'recurso', 'solicitud', 'apelación', 'petición' ]



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

solicitudes = ['presentar pruebas', 'comparecer', 'notificar', 'cumplir con la orden judicial', 'pagar la fianza','dar cumplimiento']


recursos_ica = [
    'ICA',
    'Corte de Apelaciones',
    'C.A.',
    'Tribunal',
    'Corte',
    'El tribunal competente',
    'La Corte de Apelaciones',
    'El órgano jurisdiccional',
    'La autoridad judicial',
    'El juzgado de alzada',
]

acciones_ica = [
    'informar el domicilio contractual y el FUN actualizado del recurrente dentro de 05 días',
    'presentar el FUN contractual actualizado',
    'solicitar el cumplimiento de la sentencia dentro del plazo establecido',
    'presentar los documentos requeridos para la resolución del caso',
    'aclarar los hechos relacionados con el incumplimiento de la sentencia',
    'presentar pruebas adicionales que respalden la demanda',
    'informar sobre el estado actual del cumplimiento de la sentencia',
]

motivos_ica = [
    'para verificar el cumplimiento de la sentencia',
    'para garantizar la transparencia del proceso',
    'para asegurar el cumplimiento de los plazos legales',
    'para resolver discrepancias en la documentación presentada',
    'para aclarar aspectos no definidos en la resolución',
    'para garantizar el derecho a la defensa de las partes',
    'para evaluar la situación actual del caso',
]

cumplase_ = [

    'cúmplase',
    'cúmplase cs',
    'cúmplase corte suprema',
    'c.s.',
    'c.s',
    'Cump',
    "C/se" 

]
acciones =[
    'confirma',
    'revoca',
    'omite',
    'incompetencia',
    'litis pendencia'
]


decisiones_rechaza = [
    ('rechaza', 'con costas'),
    ('rechaza', 'sin costas'),
    ('rechaza', 'con costas al demandante'),
    ('rechaza', 'con costas al demandado'),
    ('rechaza', 'con costas repartidas'),
]

motivos_rechaza = [
    'falta de pruebas',
    'error procesal',
    'falta de fundamento',
    'extemporaneidad',
    'carecer de interés legítimo',
    'incumplimiento de cobertura por parte de la isapre',
    'negativa de trámite por parte de la isapre',
    'falta de información proporcionada por la isapre',
    'aumento injustificado de costos por la isapre',
    'discrepancia en el cálculo de planes por la isapre',
    'incumplimiento de plazos administrativos por la isapre',
    'no cumplir lo estipulado en el plan'
]


causales = [
    'por parentesco con la parte interesada',
    'por haber intervenido en el caso previamente',
    'por amistad íntima con el acusado',
    'por recibir beneficios de una de las partes',
    'por haber emitido opinión pública sobre el caso',
    'por tener interés directo en el resultado del proceso'
]

profesiones = [
    'ministro de la Corte Suprema',
    'juez de la Corte de Apelaciones',
    'abogado defensor',
    'fiscal',
    'abogado integrante',
    'ministro de tribunal de alzada'
]


nombres = ['Pairican', 'González', 'Muñoz', 'Valenzuela', 'Sepúlveda', 'Rodríguez', 'Pérez', 'Silva', 'Contreras', 'Fuentes']
titulos = ['Sr.', 'Sra.', 'Don', 'Doña', 'Ministro', 'Ministra', 'Juez', 'Jueza', 'Abogado', 'Abogada', 'Ministro', 'Ministra', 'Presidente', 'Pdte']