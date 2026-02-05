SELECT AlbumId,
    COUNT(*) AS NumTracks
FROM tracks
GROUP BY AlbumId
HAVING COUNT(*) >= 25;