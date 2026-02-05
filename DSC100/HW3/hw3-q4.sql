     WITH Direct AS (
             SELECT DISTINCT dest_city
               FROM flights
              WHERE origin_city = '"San Diego CA"'
          ),
          OneStop AS (
             SELECT DISTINCT f2.dest_city
               FROM flights f1
               JOIN flights f2 ON f1.dest_city = f2.origin_city
              WHERE f1.origin_city = '"San Diego CA"'
          )
   SELECT dest_city AS city
     FROM OneStop
    WHERE dest_city NOT IN (
             SELECT dest_city
               FROM Direct
          )
      AND dest_city != '"San Diego CA"'
 ORDER BY city;