SELECT DISTINCT Artists.Name
FROM Artists
    JOIN Albums USING (ArtistId)
WHERE Released > '2000-01-01';