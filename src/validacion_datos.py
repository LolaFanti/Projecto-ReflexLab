
def verificar_positivo(numero):
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
    
    if numero>= 0:
        return numero 
    else: 
        raise ValueError("El numero del trial es negativo")
     
def convertir_a_int(valor, nombre_campo):
    """
    Convierte un valor a tipo entero validando que no esté vacío.

    Parameters:
    ----------
         valor (str): Valor a convertir.
         nombre_campo (str): Nombre del campo para mensajes de error.
    Returns:
        int: El valor convertido a entero.

    Raises:
    ----------
        ValueError: Si el valor está vacío.
        TypeError: Si el valor no puede convertirse a entero.
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
    Convierte un valor a tipo float validando que no esté vacío.

    Parameters:
    ----------
        valor (str): Valor a convertir.
        nombre_campo (str): Nombre del campo para mensajes de error.

    Returns:
    ----------
        float: El valor convertido a número decimal.

    Raises:
    ----------
        ValueError: Si el valor está vacío.
        TypeError: Si el valor no puede convertirse a float.
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
        
        

def validar_go_nogo (estimulo):
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
    estimulo = estimulo.strip().lower()
    if estimulo.strip() =="go" or estimulo.strip()=="nogo" : 
        return estimulo 
    else: 
        raise ValueError("el estimulo es distinto a 'go' o 'nogo'")
        
def validar_respuesta (respuesta):
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
    respuesta = respuesta.strip().lower()
    if respuesta.strip() =="correcto" or respuesta.strip()=="incorrecto" :
        return respuesta
    else:
        raise ValueError("La respuesta es distinto a 'correcto' o'incorrecto")
   

