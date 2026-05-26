import matplotlib.pyplot as plt

def calcular_tiempo_reaccion_promedio(df_participante):
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
    
    if df_participante.empty:
       return "No hay datos para calcular promedio"

    return df_participante["tiempo_reaccion"].mean()

    
    
def calcular_tasa_error(df_participante):
    """
    Calcula la proporción de respuestas incorrectas de un participante.

    Args:
        participante_diccio (dict): Diccionario con los datos del participante,
        que contiene una lista de registros bajo la clave "datos".

    Returns:
        float: Proporción de respuestas incorrectas.
        str: Mensaje indicando que no hay datos si la lista está vacía.
    """
   
    if df_participante.empty:
        return "No hay datos para calcular tasa de error"

    errores = df_participante["resultado_respuesta"] == "incorrecto" #queda como una columna de True y False

    return errores.mean()

def graficar_tiempo_reaccion(df_participante, id_participante):
    
    plt.plot(df_participante["trial"],df_participante["tiempo_reaccion"])

    plt.title(f"Tiempo de reacción - Participante {id_participante}")

    plt.xlabel("Trial")
    plt.ylabel("Tiempo de reacción")

    plt.savefig(f"graficos/tiempo_reaccion_{id_participante}.png")#para que se guarde en graficos 

    plt.close()

def graficar_tasa_error(df_participante, id_participante):

    errores = calcular_tasa_error(df_participante)

    aciertos = 1 - errores #el resto fueron correctas. ej si errores = 0,2 aciertos va a ser= 0,8

    valores = [aciertos, errores]

    etiquetas = ["Correctas", "Incorrectas"]

    plt.pie(valores, labels=etiquetas, autopct="%1.1f%%")# esto de autopct me lo dijo chat gpt porque se imprimia mal sino.

    plt.title(f"Tasa de error - Participante {id_participante}")

    plt.savefig(f"graficos/tasa_error_{id_participante}.png")#para que se guarde en graficos 

    plt.close()


    
