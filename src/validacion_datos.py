import pandas as pd


def convertir_columnas_numericas(df, columnas):
    '''
    Verifica que las columnas esten compuestas de numeros. 
    Si son numeros los transforma en informacion numerica. 

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contiene los datos.
    columnas : list
        Lista con los nombres de las columnas que se van a convertir.

    Raises
    ------
    TypeError
        La columna debe contener valores numéricos.

    Returns
    -------
    None.

    '''

    for columna in columnas:

        try:
            df[columna] = pd.to_numeric(df[columna],errors="raise") # "raise" string que pandas interpreta para levantar el error.

        except:
            raise TypeError(f"La columna '{columna}' debe contener valores numéricos")

def verificar_positivo(df, columna):
    """"
  
    Convierte el numero en un entero (int). 
    Verifica que el numero sea positivo
    Parameters:
    ----------
    numero: int
        Numero a verificar que sea positivo.  


    Returns
    -------
    Numero: int
        Numero entero y positivo. 
   
    """
    
    if (df[columna] < 0).any():

        raise ValueError(
            f"La columna '{columna}' tiene valores negativos"
        )
     

def convertir_a_bool_respuesta(valor):
    """
    Convierte un string a tipo booleano según valores predefinidos.

    Parameters:
    ----------
        valor (str): Texto a convertir.

    Returns:
    ----------
        bool: True o False según el valor ingresado.

    Raises:
    ----------
        TypeError: Si el valor no corresponde a un booleano válido.
    """
       
    texto = valor.strip().lower()

    if texto == "true":
        return True
    elif texto == "false":
        return False
    else: 
        raise TypeError("La respuesta debe ser de tipo bool.")
        
        

def validar_go_nogo (df):
    """
    Valida que el estímulo sea 'go' o 'nogo'.

    Parameters:
    ----------
        estimulo (str): Texto que representa el estímulo.

    Returns:
    ----------
        str: El estímulo validado.

    Raises:
    ----------
        ValueError: Si el estímulo no es 'go' ni 'nogo'.
    """
    df["estimulo"] = (df["estimulo"].str.lower().str.strip()) #modifica la columna "estimulo".

    valores_validos = df["estimulo"].isin(["go", "nogo"]) #devuelve serie de booleanos

    if valores_validos.all() == False: #si no todos son True, entra en el if
        raise ValueError("Hay estímulos distintos a 'go' o 'nogo'")
        
def validar_respuesta (df):
    """
    Valida que la respuesta sea 'correcto' o 'incorrecto'.

    Parameters:
    ----------
        respuesta (str): Texto que representa la respuesta.

    Returns:
    ----------
        str: La respuesta validada.

    Raises:
    ----------
        ValueError: Si la respuesta no es 'correcto' ni 'incorrecto'.
    """
    df["resultado_respuesta"] = (df["resultado_respuesta"].str.lower().str.strip())

    respuestas_validas = (df["resultado_respuesta"].isin(["correcto", "incorrecto"]))

    if respuestas_validas.all() == False:

        raise ValueError("Hay respuestas inválidas")

def validar_tiempos_crecientes(df):
    '''
    Valida los tiempos del Dataframe y los ordena de forma creciente. 

    Parameters
    ----------
    df : pd.DataFrama
        DataFrame que contiene los datos.

    Raises
    ------
    ValueError
        Los tiempos no están en orden creciente para el participante.

    Returns
    -------
    None.

    '''

    for id_participante, grupo in df.groupby("id"):

        tiempos_ordenados = grupo["tiempo_inicio"].sort_values(ascending=True)

        if not grupo["tiempo_inicio"].equals(tiempos_ordenados): # pregunta si la columna original estaba igual que la ordenada

            raise ValueError(f"Los tiempos no están en orden creciente para el participante {id_participante}")
