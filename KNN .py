import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir(r'D:/...')
##TP d'application de l'alog KNN
#Mise en place des données
df = pd.read_csv('bmd.csv')
df.head()
df['fracture'].value_counts()
X = df[['age','sex','weight_kg','height_cm','bmd']].values
Y=df[['fracture']].values
Y=Y.reshape(-1)
#Traitement des données
nb=np.shape(X)[0]
for k in range(nb):
    if Y[k]=='fracture':
        Y[k]=1 #1 pour une fracture
    else:
        Y[k]=0 #0 sans fracture
    if X[k,1]=='F':
        X[k,1]=1 #1 pour les filles
    else:
        X[k,1]=0 #0 pour les garçons
Data=np.empty((np.shape(X)[0],np.shape(X)[1]-1),dtype=float)
Data[:,:2]=X[:,:2]
Data[:,-1]=X[:,-1]
Data[:,-2]=X[:,2]/(X[:,3]/100)**2

plt.figure()
colors = ['blue', 'orange']
markers = ['^', 'o']
nom=['Pas de fracture','Fracture']
plt.subplot(2,2,1)
for i in range(2):
    mask = (Y == i)
    plt.scatter(Data[mask, -1], Data[mask,-2], alpha=0.8, c=colors[i], marker=markers[i],label=nom[i])
plt.legend()
plt.xlabel('Densitométrie osseuse')
plt.ylabel('Indice IMC')
plt.subplot(2,2,2)
for i in range(2):
    mask = (Y == i)
    plt.scatter(Data[mask, 0], Data[mask,-2], alpha=0.8, c=colors[i], marker=markers[i],label=nom[i])
plt.legend()
plt.xlabel('Age')
plt.ylabel('Indice IMC')
plt.subplot(2,2,3)
for i in range(2):
    mask = (Y == i)
    plt.scatter(Data[mask, 0], Data[mask,-1], alpha=0.8, c=colors[i], marker=markers[i],label=nom[i])
plt.legend()
plt.xlabel('Age')
plt.ylabel('Densitométrie osseuse')
plt.subplot(2,2,4)
for i in range(2):
    mask = (Y == i)
    plt.scatter(Data[mask, 1], Data[mask,-2], alpha=0.8, c=colors[i], marker=markers[i],label=nom[i])
plt.legend()
plt.xlabel('Sexe')
plt.ylabel('Densitométrie osseuse')

plt.show()
