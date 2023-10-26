-- Grasshopper - Summation

-- Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

-- For example (Input -> Output):

-- 2 -> 3 (1 + 2)
-- 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

-- # write your SQL statement here: you are given a table 'kata' with a column 'n', 
-- return a table with 'n' and your result stored in a column naed 'res'.

WITH RECURSIVE NumberSeries AS (
  SELECT 1 AS num
  UNION ALL
  SELECT num + 1
  FROM NumberSeries
  WHERE num < (SELECT MAX(n) FROM kata)
)

SELECT kata.n, SUM(ns.num) AS res
FROM kata
JOIN NumberSeries ns
ON ns.num <= kata.n
GROUP BY kata.n
ORDER BY kata.n;


-- this is how you print stuff in sql
-- SELECT 'Hello, world!' AS message;