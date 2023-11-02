-- Given the following table 'decimals':

-- decimals table schema
-- id
-- number1
-- number2
-- Return a table with a single column towardzero where the values are the result of number1 + number2 truncated towards zero.

select trunc(number1+number2) as towardzero from decimals;

--
SELECT CASE 
          WHEN number1+number2>0 
             THEN FLOOR(number1+number2)
          ELSE CEILING(number1+number2)
       END as towardzero
FROM decimals;