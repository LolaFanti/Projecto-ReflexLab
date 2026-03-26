def parsear_linea (linea):
    """
    Separa la línea en campos, convierte los valores al tipo correspondiente.
    Parameters
    ----------
    linea : str
        Informacion cruda del archivo.

    Returns
    dicc : diccionario
        Diccionario con la informacion del archivo ordenado.
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
    
    diccio = {"id":id_usuario, "trial": trial, "estimulo": estimulo, 
              "tiempo inicio": t_inicio, "respuesta": respuesta, 
              "tiempo reaccion": t_reaccion, "resultado de respuesta": r_respuesta,
              "condicion":condicion}
    return diccio
    



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
    
    
