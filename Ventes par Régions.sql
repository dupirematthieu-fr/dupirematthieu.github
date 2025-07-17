# query: je demande à la base de données "ventes" de me retourner 3 champs: la région (c5), la somme du nombre de produits vendus par région (SUM(c4)) ainsi que le chiffre d'affaire par région (SUM(c3*c4))
# je lui demande de les trier selon la région (GROUP BY c5), et de supprimer l'enregistrement "region" du résultat pour une meilleure lisibilité (WHERE c5 != 'region')  

SELECT c5 , SUM(c4) AS ventes_par_region , SUM(c3*c4) AS chiffre_d_affaire_par_region
FROM ventes
WHERE c5 != 'region'
GROUP BY c5
