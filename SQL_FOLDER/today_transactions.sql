/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

SELECT
    COUNT(*) AS 'COUNT'
FROM
    ESFIDocumentTrade
WHERE
    fShippingPurposeCode = N'ΠΩΛΗΣΗ'
    AND fADSiteGID = N'86947579-6885-4E86-914E-46378DB3794F'
    AND (ADCode LIKE N'ΤΔΑ%' OR ADCode LIKE N'ΑΠΛ%')
    AND CONVERT(date, ESDCreated) = CONVERT(date, GETDATE());
