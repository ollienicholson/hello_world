

-- The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

-- Task
-- Given a year, return the century it is in.

-- Examples
-- 1705 --> 18
-- 1900 --> 19
-- 1601 --> 17
-- 2000 --> 20
-- In SQL, you will be given a table years with a column yr for the year. Return a table with a column century.

-- Note: this kata uses strict construction as shown in the description and the examples, you can read more about it here

SELECT CEILING(yr/100.00) AS Century
FROM years

--
select ceil(yr::real / 100) as century from years;

--
SELECT 
  CASE (YR % 100)
  WHEN 0 THEN
    YR / 100
  ELSE
    ( YR / 100 ) + 1
  END 
  AS CENTURY  
FROM YEARS;

--
select (yr+99)/100 as century from years;

--
SELECT 
  CASE
   WHEN yr%100 = 0 THEN yr/100
   WHEN yr%100 > 0 THEN yr/100+1
  END 
as century
from years