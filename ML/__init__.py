

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
    
    
    def hsitograma(self,data,titulo='Histograma'):
        fig, axs = plt.subplots(nrows=len(data.columns), figsize=(20,15))
        for i, columna in enumerate(data.columns):
            sns.histplot(data[columna],ax=axs[i-1],kde=True,color='red')
        fig.suptitle(titulo, fontsize=32)
        # ajustar espacios entre subplots
        plt.tight_layout()
        pass

    def corrGrafica(self,data,titulo='Correlacion'):    # Crear una matriz de gráficos de dispersión y histogramas
        fig, axs = plt.subplots(len(data.columns), len(data.columns), figsize=(25, 25))
        fig.suptitle(titulo, fontsize=32)
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

    def entrenar(self,entrenamiento,epochs = 100, learning_rate = 0.001,b0 = 0.1, b1 = 0.2):
        #los datos de entrenamiento deben venir en pandas la columna  0 es el objetivo a predecir y la co
        y = entrenamiento.iloc[:,0].values #primeta columna es la variable a predecir
        x =  pd.DataFrame(entrenamiento.iloc[:,1])#la segunda columna debe ser la variable dependiente
        x['unos'] = 1 
        #Aqui voy a ver cada uno de los parametros calculados
        error_df = pd.DataFrame(columns=["Epoch", "Error","b0","b1"])
        for i in range(epochs+1):
            
            y_pred_dot = np.dot(x.values,[b1,b0])#pd.DataFrame({ 'y_pred_dot':np.dot(x1.values,[b1,b0])})
            #y_pred_dot = b0 + b1 * x
            df_y =pd.DataFrame({'y_real':y,'y_pred_dot':y_pred_dot})

            error = np.add(df_y.y_pred_dot,-df_y.y_real)
            error_medio = np.divide(np.mean(np.power(error,2)),2)

            error_df = pd.concat([error_df, pd.DataFrame({"Epoch": [i], "Error":error_medio, "b0":b0,"b1":b1})])#(1/(2*len(df_y)))*((-df_y.y_real + df_y.y_pred_dot)**2).sum()})])
            
            d_error_d_b1=np.mean(np.multiply(error,x[x.columns[0]].values))#(1/(len(df_y)))*((df_y.y_real - df_y.y_pred_dot)*x).sum()
            d_error_d_b0=np.mean(error)#(1/(len(df_y)))*((df_y.y_real - df_y.y_pred_dot)).sum()

            b1 = b1-learning_rate*d_error_d_b1
            b0 = b0-learning_rate*d_error_d_b0

            #error_df = pd.concat([error_df, pd.DataFrame({"Epoch": [i], "Error": error_medio })])
            if i % 10 == 0:
                print(f" Epoca: {i}, Error Medio: {error_medio}, b0: {b0}, b1: {b1} ")
        return error_df,error_df.iloc[-1].to_dict()
    
    def guardarModelo(self,modelo,directorioNombre):
        modelo.to_csv(directorioNombre,index=False)

    def cargarModelo(self,modelo,directorioNombre):
        return pd.read_csv(directorioNombre),pd.read_csv(directorioNombre).iloc[-1].to_dict()
    
    def getInfo(self,data):
        rango = data.max() - data.min()
        # Convierte el rango en un DataFrame y transpónlo
        rango_df = pd.DataFrame(rango).transpose()
        # Concatena los DataFrames
        resultado = pd.concat([data.describe(), rango_df]).rename(index={0: 'Rango'})
        return resultado
    
    def proyeccion(self,modelo,evaluacion):
        x =  pd.DataFrame(evaluacion.iloc[:,1])#la segunda columna debe ser la variable dependiente
        x['unos'] = 1
        ypred = np.dot(x.values,[modelo['b1'],modelo['b0']])
        return pd.DataFrame({ 'x':evaluacion.iloc[:,1],'y_pred':ypred})