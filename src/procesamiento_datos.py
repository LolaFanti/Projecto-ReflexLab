def  filtrar_por_participante (df, id_buscado) :
    """
    Filtra los registros de un participante específico a partir de una lista de datos.

    Parameters:
    ----------
        lista (list): Lista de diccionarios con los datos de los participantes.
        id_buscado (int): Identificador del participante a filtrar.

    Returns:
    ----------
        dict: Diccionario con el id del participante y sus registros asociados.

    Raises:
    ----------
        ValueError: Si el id del participante no se encuentra en la lista.
    """
    df_filtrado = df[df["id"] == id_buscado] #hace una serie de booleanos, y devuelve solo las filas True.

    if len(df_filtrado) == 0:

        raise ValueError("El ID del participante no está en el archivo")

    return df_filtrado

        