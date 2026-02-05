   SELECT DISTINCT P.name
     FROM playlist P
    WHERE NOT EXISTS (
             SELECT 1
               FROM track
               JOIN playlist_track PT USING (track_id)
               JOIN genre G USING (genre_id)
              WHERE (G.name = 'Rock'
                 OR G.name = 'Blues')
                AND PT.playlist_id = P.playlist_id
          )
 ORDER BY P.name;