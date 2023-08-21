/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

SELECT
    isnull(count(Distinct ESFIItem.Code),0)                                                                    AS COUNT
FROM ESFIItemEntry_ESFIItemPeriodics
     LEFT JOIN ESFIItem
        ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = ESFIItem.GID
WHERE   ESFIItemEntry_ESFIItemPeriodics.fSiteGID= '86947579-6885-4E86-914E-46378DB3794F'
        AND (ESFIItemEntry_ESFIItemPeriodics.DocumentCode like 'ΑΠΛ%' or ESFIItemEntry_ESFIItemPeriodics.DocumentCode like 'ΤΔΑ%')
        AND convert(varchar, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate, 102) = convert(varchar, getdate(), 102)
