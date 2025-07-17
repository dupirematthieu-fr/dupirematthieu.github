# Pour ce programme j'ai repris le précédent programme proposé dans l'exercice en y apportant des modifications: dans la variable figure j'utilise 'qte' en 'values'
# 'region' en 'names' et je modifie le titre par 'quantité vendue par région'. De la même manière je modifie le nom du fichier html créé par 'ventes-par-région.html'
# Le résultat sous forme de graphique est disponible dans le document Word "Projet_Analyse_des_ventes_PME_DUPIRE_Matthieu.docx" disponible dans le Github.

import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')
