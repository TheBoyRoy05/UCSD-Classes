SELECT DISTINCT CustomerId
FROM invoices
    JOIN invoice_items USING (InvoiceId)
    JOIN tracks USING (TrackId)
    JOIN genres G USING (GenreId)
WHERE G.Name = 'Blues';