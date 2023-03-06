import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class ML:
    
    def __init__(self, directorioArchivo, segmentacion=0.8):
        self.directorioArchivo = directorioArchivo
        self.segmentacion = segmentacion
        self.datos = self.npyToPandas()
        self.entrenamiento ,self.validacion = self.separacionData()
        self.VercorrelacionTodo = self.datos.corr().style.background_gradient(cmap='Reds') 
        self.VercorrelacionEntrenamiento = self.entrenamiento.corr().style.background_gradient(cmap='Reds')
        self.VercorrelacionValidacion = self.validacion.corr().style.background_gradient(cmap='Reds')
        self.correlacionTodo = self.datos.corr() 
        self.correlacionEntrenamiento = self.entrenamiento.corr()
        self.correlacionValidacion = self.validacion.corr()
        

    def npyToPandas(self, directorioArchivo=None, mostrar_salida=False):
        if directorioArchivo is None:
            directorioArchivo = self.directorioArchivo
        datos = np.load(directorioArchivo)
        df = pd.DataFrame(datos,columns=[
        'SalePrice', 
        'OverallQual',
        '1stFlrSF',
        'TotRmsAbvGrd',
        'YearBuilt',
        'LotFrontage'])
        if mostrar_salida:
            display(df)
        return df

    def separacionData(self, segmentacion=None, mostrar_salida=False):
        if segmentacion is None:
            segmentacion = self.segmentacion
        data = self.npyToPandas(mostrar_salida=mostrar_salida)
        entrenamiento = data[0:int(len(data)*segmentacion)]
        validacion = data[int(len(data)*segmentacion):]
        if mostrar_salida:
            print("Entrenamiento:")
            display(entrenamiento)
            print("Validación:")
            display(validacion)
        return entrenamiento, validacion
    
    
    def hsitograma(self,data):
        fig, axs = plt.subplots(nrows=len(data.columns), figsize=(20,15))
        for i, columna in enumerate(data.columns):
            sns.histplot(data[columna],ax=axs[i-1],kde=True,color='red')
        # ajustar espacios entre subplots
        plt.tight_layout()
        pass

    def corrGrafica(self,data):    # Crear una matriz de gráficos de dispersión y histogramas
        fig, axs = plt.subplots(len(data.columns), len(data.columns), figsize=(25, 25))

        # Iterar sobre todas las combinaciones de columnas
        for i in range(len(data.columns)):
            for j in range(len(data.columns)):
                # Crear un gráfico de dispersión o histograma para cada combinación de columnas

                axs[i,j].scatter(data[data.columns[j]], data[data.columns[i]],color='red')

                # Calcular la correlación y agregarla como texto en el gráfico
                corrcoef = data.corr().iloc[i,j]
                axs[i,j].text(0.05, 0.95, f"Corr: {corrcoef:.2f}", transform=axs[i,j].transAxes,ha="left", va="top")

                # Añadir etiquetas a los ejes
                if i == 0:
                    axs[i,j].set_xlabel(data.columns[j])
                    axs[i,j].xaxis.set_label_coords(0.5, 1.1)
                if j == 0:
                    axs[i,j].set_ylabel(data.columns[i])
                    
                axs[i,j].set_xlim(
                    data[data.columns[j]].min()-(data[data.columns[j]].max()-data[data.columns[j]].min())*0.1,
                    data[data.columns[j]].max()+(data[data.columns[j]].max()-data[data.columns[j]].min())*0.1)
                axs[i,j].set_ylim(
                    data[data.columns[i]].min()-(data[data.columns[j]].max()-data[data.columns[j]].min())*0.1,
                    data[data.columns[i]].max()+(data[data.columns[j]].max()-data[data.columns[j]].min())*0.1)
    pass
    
   
