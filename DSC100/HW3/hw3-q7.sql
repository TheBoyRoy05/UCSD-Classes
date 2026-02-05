   SELECT DISTINCT NAME
     FROM track T
    WHERE NOT EXISTS (
             SELECT 1
               FROM invoice_line I
              WHERE I.track_id = T.track_id
          )
 ORDER BY NAME;