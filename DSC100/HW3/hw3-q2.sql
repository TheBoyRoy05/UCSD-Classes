   SELECT DISTINCT origin_city AS city
     FROM flights
    WHERE origin_city NOT IN (
             SELECT DISTINCT origin_city
               FROM flights
              WHERE actual_time >= 180
          )
 ORDER BY city;