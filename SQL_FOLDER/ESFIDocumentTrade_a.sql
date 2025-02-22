/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

DECLARE @StartDate DATETIME = DATEADD(DAY, DATEDIFF(DAY, 0, GETDATE()), 0); -- Only today's date
DECLARE @EndDate DATETIME = GETDATE(); -- Current date and time

SELECT
    COUNT(*) AS 'COUNT',
    DATEPART(YEAR, edt.ESDCreated) AS 'YEAR'
FROM
    ESFIDocumentTrade AS edt
WHERE
    edt.fShippingPurposeCode = N'ΠΩΛΗΣΗ'
    AND edt.fADSiteGID = N'86947579-6885-4E86-914E-46378DB3794F'
    AND (edt.ADCode LIKE N'ΤΔΑ%' OR edt.ADCode LIKE N'ΑΠΛ%')
    AND DATEPART(MONTH, edt.ESDCreated) = DATEPART(MONTH, GETDATE()) -- Same month
    AND DATEPART(DAY, edt.ESDCreated) = DATEPART(DAY, GETDATE()) -- Same day
    AND edt.ESDCreated >= DATEADD(YEAR, -5, @StartDate) -- Last 5 years
    AND edt.ESDCreated <= @EndDate -- Up to current time today
GROUP BY
    DATEPART(YEAR, edt.ESDCreated) -- Group by each year
ORDER BY
    DATEPART(YEAR, edt.ESDCreated);