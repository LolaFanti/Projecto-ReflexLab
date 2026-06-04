import pandas as pd

from src.validacion_datos import (convertir_columnas_numericas, verificar_positivo, validar_go_nogo, validar_respuesta, validar_tiempos_crecientes)

def cargar_datos(ruta_archivo):
    """
    Carga un archivo CSV y valida el contenido de sus datos.
    
    Parameters
    ----------
    ruta_archivo : str o file-like object
        Ruta del archivo CSV o archivo cargado por el usuario.
    
    Returns
    -------
    pd.DataFrame
        DataFrame con los datos cargados y validados.
    
    Raises
    ------
    FileNotFoundError
        Si el archivo no puede abrirse.
    ValueError
        Si el archivo está vacío, contiene valores inválidos
        o los tiempos no están en orden creciente.
    TypeError
        Si alguna columna que debe ser numérica contiene
        valores no numéricos.
    """
    try:
        df = pd.read_csv(ruta_archivo, header=None)#Esto porque los arachivos que nos mando marcos no tienen nombre las columnas
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
