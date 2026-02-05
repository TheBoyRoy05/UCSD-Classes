SELECT A.Name, COUNT(*) AS Count
FROM tracks
JOIN albums USING (AlbumId)
JOIN artists A USING (ArtistId)
JOIN genres G USING (GenreId)
WHERE G.Name = 'Blues'
GROUP BY A.ArtistId;