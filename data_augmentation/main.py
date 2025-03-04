# main.py (dentro de data_augmentation)

import pandas as pd
import random
import numpy as np
# Importa cada archivo usando data_augmentation como paquete
from . import Acuerdo
from . import Acumula
from . import Apercibe
from . import Archivo
from . import Cs
from . import Fallo_Desestima
from . import Fija_Costas
from . import Ica_Solicita_Diligencia
from . import Inhabilidad
from . import Inicio_tramitacion
from . import Multa
from . import Omite
from . import Rechazada
from . import Retira
from . import TP
from . import Incompetencia
from . import NHL
from . import Oni
from . import Prescinde
from . import Concede_apelacion
from . import Art_numeral as Articulo
from . import Acoge as Acogida
from . import Certifiquese
from . import Dese_cuenta
from . import Ica_Informa
from . import Agreguese
from . import Evacuainforme
from . import Admisible

from . import Ica_amplia_plazo

def main():

    # Generar datasets
    data_acuerdo = Acuerdo.generar_dataset(300)
    data_acumula = Acumula.generar_dataset(300)
    data_apercibe = Apercibe.generar_dataset(300)
    data_archivo = Archivo.generar_dataset(300)
    data_cs = Cs.generar_dataset(300)
    data_fallo_desestima = Fallo_Desestima.generar_dataset(300)
    data_fija_costas = Fija_Costas.generar_dataset(300)
    data_ica_solicita = Ica_Solicita_Diligencia.generar_dataset(300)
    data_inhabilidad = Inhabilidad.generar_dataset(300)
    data_inicio_tramitacion = Inicio_tramitacion.generar_dataset(300)
    data_multa = Multa.generar_dataset(300)
    data_omite = Omite.generar_dataset(300)
    data_rechazada = Rechazada.generar_dataset(300)
    data_retira = Retira.generar_dataset(300)
    data_tp = TP.generar_dataset(300)
    data_incompetencia = Incompetencia.generar_dataset(300)
    data_nhl = NHL.generar_dataset(300)
    data_oni = Oni.generar_dataset(300)
    data_prescinde = Prescinde.generar_dataset(300)
    data_concede_apelacion = Concede_apelacion.generar_dataset(300)
    data_articulo = Articulo.generar_dataset(300)
    data_acoge = Acogida.generar_dataset(300)
    data_certifiquese = Certifiquese.generar_dataset(300)
    data_dese_cuenta = Dese_cuenta.generar_dataset(300)
    data_ica_informa = Ica_Informa.generar_dataset(200)
    data_ica_agrega = Agreguese.generar_dataset(100)
    data_evacua_informe = Evacuainforme.generar_dataset(100)
    data_admisible = Admisible.generar_dataset(30)
    data_amplia_plazo = Ica_amplia_plazo.generar_dataset(30)


    # Dataframes por cada clase
    dfs = []
    dfs.append(pd.DataFrame({'frase': data_acuerdo, 'etiqueta': 'Acuerdo'}))
    dfs.append(pd.DataFrame({'frase': data_acumula, 'etiqueta': 'Acumulación'}))
    dfs.append(pd.DataFrame({'frase': data_apercibe, 'etiqueta': 'Apercibe'}))
    dfs.append(pd.DataFrame({'frase': data_archivo, 'etiqueta': 'Archivado'}))
    dfs.append(pd.DataFrame({'frase': data_cs, 'etiqueta': 'Cs'}))
    dfs.append(pd.DataFrame({'frase': data_fallo_desestima, 'etiqueta': 'Fallo/Desestima'}))
    dfs.append(pd.DataFrame({'frase': data_fija_costas, 'etiqueta': 'Fija Costas'}))
    dfs.append(pd.DataFrame({'frase': data_ica_solicita, 'etiqueta': 'Ica Solicita Diligencia'}))
    dfs.append(pd.DataFrame({'frase': data_inhabilidad, 'etiqueta': 'Inhabilidad'}))
    dfs.append(pd.DataFrame({'frase': data_inicio_tramitacion, 'etiqueta': 'Inicio Tramitación'}))
    dfs.append(pd.DataFrame({'frase': data_multa, 'etiqueta': 'Multa'}))
    dfs.append(pd.DataFrame({'frase': data_omite, 'etiqueta': 'Inadmisible/Omite'}))
    dfs.append(pd.DataFrame({'frase': data_rechazada, 'etiqueta': 'Rechazada'}))
    dfs.append(pd.DataFrame({'frase': data_retira, 'etiqueta': 'Retira'}))
    dfs.append(pd.DataFrame({'frase': data_tp, 'etiqueta': 'Téngase Presente'}))
    dfs.append(pd.DataFrame({'frase': data_incompetencia, 'etiqueta': 'Incompetencia'}))
    dfs.append(pd.DataFrame({'frase': data_nhl, 'etiqueta': 'Nhl'}))
    dfs.append(pd.DataFrame({'frase': data_oni, 'etiqueta': 'Oni'}))
    dfs.append(pd.DataFrame({'frase': data_prescinde, 'etiqueta': 'Prescinde'}))
    dfs.append(pd.DataFrame({'frase': data_concede_apelacion, 'etiqueta': 'Concede Apelación'}))
    dfs.append(pd.DataFrame({'frase': data_articulo, 'etiqueta': 'Art / Numeral'}))
    dfs.append(pd.DataFrame({'frase': data_acoge, 'etiqueta': 'Acoge'}))
    dfs.append(pd.DataFrame({'frase': data_certifiquese, 'etiqueta': 'Certifiquese'}))
    dfs.append(pd.DataFrame({'frase': data_dese_cuenta, 'etiqueta': 'Dese Cuenta'}))
    dfs.append(pd.DataFrame({'frase': data_ica_informa, 'etiqueta': 'Ica Informa'}))
    dfs.append(pd.DataFrame({'frase': data_ica_agrega, 'etiqueta': 'Agréguese A Tabla'}))
    dfs.append(pd.DataFrame({'frase': data_evacua_informe, 'etiqueta': 'Evacua Informe'}))
    dfs.append(pd.DataFrame({'frase': data_admisible, 'etiqueta': 'Admisibles'}))
    dfs.append(pd.DataFrame({'frase': data_amplia_plazo, 'etiqueta': 'Ica Amplia Plazo'}))


    # Concatenar, eliminar duplicados y barajar
    df_total = pd.concat(dfs, ignore_index=True)
    df_unicos = df_total.drop_duplicates(subset=['frase'])
    df_final = df_unicos.sample(frac=1, random_state=42).reset_index(drop=True)

    return df_final

if __name__ == "__main__":
    df_resultado = main()
    print(df_resultado.head(10))
    print(df_resultado['etiqueta'].value_counts())
