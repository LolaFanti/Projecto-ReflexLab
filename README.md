# Projecto-ReflexLab



Este repositorio colaborativo tiene como objetivo obtener datos provenientes de distintos tipos de tareas como Go/No-Go, para procesar respuestas conductuales discretas y analizar el desempeño básico de los participantes.



Lola Fanti, Clara Henestrosa, Ela Iturriaga, Olivia Muller





Errores y validaciones:



El programa valida que el archivo exista y pueda abrirse. Además, verifica que la base de datos cargada contenga registros. Para cada línea del archivo, controla que no esté vacía y que tenga la cantidad correcta de columnas. También comprueba que los tipos de datos sean correctos: trial debe ser entero, tiempo\_inicio y tiempo\_reaccion deben ser numéricos decimales, y respuesta debe ser booleana. A su vez, valida que ciertos valores no sean negativos, como trial y tiempo\_reaccion, y que los campos solo contengan valores permitidos, por ejemplo go o nogo para el estímulo y correcto o incorrecto para el resultado de la respuesta. Por último, verifica que los tiempos de inicio estén en orden creciente para cada participante y que el participante solicitado exista en la base antes de calcular las métricas correspondientes.



Utilización de Pandas:



Para adaptar el proyecto al uso de pandas, se modificarían principalmente las funciones relacionadas con la carga, validación, filtrado y análisis de datos. En carga\_datos.py, la función cargar\_datos() se reemplazaria la manera de abrir archivos por "pd.read\_csv()" para cargar directamente un DataFrame. Además, ya no sería necesario construir manualmente una lista de diccionarios ni utilizar "parsear\_linea()" para separar los campos del CSV, ya que pandas lo separa automaticamente por columnas. Dentro de esta misma función se agregarían validaciones sobre el DataFrame completo, como la verificación de nombres de columnas mediante "list(df.columns)" y controles sobre valores negativos o inválidos utilizando operaciones sobre columnas completas. En validacion\_datos.py, las funciones "convertir\_a\_int()" y "convertir\_a\_float()" dejarían de ser necesarias porque queda englobado en el método pd.to\_numeric(). En procesamiento\_datos.py, la función filtrar\_por\_participante() dejaría de recorrer listas manualmente con ciclos for y pasaría a utilizar filtros de pandas como "df\[df\["id"] == id\_buscado]", devolviendo directamente un DataFrame filtrado. En metricas.py, las funciones de cálculo también cambiarían: "calcular\_tiempo\_reaccion\_promedio()" dejaría de sumar valores manualmente para utilizar métodos de pandas como ".mean()", mientras que "calcular\_tasa\_error()" reemplazaría el conteo manual de errores por filtros y operaciones sobre columnas del DataFrame. Finalmente, en main.py, las variables principales pasarían a almacenar DataFrames en lugar de listas y diccionarios, y varias operaciones de acceso a los datos se simplificarían utilizando directamente las funcionalidades de pandas.


Utilización de StreamLit:

El proyecto incluye una interfaz gráfica desarrollada con Streamlit que permite interactuar con el sistema desde un navegador web. A través de esta interfaz, el usuario puede cargar un archivo CSV, validar automáticamente los datos ingresados, visualizar indicadores clave de desempeño (KPIs) y consultar los gráficos generados por los módulos de análisis.