SELECT InvoiceId, Total
FROM invoices
WHERE BillingCountry IN ('USA', 'Canada')
ORDER BY InvoiceId DESC;