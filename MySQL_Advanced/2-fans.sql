-- Rank country origins of bands by the number of (non-unique) fans
SELECT origin, SUM(nb_fans) as total_fans
FROM metal_bands
GROUP BY origin
ORDER BY total_fans DESC;