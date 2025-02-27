import Acuerdo, Acumula, Apercibe,  Archivo, Cs, Fallo_Desestima, Fija_Costas, Ica_Solicita_Diligencia, Inhabilidad, Inicio_tramitacion, Multa, Omite, Rechazada, Retira, TP



def main():
    # Generamos datasets de cada archivo
    data_acuerdo = Acuerdo.generar_dataset(300)
    data_acumula = Acumula.generar_dataset(300)
    data_apercibe = Apercibe.generar_dataset(300)
    data_archivo = Archivo.generar_dataset(300)
    data_cs = Cs.generar_dataset(300)
    data_fallo_desestima =Fallo_Desestima.generar_dataset(300)
    data_fija_costas = Fija_Costas.generar_dataset(300)
    data_ica_solicita = Ica_Solicita_Diligencia.generar_dataset(300)
    data_inhabilidad = Inhabilidad.generar_dataset(300)
    data_inicio_tramitacion = Inicio_tramitacion.generar_dataset(300)
    data_multa = Multa.generar_dataset(300)
    data_omite =Omite.generar_dataset(300)
    data_rechazada =Rechazada.generar_dataset(300)
    data_retira = Retira.generar_dataset(300)
    data_tp = TP.generar_dataset(300)

    all_data = [
        data_acuerdo + data_acumula + data_apercibe + data_archivo + data_cs + data_fallo_desestima, data_fija_costas, 
        data_ica_solicita, data_inhabilidad,data_inicio_tramitacion, data_multa, data_omite, data_rechazada, data_retira, data_tp]
    return all_data


if __name__ == "__main__":
    object = main()
    print(object[:100])
