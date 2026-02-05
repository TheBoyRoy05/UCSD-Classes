SELECT
    C.name AS name,
    SUM(F.departure_delay) AS delay
FROM
    Flights F
    JOIN Carriers C ON F.carrier_id = C.cid
GROUP BY
    C.cid;

-- 22 rows