# query: je demande la somme des prix de ventes de tous les produits (c3*c4) que je nomme "chiffre_d_affaire_total" depuis la table "ventes"

SELECT SUM(c3*c4) AS chiffre_d_affaire_total
FROM ventes
