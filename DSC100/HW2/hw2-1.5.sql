SELECT CustomerId, SUM(Total) AS Total
FROM invoices
GROUP BY CustomerId;