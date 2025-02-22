/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

SELECT COUNT(DISTINCT ESFIItem.Code) AS COUNT
FROM ESFIItem
    INNER JOIN ES00HistoryLogRawData
        ON ESFIItem.GID = ES00HistoryLogRawData.fPK
WHERE
    CAST(ESDModified AS DATE) = CAST(GETDATE() AS DATE)
    AND ES00HistoryLogRawData.TableID = 'ESMMStockItem'
    AND ES00HistoryLogRawData.FieldID = 'RetailPrice'
    AND CAST(ES00HistoryLogRawData.HDate AS DATE) = CAST(GETDATE() AS DATE);
