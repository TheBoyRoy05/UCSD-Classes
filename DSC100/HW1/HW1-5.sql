SELECT Artists.Name,
    Albums.Title
FROM Artists
    JOIN Albums USING (ArtistId)
ORDER BY Artists.Name;