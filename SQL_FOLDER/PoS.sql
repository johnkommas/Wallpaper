-- CTE για Query_ESFIMyDataPaymentRequestTransaction
WITH Query_ESFIMyDataPaymentRequestTransaction AS (
    SELECT 
        ESFIMyDataPaymentRequestTransaction.fMyDataPaymentRequestGID AS fMyDataPaymentRequestGID,
        SUM(ESFIMyDataPaymentRequestTransaction.Status) AS StatusInt
    FROM ESFIMyDataPaymentRequestTransaction AS ESFIMyDataPaymentRequestTransaction
    WHERE ESFIMyDataPaymentRequestTransaction.Status = 1
    GROUP BY ESFIMyDataPaymentRequestTransaction.fMyDataPaymentRequestGID
),
-- CTE για FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1
FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1 AS (
    SELECT 
        ESFIDocumentDirectory.fDocumentGID AS fDocumentGID,
        ESFIDocumentDirectory.fCompanyCode AS fCompanyCode,
        ESFIDocumentDirectory.ADPrinted AS ADPrinted,
        ESFIDocumentDirectory.ADCode AS ADCode,
        ISNULL(ESFIEInvoiceProviderDetails.MarkID, CAST(FK_ESFIMyDataReferenceDocument_ESFIMyDatainvoice.mark AS NVARCHAR)) AS MARK
    FROM ESFIDocumentDirectory AS ESFIDocumentDirectory
    LEFT JOIN ESFIEinvoiceProviderDetails AS ESFIEInvoiceProviderDetails
        ON ESFIDocumentDirectory.fDocumentGID = ESFIEInvoiceProviderDetails.fDocumentGID
    LEFT JOIN ESFIMyDataReferenceDocument AS ESFIMyDataReferenceDocument
        ON ESFIDocumentDirectory.fDocumentGID = ESFIMyDataReferenceDocument.fDocumentGID
    INNER JOIN ESFIMyDataInvoice AS FK_ESFIMyDataReferenceDocument_ESFIMyDatainvoice
        ON ESFIMyDataReferenceDocument.fMyDataInvoiceGID = FK_ESFIMyDataReferenceDocument_ESFIMyDatainvoice.GID
),
-- CTE για ProcessedStatus
ProcessedStatus AS (
    SELECT 
        ESFIMyDataPaymentRequest.GID,
        CASE
            WHEN ESFIMyDataPaymentRequest.SignatureSignDateTime <= DATEADD(MINUTE, 10, GETDATE())
                 AND ESFIMyDataPaymentRequest.SignatureSignDateTime >= DATEADD(MINUTE, -10, GETDATE())
                 AND ESFIMyDataPaymentRequest.Status = 0
                 AND FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID IS NULL THEN 0
            WHEN ESFIMyDataPaymentRequest.Status = 0
                 AND FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID IS NOT NULL
                 AND ISNULL(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted, 0) <> 1 THEN 0
            WHEN (FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID IS NULL
                 OR ISNULL(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted, 0) <> 1)
                 AND ESFIMyDataPaymentRequest.Status = 0
                 AND Query_ESFIMyDataPaymentRequestTransaction.StatusInt > 0 THEN 1
            WHEN ESFIMyDataPaymentRequest.Status = 0
                 AND ESFIMyDataPaymentRequest.SignatureExpirationDate <= GETDATE() THEN 6
            WHEN ESFIMyDataPaymentRequest.Status = 0
                 AND Query_ESFIMyDataPaymentRequestTransaction.StatusInt > 0 THEN 2
            WHEN ESFIMyDataPaymentRequest.Status = 0
                 AND ISNULL(Query_ESFIMyDataPaymentRequestTransaction.StatusInt, 0) = 0 THEN 3
            WHEN ESFIMyDataPaymentRequest.Status = 4
                 AND ESFIMyDataPaymentRequest.Preloaded = 1 THEN 7
            WHEN ESFIMyDataPaymentRequest.Status = 4 THEN 8
            WHEN ESFIMyDataPaymentRequest.Status = 1 THEN 4
            WHEN ESFIMyDataPaymentRequest.Status = 2 THEN 5
            WHEN ESFIMyDataPaymentRequest.Status = 11 THEN 9
            ELSE 4
        END AS CalculatedStatus
    FROM ESFIMyDataPaymentRequest AS ESFIMyDataPaymentRequest
    LEFT JOIN Query_ESFIMyDataPaymentRequestTransaction
        ON ESFIMyDataPaymentRequest.GID = Query_ESFIMyDataPaymentRequestTransaction.fMyDataPaymentRequestGID
    LEFT JOIN FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1
        ON ESFIMyDataPaymentRequest.DocumentID = FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID
)
SELECT 
    CASE
        WHEN CalculatedStatus = 0 THEN 'Υπό επεξεργασία'
        WHEN CalculatedStatus = 1 THEN 'Προς ακύρωση'
        WHEN CalculatedStatus = 2 THEN 'Προς έγκριση'
        WHEN CalculatedStatus = 3 THEN 'Προς απόρριψη'
        WHEN CalculatedStatus = 4 THEN 'Αποτυχημένη'
        WHEN CalculatedStatus = 5 THEN 'Επιτυχημένη'
        WHEN CalculatedStatus = 6 THEN 'Ληγμένη'
        WHEN CalculatedStatus = 7 THEN 'Προφορτωμένη'
        WHEN CalculatedStatus = 8 THEN 'Εκκρεμής'
        WHEN CalculatedStatus = 9 THEN 'Προς Αποστολή'
        ELSE 'Ληγμένη'
    END AS Status,
    ESFIMyDataPaymentRequest.POSID AS POSID,
    ESFIMyDataPaymentRequest.ESDCreated
FROM ProcessedStatus
LEFT JOIN ESFIMyDataPaymentRequest 
    ON ProcessedStatus.GID = ESFIMyDataPaymentRequest.GID
WHERE CAST(ESFIMyDataPaymentRequest.ESDCreated AS DATE) = CAST(GETDATE() AS DATE)
-- WHERE ESFIMyDataPaymentRequest.ESDCreated >= DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE()), 0)
--   AND ESFIMyDataPaymentRequest.ESDCreated < DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE()) + 1, 0)
ORDER BY ESFIMyDataPaymentRequest.ESDCreated;