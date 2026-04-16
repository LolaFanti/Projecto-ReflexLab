# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 19:06:33 2026

@author: lola_
"""
from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_reaccion_promedio, calcular_tasa_error

ruta_archivo = input("Ingresá el nombre del archivo sin .csv: ")
try:
    datos = cargar_datos(ruta_archivo)
    
except FileNotFoundError as e:
    print(e)
    
else:
    id_participante = input("Ingresá el id del participante: ")
    datos_participante = filtrar_por_participante(datos, id_participante)

    promedio_tiempo = calcular_tiempo_reaccion_promedio(datos_participante)
    tasa_error = calcular_tasa_error(datos_participante)
    
    print("Resultados del análisis")
    print("Participante:", id_participante)
    print("Cantidad de registros:", len(datos_participante["datos"]))
    print("Tiempo de reacción promedio:", promedio_tiempo)
    print("Tasa de error:", tasa_error)



 