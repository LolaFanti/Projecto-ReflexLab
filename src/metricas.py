# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:48:12 2026

@author: lola_
"""

def calcular_tiempo_reaccion_promedio(participante_diccio):
    """
    Calcula el promedio del tempio de reaccion de un participante.

    Parameters
    ----------
    participante_diccio : dicc
        Diccionairo de diccionarios con la información de un participante.

    Returns
    -------
    float: El promedio del tiempo de reaccion.
    string: Si la lista de tiempos esta vacia, devuelve un mensaje que aclara que no hay datos en la lista..

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
    Calcula la tasa de error (proporción de respuestas incorrectas).

    Parameters
    ----------
    participante_diccio: dicc
        Diccionario con la información de un participante.

    Returns
    -------
    float: proporcion de respuestas incorrectas.

    string: Si la lista de tiempos esta vacia, devuelve un mensaje que aclara que no hay datos en la lista
    """
    datos = participante_diccio["datos"]
    if len(datos) == 0:
       mensaje = "No hay datos para calcular tasa de error"
       return mensaje

    errores = 0

    for dato in datos:
       if dato["resultado_respuesta"].lower() == "incorrecta":
           errores += 1

    tasa = errores / len(datos)

    return tasa



    
