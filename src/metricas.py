# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:48:12 2026

@author: lola_
"""

def calcular_tiempo_reaccion_promedio(lista):
    """
    Calcula el promedio del tempio de reaccion de un participante.

    Parameters
    ----------
    lista : list
        lista de diccionarios con la información de un participante.

    Returns
    -------
    float: El promedio del tiempo de reaccion.

    """
    if len(lista) == 0:
       return 0.0
   
    suma = 0

    for dato in lista:
       suma += dato["tiempo_reaccion"]

    promedio = suma / len(lista)

    return promedio
    
def calcular_tasa_error(lista):
    """
    Calcula la tasa de error (proporción de respuestas incorrectas).

    Parameters
    ----------
    lista : list
        lista de diccionarios con la información de un participante.

    Returns
    -------
    float: proporcion de respuestas incorrectas.

    """
    if len(lista) == 0:
       return 0.0

    errores = 0

    for dato in lista:
       if dato["resultado_respuesta"].lower() == "incorrecta":
           errores += 1

    tasa = errores / len(lista)

    return tasa



    
