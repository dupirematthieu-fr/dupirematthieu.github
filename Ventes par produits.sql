# query: je demande à la base de données "ventes" qu'elle me retourne 3 champs, le type de produits (c2), la somme du nombre de produits vendus (SUM(c4)) ainsi que le chiffre d affaire par produit (SUM(c3*c4))
# je lui demande de les trier selon l'ordre de la colonne c2, en omettant l'enregistrement "produit" pour une meilleure lisibilité
  
SELECT c2 , SUM(c4) AS vente_par_produit , SUM(c3*c4) AS chiffre_d_affaire_par_produit
FROM ventes
WHERE c2 != 'produit'
GROUP BY c2
