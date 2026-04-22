# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:46:50 2026

@author: lola_
"""

def trial_positivo(numero):
    """"
  
    Convierte el numero en un entero (int). 
    Verifica que el numero sea positivo
    ----------
    numero: int
        Numero a verificar que sea positivo.  


    Returns
    -------
    Numero: int
        Numero entero y positivo. 
   
    """
    
    if numero>0:
        return numero 
    else: 
        raise ValueError("El numero del trial es negativo")
     
def convertir_a_int(valor, nombre_campo):
    """
    Convierte un valor a int validando que no esté vacío.
    """
    if valor == "":
        raise ValueError(f"El campo '{nombre_campo}' está vacío.")

    try:
        aa = int(valor)
        return aa
    except ValueError:
        raise TypeError(f"El campo '{nombre_campo}' debe ser de tipo int.")


def convertir_a_float(valor, nombre_campo):
    """
    Convierte un valor a float validando que no esté vacío.
    """
    if valor == "":
        raise ValueError(f"El campo '{nombre_campo}' está vacío.")

    try:
        aa = float(valor)
        return aa
    except ValueError:
        raise TypeError(f"El campo '{nombre_campo}' debe ser de tipo float.")


def convertir_a_bool_respuesta(valor):
    """
    Convierte strings comunes a bool.
    Acepta: true/false, 1/0, si/no, yes/no
    """
       
    texto = valor.strip().lower()

    if texto == "true":
        return True
    elif texto == "false":
        return False
    else: 
        raise TypeError("La respuesta debe ser de tipo bool.")
   

