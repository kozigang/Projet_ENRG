#Importation des librairies nécessaires
import pandas as pd
import numpy as np
import string
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
import random
import json

# Lire le csv dico qui permet de relier un numéro de station à une ville
df = pd.read_csv('/Users/evank/OneDrive/Bureau/Projet_DevPlatformeENRG/Projet_ENRG/Data_base_eolien/VENT/postesSynop.csv', sep=';')

# Spécifier le séparateur lors de la lecture du CSV
data_csv = pd.read_csv('/Users/evank/OneDrive/Bureau/Projet_DevPlatformeENRG/Projet_ENRG/Data_base_eolien/VENT/synop.202312.csv', sep=';')

# Conserver seulement les colonnes spécifiées
data_csv = data_csv.filter(items=['numer_sta', 'date', 'ff', 'raf10'])

# Fusionner les deux DataFrames sur la colonne 'ID' au lieu de 'numer_sta'
merged_data = pd.merge(data_csv, df, left_on='numer_sta', right_on='ID')

# Supprimer les lignes où l'ID correspond à 7761 ou 78890
#merged_data = merged_data.drop(merged_data[(merged_data['numer_sta'] == 7761)|(merged_data['numer_sta'] == 7790)|(merged_data['numer_sta'] == 78890)|(merged_data['numer_sta'] == 78890)].index)
# Liste des ID des pays non métropolitains
ids_pays_non_metropoles = [7761, 7790, 78890, 78894, 78897, 78922, 78925, 61968, 61970, 61972, 61976, 61980, 61996, 61997, 61998, 67005, 71805, 81401, 81405, 81408, 81415, 89642]

# Supprimer les lignes où l'ID correspond à l'un des pays non métropolitains
merged_data = merged_data[~merged_data['numer_sta'].isin(ids_pays_non_metropoles)]


# Classifier les données par le nom de la ville
grouped_data = merged_data.groupby('Nom')

# Dico solaire
"""
Dico = {1300: {'2A': 'Corse du Sud', '2B': 'Haute Corse', '09': 'Ariege', '66': 'Pyrenees Orientals', '11': 'Aude',
               '34': 'Herault', '48': 'Lozere', '30': 'Gard', '07': 'Ardeche', '26': 'Drome', '05': 'Hautes Alpes',
               '84': 'Vaucluse', '13': 'Bouche du Rhone', '83': 'Var', '06': 'Alpes Maritimes',
               '04': 'Alpes de Haute Provence'},
        1150: {'31' :}}
"""
NbVille = 0

# Convertir la colonne 'date' en type datetime
merged_data['date'] = pd.to_datetime(merged_data['date'], format='%Y%m%d%H%M%S')

# Filtrer les lignes où l'heure est 00:00:00
merged_data = merged_data[merged_data['date'].dt.hour == 0]

# Classifier les données par le nom de la ville
grouped_data = merged_data.groupby('Nom')

###

# Remplacer les 'mq' par np.nan dans le DataFrame
merged_data.replace('mq', np.nan, inplace=True)

# Convertir la colonne 'ff' en type float
merged_data['ff'] = merged_data['ff'].astype(float)

# Calculer la moyenne de la vitesse moyenne (ff) pour chaque ville
city_avg_speed = merged_data.groupby('Nom')['ff'].transform('mean')

# Remplacer les valeurs manquantes dans 'ff' par la moyenne correspondante de chaque ville
merged_data['ff'].fillna(city_avg_speed, inplace=True)

###
# Afficher un résultat par jour pour chaque ville
NbVille = 0
for name, group in grouped_data:
    print(f"\nVille {name}")
    print(group.to_string())
    NbVille += 1

print(NbVille)

# Vérifier les colonnes contenant des valeurs manquantes
missing_values_columns = merged_data.columns[merged_data.isnull().any()]

"""
# Afficher les noms des colonnes contenant des valeurs manquantes
print("Colonnes avec des valeurs manquantes :")
for col in missing_values_columns:
    print(col)
"""

# Identifier les lignes avec des valeurs manquantes dans la colonne 'ff'
missing_ff_rows = merged_data[merged_data['ff'].isnull()]

# Afficher les lignes avec des valeurs manquantes dans la colonne 'ff'
print("Lignes avec des valeurs manquantes dans la colonne 'ff':")
print(missing_ff_rows)
