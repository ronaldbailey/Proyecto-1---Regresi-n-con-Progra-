# Proyecto-1---Regresi-n-con-Progra-
El proyecto consiste en aplicar los conocimientos aprendidos en clase (y apoy´andose de referencias adicionales u´tiles) para crear modelos predictivos de regresi´on lineal uni-variable sencillos 



npyToPandas: convierte un archivo de tipo .npy a un objeto de tipo DataFrame de Pandas.
separacionData: divide los datos en dos conjuntos, uno para entrenamiento y otro para validación, según una proporción determinada.
hsitograma: genera un histograma para cada columna del conjunto de datos.
corrGrafica: genera una matriz de gráficos de dispersión y histogramas para cada combinación de columnas del conjunto de datos, mostrando la correlación entre ellas.
La clase ML se inicializa con el directorio del archivo .npy y una proporción de segmentación por defecto de 0.8. Luego, se convierte el archivo .npy en un objeto DataFrame de Pandas y se separan los datos en dos conjuntos de entrenamiento y validación. También se calculan y almacenan las correlaciones para todo el conjunto de datos, así como para los conjuntos de entrenamiento y validación. Además, se generan gráficos de dispersión y histogramas para todas las combinaciones de columnas del conjunto de datos.



directorioArchivo: una cadena de caracteres que representa el directorio donde se encuentra el archivo de datos que se va a cargar.
segmentacion: un valor entre 0 y 1 que indica la proporción de datos que se utilizarán para el conjunto de entrenamiento. Por defecto se establece en 0.8, lo que significa que el 80% de los datos se utilizarán para el entrenamiento y el 20% restante para la validación.
datos: un objeto pandas.DataFrame que almacena los datos cargados desde el archivo npy.
entrenamiento: un objeto pandas.DataFrame que almacena los datos que se utilizarán para el entrenamiento.
validacion: un objeto pandas.DataFrame que almacena los datos que se utilizarán para la validación.
VercorrelacionTodo: un objeto pandas.io.formats.style.Styler que muestra una tabla con la matriz de correlación de todos los datos cargados.
VercorrelacionEntrenamiento: un objeto pandas.io.formats.style.Styler que muestra una tabla con la matriz de correlación de los datos de entrenamiento.
VercorrelacionValidacion: un objeto pandas.io.formats.style.Styler que muestra una tabla con la matriz de correlación de los datos de validación.
correlacionTodo: un objeto pandas.DataFrame que almacena la matriz de correlación de todos los datos cargados.
correlacionEntrenamiento: un objeto pandas.DataFrame que almacena la matriz de correlación de los datos de entrenamiento.
correlacionValidacion: un objeto pandas.DataFrame que almacena la matriz de correlación de los datos de validación.
Funciones:

__init__(): la función de inicialización de la clase. Esta función carga los datos desde el archivo npy, separa los datos en los conjuntos de entrenamiento y validación, y calcula las matrices de correlación y las tablas de estilo para cada conjunto de datos.
npyToPandas(): esta función carga los datos desde un archivo npy y los devuelve como un objeto pandas.DataFrame. La función toma como argumento el directorio del archivo npy y un parámetro booleano mostrar_salida que indica si se debe mostrar la salida de la función.
separacionData(): esta función separa los datos en los conjuntos de entrenamiento y validación. La función toma como argumentos el parámetro de segmentación y un parámetro booleano mostrar_salida que indica si se debe mostrar la salida de la función.
hsitograma(): esta función crea un histograma para cada columna del conjunto de datos que se le pase como argumento. La función toma como argumento el conjunto de datos.
corrGrafica(): esta función crea una matriz de gráficos de dispersión y histogramas para cada combinación de columnas del conjunto de datos que se le pase como argumento. La función toma como argumento el conjunto de datos.