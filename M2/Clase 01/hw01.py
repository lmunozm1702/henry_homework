import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

muestra = np.array( [[1.85, 1.8, 1.8 , 1.8],
                    [1.73,  1.7, 1.75, 1.76],
                    [ 1.65, 1.69,  1.67 ,  1.6],
                    [1.54,  1.57, 1.58, 1.59],
                    [ 1.4 , 1.42,  1.45, 1.48]]) 

#media
print(np.mean(muestra))

#mediana
print(np.median(muestra))

#moda
print(stats.mode(muestra.flatten(), keepdims=True)[0])

#varianza
print(np.var(muestra))

#desviación estándar
print(np.std(muestra))

#convertir muestra en lista
muestra_list = muestra.flatten().tolist()
print(muestra_list)

#histograma
plt.hist(x = muestra_list, bins = 5, color = 'cyan', rwidth = 0.8)
plt.title("Histograma de alturas")
plt.xlabel("Altura")
plt.ylabel("Frecuencia")
#plt.show()

#pandas
df = pd.DataFrame(muestra)
print(df.describe())


grupos = np.array([[10.5,17],
                  [6.8,18],
                  [20.7,21],
                  [18.2,16],
                  [8.6,16],
                  [25.8,21],
                  [22.2,16],
                  [5.9,14],
                  [7.6,18],
                  [11.8,18]])

grupos_df = pd.DataFrame(grupos, columns = ['Ingreso en miles', 'Años de estudio'])
print(grupos_df)
print(grupos_df.describe())

#Histograma de ingresos
plt.hist(x = grupos_df['Ingreso en miles'], bins = 6, color = 'blue', rwidth = 0.8)
plt.title("Histograma de ingresos")
plt.xlabel("Ingreso en miles")
plt.ylabel("Frecuencia")
#plt.show()

#Histograma de años de estudio
plt.hist(x = grupos_df['Años de estudio'], bins = 6, color = 'red', rwidth = 0.8)
plt.title("Histograma de años de estudio")
plt.xlabel("Años de estudio")
plt.ylabel("Frecuencia")
#plt.show()

#media de ingresos
print(grupos_df['Ingreso en miles'].mean())
print(np.mean(grupos_df['Ingreso en miles']))

grupos_df.loc[10] = [50, 35]
grupos_df.loc[11] = [120, 30]
print(grupos_df)
print(grupos_df.describe())