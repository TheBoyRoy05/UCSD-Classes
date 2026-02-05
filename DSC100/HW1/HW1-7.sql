SELECT Artists.Name,
    COUNT(Albums.AlbumId) AS AlbumCount
FROM Artists
    LEFT JOIN Albums USING (ArtistId)
GROUP BY Artists.Name;