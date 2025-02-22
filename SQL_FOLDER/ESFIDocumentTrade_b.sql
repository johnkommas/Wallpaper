/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

DECLARE @StartDate DATETIME = DATEADD(YEAR, -5, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)); -- Start, 5 years from the first day of this month
DECLARE @EndDay INT = DAY(GETDATE()); -- Today's day of the month

SELECT
    COUNT(*) AS 'COUNT',
    DATEPART(YEAR, ESDCreated) AS 'YEAR'
FROM
    ESFIDocumentTrade
WHERE
    fShippingPurposeCode = N'ΠΩΛΗΣΗ'
    AND fADSiteGID = N'86947579-6885-4E86-914E-46378DB3794F'
    AND (ADCode LIKE N'ΤΔΑ%' OR ADCode LIKE N'ΑΠΛ%')
    AND ESDCreated >= @StartDate -- Only include the last 5 years from this month
    AND DATEPART(MONTH, ESDCreated) = MONTH(GETDATE()) -- Current month
    AND DATEPART(DAY, ESDCreated) <= @EndDay -- Up to today's day of the month
GROUP BY
    DATEPART(YEAR, ESDCreated)
ORDER BY
    DATEPART(YEAR, ESDCreated);
