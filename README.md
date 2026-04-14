# Projecto-ReflexLab



Este repositorio colaborativo tiene como objetivo obtener datos provenientes de distintos tipos de tareas como Go/No-Go, para procesar respuestas conductuales discretas y analizar el desempeño básico de los participantes.

Errores y validaciones
En la función cargar_datos se contemplan posibles errores asociados a la lectura del archivo. En primer lugar, se maneja el caso en el que el archivo no exista mediante un bloque try/except, devolviendo una lista vacía para evitar que el programa se detenga.

Funcion métricas: Si el id del participante buscado no esta dentro de los posibles id de los participantes, la lista de datos va a estar vacia. Es por eso no se podria dividir por el len de esa lista ya que seria dividir por 0. Para manejar esto le decimos a las funciones de metricas que si la lista de datos esta vacia imprima el mensaje correspondiente.
 La informacion que viene del archivo en la funcion parsear_linea no es necesario verificarla ya que sabemos que va a tener los tipos de datos correctos

Lola Fanti, Clara Henestrosa, Ela Iturriaga, Olivia Muller

