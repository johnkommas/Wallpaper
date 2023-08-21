/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

SELECT count(DISTINCT ESFIItem.Code)                                       AS COUNT
FROM ESFIItem
    LEFT JOIN ES00HistoryLogRawData
        ON ESFIItem.GID = ES00HistoryLogRawData.fPK

WHERE
       convert(varchar, ESDModified, 102) = convert(varchar, getdate(), 102)
AND (ES00HistoryLogRawData.TableID = 'ESMMStockItem')
AND (ES00HistoryLogRawData.FieldID = 'RetailPrice')
AND convert(varchar, ES00HistoryLogRawData.HDate, 102) = convert(varchar, getdate(), 102)