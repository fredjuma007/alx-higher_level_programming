--SHAZAM
SELECT score score, name FROM second_TABLE
WHERE name <> ''
GROUP BY score DESC, name DESC;
