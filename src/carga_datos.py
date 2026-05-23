import pandas as pd

from src.validacion_datos import (convertir_columnas_numericas, verificar_positivo, validar_go_nogo, validar_respuesta, validar_tiempos_crecientes)

def cargar_datos(ruta_archivo):
    """
  
    Carga los datos desde un archivo CSV, parsea cada línea y construye una lista de registros.
    
    Parameters:
    ----------
        ruta_archivo (str): Ruta del archivo a leer, sin la extensión ".csv".

    Returns:
    ----------
        list: Lista de diccionarios con los registros cargados.

    Raises:
    ----------
        FileNotFoundError: Si el archivo no puede abrirse.
        ValueError: Si el archivo está vacío, si no hay registros válidos
            o si los tiempos de inicio de un participante no están en orden creciente.
        TypeError: Si ocurre un error en la conversión de los datos al tipo correspondiente.
    """
    try:
        df = pd.read_csv(ruta_archivo + ".csv", header=None)#Esto porque los arachivos que nos mando marcos no tienen nombre las columnas
        df.columns = ["id","trial","estimulo","tiempo_inicio","respuesta","tiempo_reaccion","resultado_respuesta","condicion"] 
        #renombra las columnas(que l)
    except FileNotFoundError:
        raise FileNotFoundError("Archivo no encontrado")
        
    if df.empty:
        raise ValueError("El archivo está vacío")

    
    convertir_columnas_numericas(df,["trial", "tiempo_inicio", "tiempo_reaccion"])
        

    verificar_positivo(df, "trial")
    verificar_positivo(df, "tiempo_inicio")
    verificar_positivo(df, "tiempo_reaccion")

    validar_go_nogo(df)
    validar_respuesta(df)

    validar_tiempos_crecientes(df)

    return df
