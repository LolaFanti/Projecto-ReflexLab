def  filtrar_por_participante (df, id_buscado) :
    """
    Filtra los registros correspondientes a un participante específico.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contiene los datos de todos los participantes.
    id_buscado : int
        Identificador del participante a filtrar.
    
    Returns
    -------
    pd.DataFrame
        DataFrame que contiene únicamente los registros del
        participante seleccionado.
    
    Raises
    ------
    ValueError
        Si el ID del participante no se encuentra en el DataFrame.
    """
    df_filtrado = df[df["id"] == id_buscado] #hace una serie de booleanos, y devuelve solo las filas True.

    if len(df_filtrado) == 0:

        raise ValueError("El ID del participante no está en el archivo")

    return df_filtrado

        