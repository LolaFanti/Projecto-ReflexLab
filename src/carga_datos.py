import pandas as pd

from src.validacion_datos import (validar_columnas, convertir_columnas_numericas, verificar_positivos, validar_go_nogo, validar_respuesta, validar_tiempos_crecientes)

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
        df = pd.read_csv(ruta_archivo + ".csv")
    except FileNotFoundError:
        raise FileNotFoundError("Archivo no encontrado")
        
    if df.empty:
        raise ValueError("El archivo está vacío")

    
    columnas_esperadas = [
        "id",
        "trial",
        "estimulo",
        "tiempo_inicio",
        "respuesta",
        "tiempo_reaccion",
        "resultado_respuesta",
        "condicion"]


    validar_columnas(df, columnas_esperadas)
    
    convertir_columnas_numericas(df,["trial", "tiempo_inicio", "tiempo_reaccion"])
        

    verificar_positivos(df, "trial")
    verificar_positivos(df, "tiempo_inicio")
    verificar_positivos(df, "tiempo_reaccion")

    validar_go_nogo(df)
    validar_respuesta(df)

    validar_tiempos_crecientes(df)

    return df
