SELECT DISTINCT
    C.name AS name,
    COUNT(*) AS flightcount
FROM
    Flights F
    JOIN Carriers C ON F.carrier_id = C.cid
WHERE
    F.origin_state = 'California'
GROUP BY
    F.month_id,
    C.cid
HAVING
    flightcount > 5000;

-- 6 rows