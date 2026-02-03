SELECT
    C.name as name,
    AVG(canceled) * 100.0 AS percent
FROM
    Flights F
    JOIN Carriers C ON F.carrier_id = C.cid
WHERE
    F.origin_city = 'San Diego CA'
GROUP BY
    C.cid
HAVING
    percent > 1
ORDER BY
    percent;

-- 5 rows