
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

inadmisible_formas = [
    "Inadmisible"
    "inadmis.",  # forma habitual con punto
    "inadm.",    # versión más corta, también con punto
    "inad.",     # abreviación más reducida
    "inadm",      # sin punto, menos formal pero usada en ciertos contextos
    "inadmisible",   # confusión en la colocación de la 's'
    "inadmisivle",   # error en el orden de las letras
    "inadmisble",    # omisión de la 'i' en la sílaba "isi"
    "inadmisisble",  # adición extra de una 'is'
    "inadmibible"    # error al sustituir la 's' por 'b'
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
acciones_cs =[
    'confirma',
    'revoca',
    'omite',
    '/incompetencia',
    'litis pendencia',
    'confirmada con costas',
    'revocada si costas',
    'revocada acogiendo el plan'
    'revocada sin referirse al plan de salud'
]

resoluciones_acoge = ["con costas", "sin costas", "con costas parciales", 'sin costas', 's/ costas', 'no costas', 'no se pronuncia por costas']

isapres = ["Isapre Banmédica", "Isapre Colmena", "Isapre Cruz Blanca", 'Nueva Mas Vida S.A.', 'NMV']

pronunciamientos = ["otorgue la cobertura", "no aplique alza", "mantenga las condiciones", 'restituir los cobros alegados', 'mantener el plan de salud', 'devolver excendentes']

planes = ["Plan GES", "Plan Base", "Plan Complementario", 'PB', 'TF', 'TFRN2']

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
    'no cumplir lo estipulado en el plan',
    'no adjuntar los documentos solicitados',
    'pasar del plazo judicial'
]

oni_variaciones = [

    'ONI',
    'o.n.i',
    'oni.',
    'o.n.i.',
    'Orden de no innovar',
    'ordern de no innonvar'
]
variaciones_dese_cuenta = [
    "Dese cuenta",
    "dc cuenta",
    "d cuenta",
    "d/cta",
    "d. cuenta",
    "d-cuenta",
    "d cta",
    "dc. cuenta",
    "des cuenta",
    "dse cuenta",
    "dcta"
]

variaciones_no_ha_lugar = [
    "No ha lugar",      # Forma correcta
    "no ha lugar",      # En minúsculas
    "No Ha Lugar",      # Con mayúsculas en cada palabra
    "NHL",              # Abreviatura en mayúsculas
    "nhl",              # Abreviatura en minúsculas
    "N.H.L.",           # Abreviatura con puntos
    "n.h.l.",           # Abreviatura en minúsculas con puntos
    "no h a lugar",     # Error común: separación incorrecta
    "no ha lugáor",     # Error de tipeo: letra de más o mal ubicada
    "no ha lugor",      # Error: omisión de la "a" en "lugar"
    "no ha lgar",       # Error: omisión de la "u"
]

motivos_inadmisible = [
    "No cumplir lo ordenado por la corte.",
    "Presentación extemporánea del recurso.",
    "Falta de fundamentación jurídica adecuada.",
    "Incumplimiento de requisitos formales establecidos.",
    "Falta de interés legítimo o parte afectada.",
    "Duplicidad del recurso o presentación reiterada sin novedad.",
    "No haber agotado la vía administrativa previa, cuando fuera obligatorio.",
    "Incompetencia del tribunal para conocer el recurso.",
    "Error en la presentación o tramitación del expediente.",
    "Inexistencia de legitimación activa o pasiva en el demandante."
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



concede_apelacion_motivos = [
    'Plan pago',
    'pb',
    'ges',
    'prima extra    ordinaria'
]


certifiquese = [

    'certifiquese',
    'cert.',
    'certifíquese', 
    'certi.',
    'certificación',
    'se certifica',
    'certif.',
    'cfrt.',
    
]