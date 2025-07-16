SELECT c2 , SUM(c4) AS vente_par_produit , SUM(c3*c4) AS chiffre_d_affaire_par_produit
FROM ventes
where c2 != 'produit'
GROUP BY c2
