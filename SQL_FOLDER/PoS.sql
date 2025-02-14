SELECT
       case
       when case
           when ESFIMyDataPaymentRequest.SignatureSignDateTime <= DATEADD(MINUTE,10,GETDATE()) and ESFIMyDataPaymentRequest.SignatureSignDateTime >= DATEADD(MINUTE,-10,GETDATE()) and ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null then 0

           when ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is not null and isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1 then 0

           when ((FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null or isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1) and ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 1

           when (ESFIMyDataPaymentRequest.Status=0 and ESFIMyDataPaymentRequest.SignatureExpirationDate<=GETDATE())then 6

           when (ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 2

           when (ESFIMyDataPaymentRequest.Status=0  and isnull(Query_ESFIMyDataPaymentRequestTransaction.StatusInt,0)=0)then 3

           when (ESFIMyDataPaymentRequest.Status=4 and ESFIMyDataPaymentRequest.Preloaded=1) then 7

           when (ESFIMyDataPaymentRequest.Status=4) then 8

           when (ESFIMyDataPaymentRequest.Status=1) then 4

           when (ESFIMyDataPaymentRequest.Status=2) then 5

           when (ESFIMyDataPaymentRequest.Status=11) then 9
           else 4

       end
       =0 then'Υπό επεξεργασία'
       when case
           when ESFIMyDataPaymentRequest.SignatureSignDateTime <= DATEADD(MINUTE,10,GETDATE()) and ESFIMyDataPaymentRequest.SignatureSignDateTime >= DATEADD(MINUTE,-10,GETDATE()) and ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null then 0

           when ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is not null and isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1 then 0

           when ((FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null or isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1) and ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 1

           when (ESFIMyDataPaymentRequest.Status=0 and ESFIMyDataPaymentRequest.SignatureExpirationDate<=GETDATE())then 6

           when (ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 2

           when (ESFIMyDataPaymentRequest.Status=0  and isnull(Query_ESFIMyDataPaymentRequestTransaction.StatusInt,0)=0)then 3

           when (ESFIMyDataPaymentRequest.Status=4 and ESFIMyDataPaymentRequest.Preloaded=1) then 7

           when (ESFIMyDataPaymentRequest.Status=4) then 8

           when (ESFIMyDataPaymentRequest.Status=1) then 4

           when (ESFIMyDataPaymentRequest.Status=2) then 5

           when (ESFIMyDataPaymentRequest.Status=11) then 9
           else 4

       end
       =1 then'Προς ακύρωση'
       when case
           when ESFIMyDataPaymentRequest.SignatureSignDateTime <= DATEADD(MINUTE,10,GETDATE()) and ESFIMyDataPaymentRequest.SignatureSignDateTime >= DATEADD(MINUTE,-10,GETDATE()) and ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null then 0

           when ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is not null and isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1 then 0

           when ((FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null or isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1) and ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 1

           when (ESFIMyDataPaymentRequest.Status=0 and ESFIMyDataPaymentRequest.SignatureExpirationDate<=GETDATE())then 6

           when (ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 2

           when (ESFIMyDataPaymentRequest.Status=0  and isnull(Query_ESFIMyDataPaymentRequestTransaction.StatusInt,0)=0)then 3

           when (ESFIMyDataPaymentRequest.Status=4 and ESFIMyDataPaymentRequest.Preloaded=1) then 7

           when (ESFIMyDataPaymentRequest.Status=4) then 8

           when (ESFIMyDataPaymentRequest.Status=1) then 4

           when (ESFIMyDataPaymentRequest.Status=2) then 5

           when (ESFIMyDataPaymentRequest.Status=11) then 9
           else 4

       end
       =2 then'Προς έγκριση'
       when case
           when ESFIMyDataPaymentRequest.SignatureSignDateTime <= DATEADD(MINUTE,10,GETDATE()) and ESFIMyDataPaymentRequest.SignatureSignDateTime >= DATEADD(MINUTE,-10,GETDATE()) and ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null then 0

           when ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is not null and isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1 then 0

           when ((FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null or isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1) and ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 1

           when (ESFIMyDataPaymentRequest.Status=0 and ESFIMyDataPaymentRequest.SignatureExpirationDate<=GETDATE())then 6

           when (ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 2

           when (ESFIMyDataPaymentRequest.Status=0  and isnull(Query_ESFIMyDataPaymentRequestTransaction.StatusInt,0)=0)then 3

           when (ESFIMyDataPaymentRequest.Status=4 and ESFIMyDataPaymentRequest.Preloaded=1) then 7

           when (ESFIMyDataPaymentRequest.Status=4) then 8

           when (ESFIMyDataPaymentRequest.Status=1) then 4

           when (ESFIMyDataPaymentRequest.Status=2) then 5

           when (ESFIMyDataPaymentRequest.Status=11) then 9
           else 4

       end
       =3 then'Προς απόρριψη'
       when case
           when ESFIMyDataPaymentRequest.SignatureSignDateTime <= DATEADD(MINUTE,10,GETDATE()) and ESFIMyDataPaymentRequest.SignatureSignDateTime >= DATEADD(MINUTE,-10,GETDATE()) and ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null then 0

           when ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is not null and isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1 then 0

           when ((FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null or isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1) and ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 1

           when (ESFIMyDataPaymentRequest.Status=0 and ESFIMyDataPaymentRequest.SignatureExpirationDate<=GETDATE())then 6

           when (ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 2

           when (ESFIMyDataPaymentRequest.Status=0  and isnull(Query_ESFIMyDataPaymentRequestTransaction.StatusInt,0)=0)then 3

           when (ESFIMyDataPaymentRequest.Status=4 and ESFIMyDataPaymentRequest.Preloaded=1) then 7

           when (ESFIMyDataPaymentRequest.Status=4) then 8

           when (ESFIMyDataPaymentRequest.Status=1) then 4

           when (ESFIMyDataPaymentRequest.Status=2) then 5

           when (ESFIMyDataPaymentRequest.Status=11) then 9
           else 4

       end
       =4 then'Αποτυχημένη'
when case
           when ESFIMyDataPaymentRequest.SignatureSignDateTime <= DATEADD(MINUTE,10,GETDATE()) and ESFIMyDataPaymentRequest.SignatureSignDateTime >= DATEADD(MINUTE,-10,GETDATE()) and ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null then 0

           when ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is not null and isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1 then 0

           when ((FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null or isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1) and ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 1

           when (ESFIMyDataPaymentRequest.Status=0 and ESFIMyDataPaymentRequest.SignatureExpirationDate<=GETDATE())then 6

           when (ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 2

           when (ESFIMyDataPaymentRequest.Status=0  and isnull(Query_ESFIMyDataPaymentRequestTransaction.StatusInt,0)=0)then 3

           when (ESFIMyDataPaymentRequest.Status=4 and ESFIMyDataPaymentRequest.Preloaded=1) then 7

           when (ESFIMyDataPaymentRequest.Status=4) then 8

           when (ESFIMyDataPaymentRequest.Status=1) then 4

           when (ESFIMyDataPaymentRequest.Status=2) then 5

           when (ESFIMyDataPaymentRequest.Status=11) then 9
           else 4

       end
       =5 then'Επιτυχημένη'
       when case
           when ESFIMyDataPaymentRequest.SignatureSignDateTime <= DATEADD(MINUTE,10,GETDATE()) and ESFIMyDataPaymentRequest.SignatureSignDateTime >= DATEADD(MINUTE,-10,GETDATE()) and ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null then 0

           when ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is not null and isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1 then 0

           when ((FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null or isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1) and ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 1

           when (ESFIMyDataPaymentRequest.Status=0 and ESFIMyDataPaymentRequest.SignatureExpirationDate<=GETDATE())then 6

           when (ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 2

           when (ESFIMyDataPaymentRequest.Status=0  and isnull(Query_ESFIMyDataPaymentRequestTransaction.StatusInt,0)=0)then 3

           when (ESFIMyDataPaymentRequest.Status=4 and ESFIMyDataPaymentRequest.Preloaded=1) then 7

           when (ESFIMyDataPaymentRequest.Status=4) then 8

           when (ESFIMyDataPaymentRequest.Status=1) then 4

           when (ESFIMyDataPaymentRequest.Status=2) then 5

           when (ESFIMyDataPaymentRequest.Status=11) then 9
           else 4

       end
       =6 then'Ληγμένη'
       when case
           when ESFIMyDataPaymentRequest.SignatureSignDateTime <= DATEADD(MINUTE,10,GETDATE()) and ESFIMyDataPaymentRequest.SignatureSignDateTime >= DATEADD(MINUTE,-10,GETDATE()) and ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null then 0

           when ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is not null and isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1 then 0

           when ((FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null or isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1) and ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 1

           when (ESFIMyDataPaymentRequest.Status=0 and ESFIMyDataPaymentRequest.SignatureExpirationDate<=GETDATE())then 6

           when (ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 2

           when (ESFIMyDataPaymentRequest.Status=0  and isnull(Query_ESFIMyDataPaymentRequestTransaction.StatusInt,0)=0)then 3

           when (ESFIMyDataPaymentRequest.Status=4 and ESFIMyDataPaymentRequest.Preloaded=1) then 7

           when (ESFIMyDataPaymentRequest.Status=4) then 8

           when (ESFIMyDataPaymentRequest.Status=1) then 4

           when (ESFIMyDataPaymentRequest.Status=2) then 5

           when (ESFIMyDataPaymentRequest.Status=11) then 9
           else 4

       end
       =7 then'Προφορτωμένη'
       when case
           when ESFIMyDataPaymentRequest.SignatureSignDateTime <= DATEADD(MINUTE,10,GETDATE()) and ESFIMyDataPaymentRequest.SignatureSignDateTime >= DATEADD(MINUTE,-10,GETDATE()) and ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null then 0

           when ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is not null and isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1 then 0

           when ((FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null or isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1) and ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 1

           when (ESFIMyDataPaymentRequest.Status=0 and ESFIMyDataPaymentRequest.SignatureExpirationDate<=GETDATE())then 6

           when (ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 2

           when (ESFIMyDataPaymentRequest.Status=0  and isnull(Query_ESFIMyDataPaymentRequestTransaction.StatusInt,0)=0)then 3

           when (ESFIMyDataPaymentRequest.Status=4 and ESFIMyDataPaymentRequest.Preloaded=1) then 7

           when (ESFIMyDataPaymentRequest.Status=4) then 8

           when (ESFIMyDataPaymentRequest.Status=1) then 4

           when (ESFIMyDataPaymentRequest.Status=2) then 5

           when (ESFIMyDataPaymentRequest.Status=11) then 9
           else 4

       end
       =8 then'Εκκρεμής'
       when case
           when ESFIMyDataPaymentRequest.SignatureSignDateTime <= DATEADD(MINUTE,10,GETDATE()) and ESFIMyDataPaymentRequest.SignatureSignDateTime >= DATEADD(MINUTE,-10,GETDATE()) and ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null then 0

           when ESFIMyDataPaymentRequest.Status=0 and FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is not null and isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1 then 0

           when ((FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID is null or isnull(FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.ADPrinted,0)<>1) and ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 1

           when (ESFIMyDataPaymentRequest.Status=0 and ESFIMyDataPaymentRequest.SignatureExpirationDate<=GETDATE())then 6

           when (ESFIMyDataPaymentRequest.Status=0  and Query_ESFIMyDataPaymentRequestTransaction.StatusInt>0)then 2

           when (ESFIMyDataPaymentRequest.Status=0  and isnull(Query_ESFIMyDataPaymentRequestTransaction.StatusInt,0)=0)then 3

           when (ESFIMyDataPaymentRequest.Status=4 and ESFIMyDataPaymentRequest.Preloaded=1) then 7

           when (ESFIMyDataPaymentRequest.Status=4) then 8

           when (ESFIMyDataPaymentRequest.Status=1) then 4

           when (ESFIMyDataPaymentRequest.Status=2) then 5

           when (ESFIMyDataPaymentRequest.Status=11) then 9
           else 4

       end
       =9 then'Προς Αποστολή'
       else 'Ληγμένη'
       end
        AS Status,
       ESFIMyDataPaymentRequest.POSID AS POSID

FROM ESFIMyDataPaymentRequest AS ESFIMyDataPaymentRequest
--      LEFT JOIN ESGOSites AS FK_ESFIMyDataPaymentRequest_ESGOSites
--        ON ESFIMyDataPaymentRequest.fSiteGID = FK_ESFIMyDataPaymentRequest_ESGOSites.GID
--      LEFT JOIN ESFIDocumentDirectory AS FK_ESFIMyDataPaymentRequest_ESFIDocumentDirectory
--        ON ESFIMyDataPaymentRequest.fRegistrationDocumentGID = FK_ESFIMyDataPaymentRequest_ESFIDocumentDirectory.fDocumentGID
     LEFT JOIN (
                SELECT ESFIMyDataPaymentRequestTransaction.fMyDataPaymentRequestGID AS fMyDataPaymentRequestGID,
                       Sum(ESFIMyDataPaymentRequestTransaction.Status) AS StatusInt
                FROM ESFIMyDataPaymentRequestTransaction AS ESFIMyDataPaymentRequestTransaction
                WHERE (ESFIMyDataPaymentRequestTransaction.Status = 1)

                GROUP BY ESFIMyDataPaymentRequestTransaction.fMyDataPaymentRequestGID) AS Query_ESFIMyDataPaymentRequestTransaction
       ON ESFIMyDataPaymentRequest.GID = Query_ESFIMyDataPaymentRequestTransaction.fMyDataPaymentRequestGID
     LEFT JOIN (
                SELECT ESFIDocumentDirectory.fDocumentGID AS fDocumentGID,
                       ESFIDocumentDirectory.fCompanyCode AS fCompanyCode,
                       ESFIDocumentDirectory.ADPrinted AS ADPrinted,
                       ESFIDocumentDirectory.ADCode AS ADCode,
                       isnull(ESFIEInvoiceProviderDetails.MarkID, cast(FK_ESFIMyDataReferenceDocument_ESFIMyDatainvoice.mark as nvarchar)) AS MARK
                FROM ESFIDocumentDirectory AS ESFIDocumentDirectory
                     LEFT JOIN ESFIEinvoiceProviderDetails AS ESFIEInvoiceProviderDetails
                       ON ESFIDocumentDirectory.fDocumentGID = ESFIEInvoiceProviderDetails.fDocumentGID
                     LEFT JOIN ESFIMyDataReferenceDocument AS ESFIMyDataReferenceDocument
                       ON ESFIDocumentDirectory.fDocumentGID = ESFIMyDataReferenceDocument.fDocumentGID
                     INNER JOIN ESFIMyDataInvoice AS FK_ESFIMyDataReferenceDocument_ESFIMyDatainvoice
                       ON ESFIMyDataReferenceDocument.fMyDataInvoiceGID = FK_ESFIMyDataReferenceDocument_ESFIMyDatainvoice.GID
                ) AS FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1
       ON ESFIMyDataPaymentRequest.DocumentID = FK_Query_ESFIDocumentDirectory_ESFIMyDataPaymentRequest1.fDocumentGID
     LEFT JOIN ESFIMyDataPaymentRequestTransaction AS FK_ESFIMyDataPaymentRequestTransaction_ESFIMyDataPaymentRequest
       ON ESFIMyDataPaymentRequest.GID = FK_ESFIMyDataPaymentRequestTransaction_ESFIMyDataPaymentRequest.fMyDataPaymentRequestGID
WHERE
      DATEPART (YEAR, ESFIMyDataPaymentRequest.ESDCreated) = DATEPART (YEAR, GETDATE())
    AND DATEPART (MONTH, ESFIMyDataPaymentRequest.ESDCreated) = DATEPART (MONTH, GETDATE())

ORDER BY ESFIMyDataPaymentRequest.ESDCreated