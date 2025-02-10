/*
 * Copyright (c) Ioannis E. Kommas 2025. All Rights Reserved
 */

SELECT
    FiscalMonth,
    COALESCE(SUM(TurnOver), 0) AS TurnOver
FROM
    ESFIItemPeriodics AS ItemPeriodics
    INNER JOIN (
        SELECT
            GID,
            MONTH(BeginDate) AS FiscalMonth
        FROM ESGOFiscalPeriod
        WHERE BeginDate BETWEEN DATEADD(YEAR, DATEDIFF(YEAR, 0, GETDATE()), 0) -- Πρώτη μέρα του έτους
                          AND EOMONTH(GETDATE()) -- Τελευταία μέρα του τρέχοντος μήνα
    ) AS FiscalPeriod
        ON ItemPeriodics.fFiscalPeriodGID = FiscalPeriod.GID
GROUP BY
    FiscalMonth
ORDER BY
    FiscalMonth;