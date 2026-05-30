
import streamlit as st
import matplotlib.pyplot as plt

from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import (
    calcular_tiempo_reaccion_promedio,
    calcular_tasa_error
)


st.title("Dashboard Go/No-Go")

st.write("Subí el archivo CSV del laboratorio para analizar los datos.")

archivo = st.file_uploader(
    "Arrastrá o seleccioná tu archivo CSV",
    type=["csv"]
)

if archivo is not None:

    try:
        archivo.seek(0)
        datos = cargar_datos(archivo)

    except ValueError as e:
        st.error(f"Error de validación: {e}")
        st.stop()

    except TypeError as e:
        st.error(f"Error en los datos: {e}")
        st.stop()

    except Exception as e:
        st.error(f"Ocurrió un error inesperado: {e}")
        st.stop()

    
    st.success("Archivo cargado correctamente.")

    ids_disponibles = sorted(datos["id"].unique())

    id_participante = st.selectbox(
        "Seleccioná el participante",
        ids_disponibles
    )

    try:
        datos_participante = filtrar_por_participante(datos, id_participante)

    except ValueError as e:
        st.error(e)
        st.stop()

    tiempo_promedio = calcular_tiempo_reaccion_promedio(datos_participante)
    tasa_error = calcular_tasa_error(datos_participante)

    st.subheader("Indicadores clave")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ID participante", id_participante)

    with col2:
        st.metric("Cantidad de registros", len(datos_participante))

    with col3:
        st.metric("Tiempo promedio", round(tiempo_promedio, 3))

    st.metric("Tasa de error", f"{round(tasa_error * 100, 2)}%")

    st.subheader("Visualizaciones")

    fig1, ax1 = plt.subplots()

    ax1.plot(
        datos_participante["trial"],
        datos_participante["tiempo_reaccion"]
    )

    ax1.set_title(f"Tiempo de reacción - Participante {id_participante}")
    ax1.set_xlabel("Trial")
    ax1.set_ylabel("Tiempo de reacción")

    st.pyplot(fig1)

    errores = tasa_error
    aciertos = 1 - errores

    fig2, ax2 = plt.subplots()

    ax2.pie(
        [aciertos, errores],
        labels=["Correctas", "Incorrectas"],
        autopct="%1.1f%%"
    )

    ax2.set_title(f"Tasa de error - Participante {id_participante}")

    st.pyplot(fig2)
    

