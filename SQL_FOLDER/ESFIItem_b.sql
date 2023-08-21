/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

SELECT
    count(DISTINCT ESFIItem.Code)                                     AS COUNT
FROM ESFIItem
LEFT JOIN ESFIItemEntry_ESFIItemPeriodics
                            ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = ESFIItem.GID
WHERE
       convert(varchar, ESFIItem.ESDCreated, 102) =  convert(varchar, getdate(), 102)