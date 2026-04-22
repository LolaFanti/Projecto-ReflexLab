# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:46:50 2026

@author: lola_
"""

def trial_entero_positivo(numero):
     numero= int(numero)
     if numero>0:
         return numero 
     else: 
         raise ValueError("El numero del trial es negativo")
     

