def  filtrar_por_participante (datos,id_participante) :
    """
    Selecciona los datos de un participante.

    Parameters
    ----------
    datos : list
        Contiene los datos de todos los participantes.
    id_participante : int
        Id del participante a filtrar.

    Returns
    datos_participante_filtrado : list
        Con los datos ya filtrados del participante ingresado.

    """
    datos_filtrados = []
    for dato in datos:
        if dato["id"] == id_participante:
            datos_filtrados.append(dato)

    return datos_filtrados

#me pedia que devuelva un diccionario pero me parece imposible separar 
#la informacion de los participantes que viene de multiples diccionaraios
#a uno solo.

        