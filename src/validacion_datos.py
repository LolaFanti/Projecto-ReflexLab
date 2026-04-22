# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:46:50 2026

@author: lola_
"""

def verificar_positivo(numero):
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
     

