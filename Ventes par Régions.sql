SELECT c5 , SUM(c4) AS ventes_par_region , SUM(c3*c4) AS chiffre_d_affaire_par_region
FROM ventes
where c5 != 'region'
group by c5