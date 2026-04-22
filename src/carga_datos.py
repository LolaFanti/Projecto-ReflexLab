from src.validacion_datos import (verificar_positivo, convertir_a_int, convertir_a_float, convertir_a_bool_respuesta,
                                  validar_go_nogo, validar_respuesta)

def parsear_linea (linea):
    """
    Procesa una línea de texto, separa sus campos y convierte los valores al tipo correspondiente.

    Parameters:
    ----------
        linea (str): Línea de texto con los datos crudos.

    Returns:
    ----------
        list: Lista con los valores parseados y validados.

    Raises:
    ----------
        ValueError: Si la línea está vacía o no tiene la cantidad correcta de campos.
        TypeError: Si alguno de los valores no puede convertirse al tipo esperado.
    """
    
    if linea.strip() == "":
        raise ValueError("La línea está vacía")

    lista = linea.strip().split(",")

    if len(lista) != 8:
        raise ValueError("La línea no tiene la cantidad correcta de columnas")

    id_usuario = lista[0] 
    trial = convertir_a_int(lista[1],"trial")
    trial1= verificar_positivo(trial)
    t_inicio= convertir_a_float(lista[3], "tiempo inicio")
    t_inicio = verificar_positivo(t_inicio)
    t_reaccion = convertir_a_float(lista[5], "tiempo reaccion")
    t_reaccion1 = verificar_positivo(t_reaccion)
    respuesta = convertir_a_bool_respuesta(lista[4])
    estimulo = validar_go_nogo(lista[2])
    r_respuesta = validar_respuesta(lista[6])
    condicion = lista[7]
        
    info = [id_usuario, trial1, estimulo, t_inicio, respuesta, t_reaccion1, r_respuesta, condicion]
    return info
        


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
        with open(ruta_archivo + ".csv", "r") as archivo: 
            lineas = archivo.readlines()
    except Exception:
        raise FileNotFoundError("Archivo no encontrado")
    if len(lineas) == 0:
        raise ValueError("El archivo esta vacio")
    
    lista= []
    
    for linea in lineas[1:]:
        datos = parsear_linea(linea)
        registro = {"id": datos[0], "trial": datos[1], "estimulo": datos[2],
            "tiempo_inicio": datos[3], "respuesta": datos[4],"tiempo_reaccion": datos[5],
            "resultado_respuesta": datos[6],"condicion": datos[7]}

        lista.append(registro)
    
    if len(lista) == 0:
         raise ValueError("La base de datos está vacía")   
        

    datos_por_id = {}

    for registro in lista:
        id_actual = registro["id"]

        if id_actual not in datos_por_id:
            datos_por_id[id_actual] = []

        datos_por_id[id_actual].append(registro)


    for id_participante in datos_por_id:
        registros = datos_por_id[id_participante]

        tiempo_anterior = registros[0]["tiempo_inicio"]

        for registro in registros[1:]:
            tiempo_actual = registro["tiempo_inicio"]
    
            if tiempo_actual < tiempo_anterior:
                raise ValueError(f"Los tiempos no están en orden creciente para el participante {id_participante}")
    
            tiempo_anterior = tiempo_actual
    return lista
    
