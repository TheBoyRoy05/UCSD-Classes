   SELECT DISTINCT T.name
     FROM track T
    WHERE NOT EXISTS (
             SELECT 1
               FROM playlist P
               JOIN playlist_track PT USING (playlist_id)
              WHERE P.name LIKE '%90%'
                AND PT.track_id = T.track_id
          )
 ORDER BY T.name