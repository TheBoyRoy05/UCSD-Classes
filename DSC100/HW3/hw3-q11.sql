   SELECT A.name
     FROM artist A
     JOIN album USING (artist_id)
     JOIN track USING (album_id)
     JOIN genre G USING (genre_id)
 GROUP BY A.name
   HAVING COUNT(DISTINCT G.genre_id) >= 3
 ORDER BY A.name;