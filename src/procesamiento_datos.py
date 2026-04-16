def  filtrar_por_participante (lista,id_buscado) :
    """
    Selecciona los datos de un participante y los separa en un diccionario.

    Parameters
    ----------
    datos : list
        Contiene los datos de todos los participantes.
    id_participante : int
        Id del participante a filtrar.

    Returns
    datos_participante_filtrado : dicc
        Con los datos ya filtrados del participante ingresado.

    """
    resultado = []

    for registro in lista:
        if registro["id"] == id_buscado:
            resultado.append(registro)
        else:
            mensaje = "No existe ese participante"
            return mensaje
    
    datos_participante_filtrado = {"id": id_buscado, "datos": resultado}
    return datos_participante_filtrado

        