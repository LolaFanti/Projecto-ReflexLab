from src.validacion_datos import (verificar_positivo, convertir_a_int, convertir_a_float, convertir_a_bool_respuesta,
                                  validar_go_nogo, validar_respuesta)

def parsear_linea (linea):
    """
    Separa la línea en campos, convierte los valores al tipo correspondiente.
    Parameters
    ----------
    linea : str
        Informacion cruda del archivo.

    Returns
    list
        Lista con los valores parseados.
    None
        Si la línea está vacía, tiene una cantidad incorrecta de campos
        o contiene datos numéricos inválidos.
    """
    
    try:
        lista = linea.strip().split(",")
        id_usuario = lista[0] 
        trial = convertir_a_int(lista[1],"trial")
        trial1= verificar_positivo(trial)
        t_inicio= convertir_a_float(lista[3])
        t_reaccion = convertir_a_float(lista[5])
        t_reaccion1 = verificar_positivo(t_reaccion)
        respuesta = convertir_a_bool_respuesta(lista[4])
        estimulo = validar_go_nogo(lista[2])
        r_respuesta = validar_respuesta(lista[6])
        condicion = lista[7]
        
        info = [id_usuario, trial1, estimulo, t_inicio, respuesta, t_reaccion1, r_respuesta, condicion]
        return info
        
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    

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
        Si el archivo no existe, devuelve una lista vacía.
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
        
    tiempo_anterior = lista[0]["tiempo_inicio"]
    for registro in lista[1:]:
        
            tiempo_actual = registro["tiempo_inicio"]

            if tiempo_actual < tiempo_anterior:
                raise ValueError("Los tiempos no están en orden creciente")

            tiempo_anterior = tiempo_actual
            
    return lista
    
