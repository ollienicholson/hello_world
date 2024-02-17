-- Centered pentagonal number
-- Complete the function that takes an integer and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.

-- In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots. On the third, there are 16 dots, and on the fourth there are 31 dots. The sequence is: 1, 6, 16, 31...


-- If the input is equal to or less than 0, return -1


WITH RECURSIVE PentagonalDots AS (
  SELECT 1 AS n, 1 AS res
  UNION ALL
  SELECT n + 1, res + (n - 1) * 5 + 5
  FROM PentagonalDots
  WHERE n BETWEEN -1000 AND 100000
)

SELECT pentagonal.n, CASE
         WHEN pentagonal.n <= 0 THEN -1
         ELSE PentagonalDots.res
       END AS res
FROM pentagonal
left join PentagonalDots on pentagonal.n = PentagonalDots.n


-- ALTERNATIVE
SELECT n, CASE
              WHEN n <= 0 THEN -1
              ELSE (5 * (n * (n - 1)/2) + 1) 
          END AS res    
FROM pentagonal;