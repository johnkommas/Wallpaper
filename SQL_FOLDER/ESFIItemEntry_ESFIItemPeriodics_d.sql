/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

SELECT
    ISNULL(COUNT(DISTINCT ESFIItem.Code), 0) AS COUNT
FROM ESFIItemEntry_ESFIItemPeriodics
     LEFT JOIN ESFIItem
        ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = ESFIItem.GID
WHERE
    ESFIItemEntry_ESFIItemPeriodics.fSiteGID = '86947579-6885-4E86-914E-46378DB3794F'
    AND (ESFIItemEntry_ESFIItemPeriodics.DocumentCode LIKE 'ΑΠΛ%' OR ESFIItemEntry_ESFIItemPeriodics.DocumentCode LIKE 'ΤΔΑ%')
    AND CAST(ESFIItemEntry_ESFIItemPeriodics.RegistrationDate AS DATE) = CAST(GETDATE() AS DATE);
