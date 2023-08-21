/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

SELECT
    COUNT(*) AS 'COUNT',
    DATEPART(YEAR, ESDCreated) AS 'YEAR'
FROM
    ESFIDocumentTrade
   WHERE
        fShippingPurposeCode = N'ΠΩΛΗΣΗ'
        AND fADSiteGID = N'86947579-6885-4E86-914E-46378DB3794F'
        AND (ADCode LIKE N'ΤΔΑ%' OR ADCode LIKE N'ΑΠΛ%')
        AND  DATEPART(YEAR, ESDCreated) >= DATEPART(YEAR, GETDATE()) - 5
        AND DATEPART(MONTH, ESDCreated) = DATEPART(MONTH, GETDATE())
        AND DATEPART(DAY, ESDCreated) <= DATEPART(DAY, GETDATE())
GROUP BY
    DATEPART(YEAR, ESDCreated)
ORDER BY
    2