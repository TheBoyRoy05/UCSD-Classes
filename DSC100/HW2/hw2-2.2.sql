SELECT
    SUM(capacity) AS totalcapacity
FROM
    Flights
WHERE
    (
        (
            origin_city = 'San Diego CA'
            AND dest_city = 'San Francisco CA'
        )
        OR (
            origin_city = 'San Francisco CA'
            AND dest_city = 'San Diego CA'
        )
    )
    AND month_id = 7
    AND day_of_month = 1;

-- 1 row