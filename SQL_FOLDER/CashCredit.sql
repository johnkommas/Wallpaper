DECLARE @Year      INT  = YEAR(GETDATE());
DECLARE @StartDate DATE = DATEFROMPARTS(@Year, 1, 1);
DECLARE @EndDate   DATE = DATEADD(YEAR,       1, @StartDate);

;WITH Aggregates AS (
    SELECT
        DS.Description                                    AS Description1,
        COUNT(DISTINCT T.GID)                             AS TotalCount,
        SUM(CASE WHEN L.CashValue        > 0 THEN 1 ELSE 0 END) AS CashCount,
        SUM(CASE WHEN L.CreditCardsValue > 0 THEN 1 ELSE 0 END) AS CreditCount
    FROM ESFIDocumentTrade AS T
    LEFT JOIN ESFIDocumentSeries AS DS
        ON T.fADDocumentSeriesGID = DS.GID
    LEFT JOIN (
        SELECT
            fDocumentGID,
            SUM(CASE WHEN LineType = 0 THEN LiquidityValue ELSE 0 END)                        AS CashValue,
            SUM(CASE WHEN LineType = 1 AND CA.ConcernsCard = 1 THEN LiquidityValue ELSE 0 END) AS CreditCardsValue
        FROM ESFILineLiquidityAccount AS L
        LEFT JOIN ESFICashAccount AS CA
            ON L.fLiquidityAccountGID = CA.GID
        GROUP BY fDocumentGID
    ) AS L
        ON T.GID = L.fDocumentGID
    WHERE
        T.ADRegistrationDate >= @StartDate
        AND T.ADRegistrationDate <  @EndDate
        AND T.fTradeAccountGID IS NOT NULL
        AND DS.Description IN (
            N'Δελτίο Αποστολής - Απόδειξη Λιανικής Πώλησης'
        )
    GROUP BY
        DS.Description
)

SELECT
    Description1,
    TotalCount,
    CashCount,
    CreditCount,
    CAST(CashCount   * 100.0 / NULLIF(TotalCount,0) AS DECIMAL(5,2)) AS CashPercent,
    CAST(CreditCount * 100.0 / NULLIF(TotalCount,0) AS DECIMAL(5,2)) AS CreditPercent
FROM Aggregates
ORDER BY TotalCount DESC;