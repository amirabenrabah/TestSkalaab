# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 15:51:41 2023

@author: Amira Benrabah
"""
import pandas as pd
import numpy as np

#lire le fichier CSV en data frame
df = pd.read_csv ('Real_es.csv')

#supprimer les lignes en doubles
df.drop_duplicates()
#verifier quelle colonne a des valeurs manquantes
print(df.isnull().sum())
#changer le type de la colonne Price de object a float en supprimant le char $ et remplacant la , en espace
df['Price'] = df['Price'].str.replace('$', '')
df['Price'] = df['Price'].apply(lambda x: float(x.replace(',', '')))

# Créer un dataframe qui correspond chaque Country à un State, quand ce state est manquant
dataState = {'Country': ['Belgium', 'Canada', 'Russia', 'Denmark', 'Mexico'],
        'State': ['Bruxelles', 'Ottawa', 'Moscou', 'Copenhague', 'Mexico']}
df1 = pd.DataFrame(dataState)
# Créer un un mapping entre le Country et son State
mappingState = dict(zip(df1['Country'], df1['State']))

# Remplacer les valeurs manquantes de 'State' en utilisant le mapping précedent
df['State'] = df['State'].fillna(df['Country'].map(mappingState))
#Remplacer les ville par une valeur correcte (valeur abérante)
df.loc[df['Country'] == 'Belgium', 'State'] = 'Bruxelles'
df.loc[df['Country'] == 'UK', 'State'] = 'Londres'
df.loc[df['Country'] == 'Germany', 'State'] = 'Berlin'

#Remplir les valeurs manquantes de Gender en utilisant la fréquence
df['Gender'] = df['Gender']. fillna (df['Gender']. mode ()[0])

#Remplacer les valeurs manquantes de M/D en utilisant la médiane
df['M'].fillna(df['M'].median(), inplace=True)
df['D'].fillna(df['D'].median(), inplace=True)

#Convertir ces données en Integer (puisque c'est une date)
df['M']=df['M'].astype(int)
df['D']=df['D'].astype(int)
#supprimer les données nulles et remplacer avec la dernière valeur renseignée
df['Interval'].fillna(method='ffill', inplace=True)

#définir un max de valeur autorisé
max_missing_col = 5

# Supprimer les lignes avec un nombre de valeurs manquantes supérieur au seuil
df = df.dropna(thresh=df.shape[1] - max_missing_col)


#Récuperer la position de la dernière case remplie
last_index = df['Age at time of purchase'].last_valid_index()
#Récuperer la valeur  de la dernière case remplie
last_value = df.loc[last_index, 'Age at time of purchase']
last_value=float(last_value)

#remplir les valeurs manquantes de Age at time of purchase avec la derniere case remplie puis l'incrémenter 
df['Age at time of purchase'].fillna(value=last_value, inplace=True)
df['Age at time of purchase'][last_index+1:] += np.arange(1, len(df) - last_index)
df['Age at time of purchase'] = df['Age at time of purchase'].astype(int)

#Récuperer la position de la dernière case remplie
last_index = df['Y'].last_valid_index()
#Récuperer la valeur  de la dernière case remplie
last_value = df.loc[last_index, 'Y']
#remplir les valeurs manquantes de Y avec la derniere case remplie puis l'incrémenter en moins 
df['Y'].fillna(value=last_value, inplace=True)
df['Y'][last_index+1:] -= np.arange(1, len(df) - last_index)
#convertir en integer value
df['Y'] = df['Y'].astype(int)

#convertir en integer value 
df['Year of sale'] = df['Year of sale'].astype(int)
df['Month of sale'] = df['Month of sale'].astype(int)
df['Deal satisfaction'] = df['Deal satisfaction'].astype(int)



print(df.isnull().sum())

#enregistrer la data frame traitée dans un fichier CSV
df.to_csv('cleanedData.csv', sep=',', index=False, encoding='utf-8')
