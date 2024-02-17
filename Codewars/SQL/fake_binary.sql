-- Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

-- Note: input will never be an empty string

-- return x as original col and res as output

select x,   regexp_replace(regexp_replace(x, '[0-4]', '0', 'g'), '[5-9]', '1', 'g')
AS res from fakebin;

SELECT x, TRANSLATE(x, '123456789', '000011111') AS res 
FROM fakebin

select x, replace(
  replace(
    replace(
      replace(
        replace(
          replace(
            replace(
              replace(
                replace(
                  replace( x, '4', '0')
                  ,'3', '0')
                , '2', '0')
              , '1', '0')
            , '0', '0')
          , '5', '1')
        , '6', '1')
      , '7', '1')
    , '8', '1')
  , '9', '1') as res
from fakebin