/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

 SELECT
       isnull(count(ESFIItem.Code),0)                                                     AS COUNT
FROM ESFIPricelistItem
         LEFT JOIN ESFIItem
                   on ESFIPricelistItem.fItemGID = ESFIItem.GID
         INNER JOIN ESFIPricelist
                    on ESFIPricelistItem.fPricelistGID = ESFIPricelist.GID
WHERE convert(varchar, GETDATE(), 102) BETWEEN  convert(varchar, ValidFromDate, 102) AND convert(varchar, ValidToDate, 102)
