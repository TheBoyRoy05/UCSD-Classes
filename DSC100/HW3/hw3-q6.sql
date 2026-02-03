   SELECT DISTINCT C.name AS carrier
     FROM flights F
     JOIN carriers C ON F.carrier_id = C.cid
    WHERE F.origin_city = '"San Diego CA"'
      AND F.dest_city = '"San Francisco CA"'
 ORDER BY carrier;