   SELECT origin_city,
          100.0 * AVG(
          CASE
                    WHEN actual_time < 180 THEN 1
                    ELSE 0
          END
          ) AS percentage
     FROM flights
 GROUP BY origin_city
 ORDER BY percentage;