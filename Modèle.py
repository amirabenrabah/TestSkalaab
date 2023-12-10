# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:25:11 2023

@author: Amira Benrabah
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error


#importer le dataset traité précedemment
df = pd.read_csv ('cleanedData.csv')



#imputer les colonne input Area dans une variable
X = df['Area (ft.)']

#imputer les colonne output Price dans une variable
Y = df['Price']

#transformer les colonnes de la dataframe en Array afin d'avoir 2D
arrayX=X.values
new_arrayX = np.reshape(arrayX, (-1, 1))
arrayY=Y.values
new_arrayY = np.reshape(arrayY, (-1, 1))



# diviser la dataset en données d'entrainement et données de tests
X_train, X_test, y_train, y_test = train_test_split(new_arrayX, new_arrayY, test_size=0.2, random_state=42)

#Creer un modèle de regression linéaire
linear_model = LinearRegression()

# Entrainer le modèle
linear_model.fit(X_train, y_train)

# faire des prédictions dans les données de test 
y_train_predict = linear_model.predict(X_test)

#Evaluer les performance du modèle en utilisant des metrics
mse = mean_squared_error(y_test, y_train_predict)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_train_predict)
r2 = r2_score(y_test, y_train_predict)

#les afficher
print(f'Erreur Quadratique Moyenner (MSE): {mse:.2f}')
print(f'Erreur Quadratique Moyenne Racine (RMSE): {rmse:.2f}')
print(f'Erreur Absolue Moyenne (MAE): {mae:.2f}')
print(f'R-squared (R2): {r2:.2f}')

#les visualiser via un nuages de point avec les valeurs du prix réelles
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')
plt.plot(X_test, y_train_predict, color='red', linewidth=3, label='Prix Prédits')
plt.xlabel('Superficie')
plt.ylabel('Prix')
plt.title('Prix Réels vs Prix Prédits')
plt.legend()
plt.show()

#une autre méthode d'afficher les valeurs prédites
residuals = y_test - y_train_predict
plt.scatter(X_test, residuals, color='red')
plt.axhline(y=0, color='black', linestyle='--', linewidth=2)
plt.xlabel('Superficie')
plt.ylabel('Résidue')
plt.title('Residual Plot')
plt.show()





