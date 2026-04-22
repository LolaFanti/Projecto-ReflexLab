# Projecto-ReflexLab



Este repositorio colaborativo tiene como objetivo obtener datos provenientes de distintos tipos de tareas como Go/No-Go, para procesar respuestas conductuales discretas y analizar el desempeño básico de los participantes.



Lola Fanti, Clara Henestrosa, Ela Iturriaga, Olivia Muller





Errores y validaciones:



El programa valida que el archivo exista y pueda abrirse. Además, verifica que la base de datos cargada contenga registros. Para cada línea del archivo, controla que no esté vacía y que tenga la cantidad correcta de columnas. También comprueba que los tipos de datos sean correctos: trial debe ser entero, tiempo\_inicio y tiempo\_reaccion deben ser numéricos decimales, y respuesta debe ser booleana. A su vez, valida que ciertos valores no sean negativos, como trial y tiempo\_reaccion, y que los campos solo contengan valores permitidos, por ejemplo go o nogo para el estímulo y correcto o incorrecto para el resultado de la respuesta. Por último, verifica que los tiempos de inicio estén en orden creciente para cada participante y que el participante solicitado exista en la base antes de calcular las métricas correspondientes.

