# Projecto-ReflexLab



Este repositorio colaborativo tiene como objetivo obtener datos provenientes de distintos tipos de tareas como Go/No-Go, para procesar respuestas conductuales discretas y analizar el desempeño básico de los participantes.



Lola Fanti, Clara Henestrosa, Ela Iturriaga, Olivia Muller





Errores y validaciones:



Función cargar\_datos: Se maneja el caso en el que el archivo no exista mediante un bloque try/except, se informara al usuario que el archivo no fue encontrado con un raise.



Funcion métricas: Si el ID del participante buscado no se encuentra entre los IDs disponibles, la lista de datos asociada será vacía. En ese caso, no es posible calcular métricas como el promedio o la tasa de error, ya que implicaría dividir por cero. Para evitar este problema, las funciones de métricas verifican si la lista está vacía y, de ser así, devuelven un mensaje indicando que no hay datos suficientes para realizar el cálculo.



La información proveniente del archivo, en la función parsear\_linea, no requiere validación adicional, ya que se asume que el archivo de entrada posee el formato correcto y contiene los tipos de datos esperados. Por este motivo, es seguro realizar conversiones directas a tipos numéricos (como int o float) en aquellos campos que se sabe que son numéricos, sin necesidad de verificar previamente su validez.

