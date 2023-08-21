/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

 WITH RankedRecords AS (
    SELECT *,
    ROW_NUMBER() OVER(PARTITION BY UserID ORDER BY EDate DESC) as rn
    FROM ES00EventLog
    WHERE
    id IN ('ESLOGIN','ESLOGOUT')
    AND UserID in {tuple_data}
    AND DATEPART (YEAR, EDate) = DATEPART (YEAR, GETDATE())
)
SELECT *
FROM RankedRecords
WHERE rn <= 10