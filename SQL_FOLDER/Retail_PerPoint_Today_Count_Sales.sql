-- Optimized query with indexes and faster predicate evaluation.
SELECT
    SUM(IIF(ADCode LIKE N'ΑΠΛ-Α%' OR ADCode LIKE N'ΤΔΑ-Α%', 1, 0)) AS [TAMEIO Α],
    SUM(IIF(ADCode LIKE N'ΑΠΛ-Β%' OR ADCode LIKE N'ΤΔΑ-Β%', 1, 0)) AS [TAMEIO Β]
FROM
    ESFIDocumentTrade 
WHERE
    fShippingPurposeCode = N'ΠΩΛΗΣΗ'
    AND fADSiteGID = N'86947579-6885-4E86-914E-46378DB3794F'
    AND (ADCode LIKE N'ΑΠΛ-%' OR ADCode LIKE N'ΤΔΑ-%')
--     AND ESDCreated >= CAST(GETDATE() AS DATE)
--     AND ESDCreated < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
  AND   ESFIDocumentTrade.ESDCreated >= DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE()), 0)
  AND ESFIDocumentTrade.ESDCreated < DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE()) + 1, 0);