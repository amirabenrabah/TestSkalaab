# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 17:58:41 2023

@author: Amira Benrabah
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#lire le fichier CSV en data frame
df = pd.read_csv ('cleanedData.csv')


df1=(df['Price'].describe())
print(df1)

df1=(df['Area (ft.)'].describe())
print(df1)

# Visualiser la superficie par rapport au prix en utilisant nuage de point
plt.figure(figsize=(8, 6))
plt.scatter(df['Area (ft.)'],df['Price'])
plt.title('Répartition des prix par superficie')
plt.xlabel('Superficie')
plt.ylabel('Prix')
plt.show()

#calculer la moyenne des prix pour chaque année
meanYearofSalePrice = df.groupby('Year of sale')['Price'].mean()
# Visualiser la moyenne des prix pour chaque année
plt.figure(figsize=(8, 6))
meanYearofSalePrice.plot(kind='bar', color='orange')
plt.title('Moyenne des Prix par Année')
plt.xlabel('Année')
plt.ylabel('Moyenne des Prix')
plt.show()


#calculer la moyenne des prix pour chaque année
meanMonthofSalePrice = df.groupby('Month of sale')['Price'].mean()
# Visualiser la moyenne des prix pour chaque année
plt.figure(figsize=(8, 6))
meanMonthofSalePrice.plot(kind='bar', color='orange')
plt.title('Moyenne des Prix par mois')
plt.xlabel('Mois')
plt.ylabel('Moyenne des Prix')
plt.show()

#calculer la moyenne des prix par tranche d'age
meanIntervalAgePrice = df.groupby('Interval')['Price'].mean()
# Visualiser la moyenne des prix par tranche d'age
plt.figure(figsize=(8, 6))
meanIntervalAgePrice.plot(kind='bar', color='skyblue')
plt.title('Moyenne des Prix par tranche dage')
plt.xlabel('Tranche age')
plt.ylabel('Moyenne des Prix')
plt.show()


#calculer la moyenne des prix par tranche d'age
meanIntervalAgePrice = df.groupby('Age at time of purchase')['Price'].mean()
# Visualiser la moyenne des prix par tranche d'age
plt.figure(figsize=(8, 6))
meanIntervalAgePrice.plot(kind='bar', color='skyblue')
plt.title('Moyenne des Prix par tranche dage')
plt.xlabel('Tranche age')
plt.ylabel('Moyenne des Prix')
plt.show()





#calculer la moyenne des prix par Ville
meanStatePrice = df.groupby('State')['Price'].mean()
# Visualiser la moyenne des prix pour chaque ville
plt.figure(figsize=(8, 6))
meanStatePrice.plot(kind='bar', color='skyblue')
plt.title('Moyenne des Prix par Ville')
plt.xlabel('Ville')
plt.ylabel('Moyenne des Prix')
plt.show()

#calculer la moyenne des prix par Source
meanSourcePrice = df.groupby('Source')['Price'].mean()
# Visualiser la moyenne des prix pour chaque source
plt.figure(figsize=(8, 6))
meanSourcePrice.plot(kind='bar', color='black')
plt.title('Moyenne des Prix par Source')
plt.xlabel('Source')
plt.ylabel('Moyenne des Prix')
plt.show()

#calculer la moyenne des prix par Objectif
meanSourcePrice = df.groupby('Purpose')['Price'].mean()
# Visualiser la moyenne des prix pour chaque objectif
plt.figure(figsize=(8, 6))
meanSourcePrice.plot(kind='bar', color='blue')
plt.title('Moyenne des Prix par Objectif')
plt.xlabel('Objectif')
plt.ylabel('Moyenne des Prix')
plt.show()

#calculer la moyenne des prix par genre
meanGenderPrice = df.groupby('Gender')['Price'].mean()
# Visualiser la moyenne des prix pour chaque genre
plt.figure(figsize=(8, 6))
meanGenderPrice.plot(kind='bar', color='purple')
plt.title('Moyenne des Prix par Genre')
plt.xlabel('Genre')
plt.ylabel('Moyenne des Prix')
plt.show()

#calculer la moyenne des prix par Pays
meanCountryPrice = df.groupby('Country')['Price'].mean()
# Visualiser la moyenne des prix pour chaque pays
plt.figure(figsize=(8, 6))
meanCountryPrice.plot(kind='bar', color='skyblue')
plt.title('Moyenne des Prix par Pays')
plt.xlabel('Pays')
plt.ylabel('Moyenne des Prix')
plt.show()


#calculer le nbr de ligne pour chaque ville
State_counts = df['State'].value_counts()

# Visualiser
plt.figure(figsize=(8, 6))
State_counts.plot(kind='bar', color='pink')
plt.xlabel('Ville')
plt.ylabel('Nombre de vente')
plt.title('Nombre de vente pour chaque ville')
plt.show()


#Calculer le nombre vente par mois
Month_counts = df['Month of sale'].value_counts()
#Visualiser le nombre vente par mois
Month_counts.plot(kind='pie' , labels=df['Month of sale'], autopct='%1.1f%%', startangle=90)
plt.axis('equal') #afin d'avoir un cercle symètrique
plt.title('Nombre de vente par mois')
plt.show()

# Visualiser les prix par rapport au type du bien en utilisant nuage de point
plt.figure(figsize=(8, 6))
plt.scatter(df['Price'], df['Type of property'])
plt.title('Type du bien par rapport au prix')
plt.xlabel('Prix')
plt.ylabel('type de bien')
plt.show()


#calculer la moyenne des prix pour chaque satisfaction
meanSatisfactionPrice = df.groupby('Deal satisfaction')['Price'].mean()
# Visualiser la moyenne des prix pour chaque satisfaction
plt.figure(figsize=(8, 6))
meanSatisfactionPrice.plot(kind='bar', color='yellow')
plt.title('Moyenne des Prix par Satisfaction')
plt.xlabel('Note')
plt.ylabel('Moyenne des Prix')
plt.show()



#remplacer les valeurs catègorielle par des valeurs entières
df['State'] = df['State'].replace({'Arizona': 0, 'California': 1, 'Colorado': 2, 'Kansas': 3, 'Nevada': 4, 'Oregon': 5, 'Utah': 6, 'Virginia': 7, 'Wyoming': 8, 'Copenhague': 9, 'Mexico': 10, 'Bruxelles': 11, 'Moscou': 12, 'Ottawa':13, 'Berlin':14, 'Londres':15})

print(df['State'])
#remplacer les valeurs catègorielle par des valeurs entières
df['Purpose'] = df['Purpose'].replace({'Home': 0, 'Investment': 1})


#Pour justement pouvoir visualiser dans la heat map
corr_matrix = df.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, cbar_kws={'label': 'Correlation Variables'})
plt.show()

