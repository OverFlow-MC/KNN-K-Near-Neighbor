import numpy as np
import os
import random as rd
import math as m
os.chdir(r'D:/...')
f=open('bmd.csv','r')
d=f.readlines()
for k in range(1,len(d)):
    d[k]=d[k].rstrip()#Suppression des retours chariots
    d[k]=d[k].split(',')#Séparation des éléments délimités par une virgule

Data=np.zeros((len(d)-1,4))#Initialisation de la matrice data
Etiquette=np.zeros((len(d)-1,))#Initialisation de la matrice etiquette
for i in range(1,len(d)):
    Data[i-1,0]=d[i][1]#Importation de l'age des patients
    Data[i-1,2]=(float(d[i][4]))/(((float(d[i][5]))*10**(-2))**2)#Calcul puis importation de l'IMC des patients
    Data[i-1,3]=d[i][8]# Importation des résultats du test densiométrique osseux
    if d[i][2]=='F':
        Data[i-1,1]=1#Imortation du sexe du patient (1 pour une fille et 0 pour un garçon)
    else :
        Data[i-1,1]=0
    if d[i][3]=='fracture':
        Etiquette[i-1]=1 #Importation de la donnée de fracture (1 si fracture, 0 sinon)
    else:
        Etiquette[i-1]=0

def LigneAléatoire(a,NB):
    ListeNBLignes=[]
    while len(ListeNBLignes)!=int((a*NB)/100):# Utilisation d'une boucle while pour avoir des entier tous différents dans la liste. La boucle ne s'arrête pas tant que les entier ne sont pas tous différents.
        b=rd.randint(0,NB-1)
        if b not in ListeNBLignes: #Si un entier est déjà dans la liste, le programme ne l'importe pas dedans, ce qui permet de faire recommencer la boucle.
            ListeNBLignes.append(b)
    return ListeNBLignes

def IA (a,NB):
    ListeNBLignes=LigneAléatoire(a,NB)# La taille de la liste va décider de La quantiter d'information répartis dans les matrices de test et d'apprentissage.
    DonneesTest=Data[0:len(ListeNBLignes)]
    EtiquetteTest=Etiquette[0:len(ListeNBLignes)]
    DonneesApprentissage=Data[(len(d)-len(ListeNBLignes)):len(d)]
    EtiquetteApprentissage=Etiquette[(len(d)-len(ListeNBLignes)):len(d)]
    # Création des différentes matrice de données et d'étiquettes pour les test et l'apprentissage en fonction des données présentes dans la matrice data.
    return DonneesTest, DonneesApprentissage, EtiquetteTest, EtiquetteApprentissage

def Normalisation(M):
    l,c=np.shape(M)
    ListeMoyennes=[]
    ListeEcarts=[]
    for k in range(c):
        moyenne=0
        ecart=0
        for i in range(l):
            moyenne=(moyenne+M[i][k])/l
        ListeMoyennes.append(moyenne)
        # Cette boucle permet de calculer la moyenne de chaques colonnes et la sauvegarde dans une liste.
        for i in range(l):
            M[i][k]=M[i][k]-moyenne # On soustrait à chaque éléments d'une colone la valeur de la moyenne des valeurs de cette même colonne pour avoir une matrice dont la moyenne est nulle.
            ecart=ecart+(1/l)*M[i][k]**2
        ecart=m.sqrt(ecart)
        ListeEcarts.append(ecart)
        # Cette boucle permet de calculer l'écart-type de chaques colonnes et la sauvegarde dans une liste.
        for i in range(l):
            M[i][k]=M[i][k]/ecart # On applique la transformation suggérée par l'énoncé pour avoir un écart-type égale à 1.
    return M, ListeMoyennes, ListeEcarts

ListeMoyennes,ListeEcarts=Normalisation(IA(30,169)[1])[1],Normalisation(IA(30,169)[1])[2] # Cette ligne sert à rendre les listes de moyennes et d'écart-type, obtenue avec la fonction précédante, utilisable pour la question suivante directement.

def Normalisation2(M,ListeMoyennes,ListeEcarts):
    l,c=np.shape(M)
    for k in range(c):
        for i in range(l):
            M[i][k]=M[i][k]-ListeMoyennes[k]
            M[i][k]=M[i][k]/ListeEcarts[k]
            # On applique la même transformation à la matrice DonneesTest mais aves les valeurs de moyennes et d'écarts-type obtenus avec la matrice DonneesApprentissage.
    return M

def DistanceEuclidienne(X1,X2):
    try:
        a=X2[len(X1)-1]
        b=X1[len(X2)-1]
        # Pour vérifier que les 2 listes sont bien de la même taille, on fait un test avec la taille des listes, si le programme renvoie une érreure 'out of range' alors les liste ne sont pas de la même taille.
    except:
        print('X1 et X2 doivents être de la même taille')
        return False
    d=0
    for k in range(len(X1)):
        d=d+(X1[k]-X2[k])**2
    d=m.sqrt(d) # Calcul de la distance euclidienne entre les 2 liste en appliquant la formule donné.
    return d











