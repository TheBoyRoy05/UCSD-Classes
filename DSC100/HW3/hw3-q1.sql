   SELECT origin_city,
          dest_city,
          TIME
     FROM (
             SELECT DISTINCT origin_city,
                    dest_city,
                    actual_time AS TIME,
                    RANK() OVER (
                    PARTITION BY origin_city
                     ORDER BY actual_time DESC
                    ) AS RANK
               FROM flights
          )
    WHERE RANK = 1
 ORDER BY origin_city,
          dest_city;