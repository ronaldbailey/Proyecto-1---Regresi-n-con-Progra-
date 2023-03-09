# Proyecto-1---Regresi-n-con-Progra-

- El archivo principal es el 

### Proyecto #1 - (Regresión con Progra)

El proyecto consiste en aplicar los conocimientos aprendidos en clase (y apoy´andose de referencias adicionales u´tiles) para crear modelos predictivos de regresi´on lineal uni-variable sencillos 


# ML.py

## Descripción
Este módulo contiene la clase `ML`, la cual es utilizada para cargar datos de un archivo numpy y realizar diversas operaciones con ellos, como separación en entrenamiento y validación, visualización de histogramas y correlaciones, entre otras.

## Dependencias
- numpy
- pandas
- matplotlib
- seaborn

## Uso
Para utilizar la clase `ML`, importa el módulo y crea una instancia de la clase, pasando como parámetro el directorio del archivo numpy y, opcionalmente, la proporción en la que se desea segmentar los datos en entrenamiento y validación:

```python
from ML import ML

ml = ML('path/to/numpyfile.npy', segmentacion=0.8)


Métodos
npyToPandas(directorioArchivo=None, mostrar_salida=False): Convierte un archivo numpy en un objeto pandas DataFrame y lo devuelve. Si se proporciona el parámetro mostrar_salida=True, se imprimirá en pantalla el DataFrame resultante.

separacionData(segmentacion=None, mostrar_salida=False): Devuelve dos objetos pandas DataFrame, correspondientes a los datos de entrenamiento y validación, respectivamente. Si se proporciona el parámetro mostrar_salida=True, se imprimirán en pantalla las dos tablas resultantes.

histograma(data): Muestra un histograma para cada columna del objeto pandas DataFrame proporcionado como parámetro.

corrGrafica(data): Muestra una matriz de gráficos de dispersión y histogramas para cada combinación de columnas del objeto pandas DataFrame proporcionado como parámetro. También se incluye el valor de correlación correspondiente en cada gráfico.
# Métodos
npyToPandas(directorioArchivo=None, mostrar_salida=False):
    """
    Convierte un archivo numpy en un objeto pandas DataFrame y lo devuelve.
    Si se proporciona el parámetro mostrar_salida=True, se imprimirá en pantalla el DataFrame resultante.
    """
    
separacionData(segmentacion=None, mostrar_salida=False):
    """
    Devuelve dos objetos pandas DataFrame, correspondientes a los datos de entrenamiento y validación, respectivamente.
    Si se proporciona el parámetro mostrar_salida=True, se imprimirán en pantalla las dos tablas resultantes.
    """
    
histograma(data):
    """
    Muestra un histograma para cada columna del objeto pandas DataFrame proporcionado como parámetro.
    """
    
corrGrafica(data):
    """
    Muestra una matriz de gráficos de dispersión y histogramas para cada combinación de columnas del objeto pandas DataFrame proporcionado como parámetro.
    También se incluye el valor de correlación correspondiente en cada gráfico.
    """
    
# Atributos
datos:
    """
    Objeto pandas DataFrame que contiene todos los datos cargados desde el archivo numpy.
    """
    
entrenamiento:
    """
    Objeto pandas DataFrame que contiene los datos de entrenamiento.
    """
    
validacion:
    """
    Objeto pandas DataFrame que contiene los datos de validación.
    """
    
VercorrelacionTodo:
    """
    Objeto pandas Styler que contiene una tabla con los valores de correlación entre todas las columnas de datos visualizados con un gradiente de color.
    """
    
VercorrelacionEntrenamiento:
    """
    Objeto pandas Styler que contiene una tabla con los valores de correlación entre todas las columnas de entrenamiento visualizados con un gradiente de color.
    """
    
VercorrelacionValidacion:
    """
    Objeto pandas Styler que contiene una tabla con los valores de correlación entre todas las columnas de validacion visualizados con un gradiente de color.
    """
    
correlacionTodo:
    """
    Objeto pandas DataFrame que contiene los valores de correlación entre todas las columnas de datos.
    """
    
correlacionEntrenamiento:
    """
    Objeto pandas DataFrame que contiene los valores de correlación entre todas las columnas de entrenamiento.
    """
    
correlacionValidacion:
    """
    Objeto pandas DataFrame que contiene los valores de correlación entre todas las columnas de validacion.
    """

Ejemplo
A continuación se muestra un ejemplo de cómo utilizar la clase ML:

import ML

# Crear una instancia de la clase ML
ml = ML('path/to/numpyfile.npy', segmentacion=0.8)

# Imprimir los datos de entrenamiento y validación
print



referencia https://www.geeksforgeeks.org/how-to-implement-a-gradient-descent-in-python-to-find-a-local-minimum/
