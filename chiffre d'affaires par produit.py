# Pour ce programme j'ai repris le précédent programme proposé dans l'exercice en y apportant des modifications: dans un premier temps je crée une nouvelle "données":
# je crée la donnée 'chiffre_affaires' comme étant le produit de la donnée déjà existante 'qte' et de la donnée existante 'prix'. Ensuite dans la variable figure
# j'utilise 'chiffre_affaires' en 'values', 'produits' en 'names' et je modifie le titre par 'chiffre affaires par produit'. De la même manière je modifie le nom du 
# fichier html créé par 'chiffre-affaires-par-produit.html'.
# Le résultat sous forme de graphique est disponible dans le document Word "Projet_Analyse_des_ventes_PME_DUPIRE_Matthieu.docx" disponible dans le Github.

import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
données ['chiffre_affaires'] = données ['qte'] * données ['prix']
figure = px.pie(données, values='chiffre_affaires', names='produit', title='chiffre affaires par produit')

figure.write_html('chiffre-affaires-par-produit.html')

print('chiffre-affaires-par-produit.html généré avec succès !')
