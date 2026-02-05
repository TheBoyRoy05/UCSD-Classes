   SELECT DISTINCT NAME AS carrier
     FROM carriers
    WHERE cid IN (
             SELECT DISTINCT carrier_id
               FROM flights
              WHERE origin_city = '"San Diego CA"'
                AND dest_city = '"San Francisco CA"'
          )
 ORDER BY carrier;