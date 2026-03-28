def parsear_linea (linea):
    """
    Separa la línea en campos, convierte los valores al tipo correspondiente.
    Parameters
    ----------
    linea : str
        Informacion cruda del archivo.

    Returns
    list : lista con los valores parseados
    """
    lista = linea.strip().split(";")
    id_usuario = lista[0]
    trial = int(lista[1])
    estimulo = lista[2]
    t_inicio = float(lista[3])
    respuesta = lista[4]
    t_reaccion = float(lista[5])
    r_respuesta = lista[6]
    condicion = lista[7]
    
    info = [id_usuario, trial, estimulo, t_inicio, respuesta, t_reaccion, r_respuesta, condicion]
    return info
    

def cargar_datos(ruta_archivo):
    """
    Carga datos desde un archivo y devuelve una lista de registros.
    Parameters
    ----------
    ruta_archivo : str
        Ruta del archivo a leer.

    Returns
    -------
    lista_registros : list
        Lista de registros parseados a partir del archivo.
    """
    archivo = open(ruta_archivo + ".csv", "r")
    lineas = archivo.readlines()
    archivo.close()
    
    lista= []
    
    for linea in lineas:
        datos = parsear_linea(linea)

        registro = {"id": datos[0], "trial": datos[1], "estimulo": datos[2],
            "tiempo_inicio": datos[3], "respuesta": datos[4],"tiempo_reaccion": datos[5],
            "resultado_respuesta": datos[6],"condicion": datos[7]}

        lista.append(registro)

    return lista
    
