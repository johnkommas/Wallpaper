/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

SELECT      count(distinct IMP_MobileDocumentHeaders.Code)                     AS DOCS,
            count(IMP_MobileDocumentLines.BarCode)                             AS LINES,
            CASE
                WHEN OrderType in ('ΑΤΔ', 'ΑΔΠ', 'ΑΧΔ') THEN 'ΑΓΟΡΕΣ'
                WHEN OrderType = 'ΔΕΑ'                  THEN 'ΕΠΙΣΤΡΟΦΕΣ'
                WHEN OrderType = 'ΔΕΝ'                  THEN 'ΕΝΔΟΔΙΑΚΙΝΗΣΕΙΣ'
                WHEN OrderType = 'ΠΠΡ'                  THEN 'ΠΑΡΑΓΓΕΛΙΕΣ'
                WHEN OrderType = 'ΑΠ_ΜΟΒ'               THEN 'ΡΑΦΙ ΤΙΜΕΣ'
                ELSE 'ΛΟΙΠΑ'
                END                                                            AS 'TYPE'
            FROM IMP_MobileDocumentLines
            left join IMP_MobileDocumentHeaders
            on IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
            left join ESFITradeAccount
            on ESFITradeAccount.gid = IMP_MobileDocumentHeaders.Supplier
            WHERE

            convert(varchar, RealImportTime, 102) =  convert(varchar, getdate(), 102)

            GROUP BY
                CASE
                WHEN OrderType in ('ΑΤΔ', 'ΑΔΠ', 'ΑΧΔ') THEN 'ΑΓΟΡΕΣ'
                WHEN OrderType = 'ΔΕΑ'                  THEN 'ΕΠΙΣΤΡΟΦΕΣ'
                WHEN OrderType = 'ΔΕΝ'                  THEN 'ΕΝΔΟΔΙΑΚΙΝΗΣΕΙΣ'
                WHEN OrderType = 'ΠΠΡ'                  THEN 'ΠΑΡΑΓΓΕΛΙΕΣ'
                WHEN OrderType = 'ΑΠ_ΜΟΒ'               THEN 'ΡΑΦΙ ΤΙΜΕΣ'
                ELSE 'ΛΟΙΠΑ'
                END