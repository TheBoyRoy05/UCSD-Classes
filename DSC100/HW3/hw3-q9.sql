   SELECT DISTINCT A.name
     FROM artist A
    WHERE NOT EXISTS (
             SELECT 1
               FROM track
               JOIN album AL USING (album_id)
               JOIN genre G USING (genre_id)
              WHERE G.name = 'Blues'
                AND A.artist_id = AL.artist_id
          )
 ORDER BY A.name;