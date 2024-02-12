# Dictionnaire solaire original
dico_solaire_original = {
    1300: {'2A': 'Corse du Sud', '2B': 'Haute Corse', '09': 'Ariege', '66': 'Pyrenees Orientals', '11': 'Aude',
           '34': 'Herault', '48': 'Lozere', '30': 'Gard', '07': 'Ardeche', '26': 'Drome', '05': 'Hautes Alpes',
           '84': 'Vaucluse', '13': 'Bouche du Rhone', '83': 'Var', '06': 'Alpes Maritimes',
           '04': 'Alpes de Haute Provence', '47': 'Lot et Garonne'},
    1150: {'31': 'Haute Garonne', '81':'Tarn', '12': 'Aveyron', '15': 'Cantal', '43': 'Haute Loire',
           '38': 'Isere', '73': 'Savoie', '65': 'Haute Pyrenees', '64': 'Pyrenees Atlantique', '40': 'Landes',
           '32': 'Gers', '82': 'Tarnet Garonne', '46': 'Lot', '33': 'Gironde', '17': 'Charente Maritime',
           '18': 'Charente', '86': 'Vienne', '79': 'Deux Sevres', '85': 'Vendee', '87': 'Haute Vienne', '19': 'Correze'
           ,'63': 'Puy de Dome', '42': 'Loire', '69': 'Rhone', '24': 'Dordogne'},
    1050: {'29': 'Finistere', '22': 'Cote Armor', '56': 'Morbihan', '53': 'Mayenne', '44': 'Loire Atlantique',
           '72': 'Sarthe', '49': 'Maine et Loire', '41': 'Loir et Cher', '37': 'Indre et Loire', '18': 'Cher',
           '36': 'Indre', '23': 'Creuse', '03': 'Allier', '58': 'Nievre', '71': 'Saone et Loire', '01': 'Ain',
           '74': 'Haute Savoie', '35': 'Ille et Vilaine'},
    900: {'50': 'Manche', '14': 'Calvados', '61': 'Orne', '27': 'Eure', '76': 'Seine Maritime', '28': 'Eure et Loir',
          '45': 'Loiret', '78': 'Paris', '95': 'Paris', '91': 'Essone', '77': 'Paris', '1': 'Paris', '60': 'Oise',
          '80': 'Somme', '02': 'Aisne', '62': 'Pas de Calais', '59': 'Nord', '89': 'Yonne', '21': 'Cote Or',
          '10': 'Aube', '51': 'Marne', '08': 'Ardennes', '52': 'Haute Marne', '55': 'Meuse', '54': 'Meurthe et Moselle',
          '57': 'Moselle', '88': 'Vosges', '67': 'Bas Rhin', '68':'Haut Rhin', '70': 'Haute Saone', '25': 'Doubs',
          '39': 'Jura', '90': 'Territoire Belfort', '92': 'Haut de Seine', '93': 'Seine Saint Denis',
          '94': 'Val de Marne'}
}

# Inverser le dictionnaire solaire pour associer chaque département à la puissance solaire
dico_puissance_solaire = {}
for puissance, departements in dico_solaire_original.items():
    if isinstance(departements, dict):
        for departement, nom_departement in departements.items():
            dico_puissance_solaire[departement] = puissance
    else:
        dico_puissance_solaire[departements] = puissance

# Afficher le dictionnaire de puissance solaire
print(dico_puissance_solaire)

# Créer un dictionnaire qui associe chaque département à son nom
dico_noms_departements = {}
for puissance, departements in dico_solaire_original.items():
    if isinstance(departements, dict):
        for departement, nom_departement in departements.items():
            dico_noms_departements[departement] = nom_departement
    else:
        dico_noms_departements[departements] = departements  # Si la valeur est un numéro de département unique, utiliser ce numéro comme nom

# Afficher le dictionnaire des noms de départements
print(dico_noms_departements)