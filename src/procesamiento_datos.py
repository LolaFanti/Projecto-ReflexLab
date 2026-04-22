def  filtrar_por_participante (lista,id_buscado) :
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
    resultado = []
    encontrado = False
    for registro in lista:
        if registro["id"] == id_buscado:
            encontrado = True

    if not encontrado:
        raise ValueError("El ID del participante no esta en el archivo")
        
    for registro in lista:
        if registro["id"] == id_buscado:
            resultado.append(registro)
    
    datos_participante_filtrado = {"id": id_buscado, "datos": resultado}
    return datos_participante_filtrado

        