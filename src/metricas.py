
def calcular_tiempo_reaccion_promedio(df_participante):
    """
    Calcula el promedio del tiempo de reacción de un participante.

    Parameters:
    ----------
        participante_diccio (dict): Diccionario con los datos del participante,
        que contiene una lista de registros bajo la clave "datos".

    Returns:
    ----------
        float: El promedio del tiempo de reacción.
        str: Mensaje indicando que no hay datos si la lista está vacía.
    """
    
    if df_participante.empty:
       return "No hay datos para calcular promedio"

    return df_participante["tiempo_reaccion"].mean()

    
    
def calcular_tasa_error(df_participante):
    """
    Calcula la proporción de respuestas incorrectas de un participante.

    Args:
        participante_diccio (dict): Diccionario con los datos del participante,
        que contiene una lista de registros bajo la clave "datos".

    Returns:
        float: Proporción de respuestas incorrectas.
        str: Mensaje indicando que no hay datos si la lista está vacía.
    """
   
    if df_participante.empty:
        return "No hay datos para calcular tasa de error"

    errores = df_participante["resultado_respuesta"] == "incorrecto" #queda como una columna de True y False

    return errores.mean()





    
