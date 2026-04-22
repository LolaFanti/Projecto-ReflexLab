# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:48:12 2026

@author: lola_
"""

def calcular_tiempo_reaccion_promedio(participante_diccio):
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
    
    datos = participante_diccio["datos"]
    if len(datos) == 0:
       mensaje = "No hay datos para calcular promedio"
       return mensaje
   
    suma = 0

    for dato in datos:
       suma += dato["tiempo_reaccion"]

    promedio = suma / len(datos)

    return promedio
    
def calcular_tasa_error(participante_diccio):
    """
    Calcula la proporción de respuestas incorrectas de un participante.

    Args:
        participante_diccio (dict): Diccionario con los datos del participante,
        que contiene una lista de registros bajo la clave "datos".

    Returns:
        float: Proporción de respuestas incorrectas.
        str: Mensaje indicando que no hay datos si la lista está vacía.
    """
    datos = participante_diccio["datos"]
    if len(datos) == 0:
       mensaje = "No hay datos para calcular tasa de error"
       return mensaje

    errores = 0

    for dato in datos:
       if dato["resultado_respuesta"].lower() == "incorrecto":
           errores += 1

    tasa = errores / len(datos)

    return tasa



    
