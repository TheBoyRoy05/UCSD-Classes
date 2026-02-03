SELECT BillingCountry, COUNT(*) AS NumInvoices
FROM invoices
GROUP BY BillingCountry
ORDER BY BillingCountry;