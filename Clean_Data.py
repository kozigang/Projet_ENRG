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
df = pd.read_csv('C:/Users/evank/OneDrive/Bureau/Projet_DevPlatformeENRG/Data_base_eolien/VENT/postesSynop.csv', sep=';')

# Spécifier le séparateur lors de la lecture du CSV
data_csv = pd.read_csv('C:/Users/evank/OneDrive/Bureau/Projet_DevPlatformeENRG/Data_base_eolien/VENT/synop.202312.csv.gz', sep=';')

# Conserver seulement les colonnes spécifiées
data_csv = data_csv.filter(items=['numer_sta', 'date', 'dd', 'ff', 'raf10', 'rafper', 'per'])

# Fusionner les deux DataFrames sur la colonne 'ID' au lieu de 'numer_sta'
merged_data = pd.merge(data_csv, df, left_on='numer_sta', right_on='ID')

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
# Afficher les statistiques de chaque groupe
for name, group in grouped_data:
    print(f"\nVille {name}:")
    print(group.to_string())
    NbVille += 1
print(NbVille)