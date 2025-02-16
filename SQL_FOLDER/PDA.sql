/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

SELECT
    COUNT(DISTINCT IMP_MobileDocumentHeaders.Code) AS DOCS,
    COUNT(IMP_MobileDocumentLines.BarCode) AS LINES,
    IMP_MobileDocumentHeaders.PdaId AS PdaId,
    CASE
        WHEN OrderType IN ('ΑΤΔ', 'ΑΔΠ', 'ΑΧΔ') THEN 'ΑΓΟΡΕΣ'
        WHEN OrderType = 'ΔΕΑ' THEN 'ΕΠΙΣΤΡΟΦΕΣ'
        WHEN OrderType = 'ΔΕΝ' THEN 'ΕΝΔΟΔΙΑΚΙΝΗΣΕΙΣ'
        WHEN OrderType = 'ΠΠΡ' THEN 'ΠΑΡΑΓΓΕΛΙΕΣ'
        WHEN OrderType = 'ΑΠ_ΜΟΒ' THEN 'ΡΑΦΙ ΤΙΜΕΣ'
        ELSE 'ΛΟΙΠΑ'
        END AS TYPE,
    CASE
        WHEN IMP_MobileDocumentHeaders.CheckState = 1 THEN 'Ναι'
        ELSE 'Όχι'
        END AS Katahorimeno,
--     FORMAT(RealImportTime, 'dd MMM', 'el-GR') AS 'MONTH'
    FORMAT(RealImportTime, 'MMM', 'el-GR') AS 'MONTH'
FROM IMP_MobileDocumentLines
         LEFT JOIN IMP_MobileDocumentHeaders
                   ON IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
         LEFT JOIN ESFITradeAccount
                   ON ESFITradeAccount.gid = IMP_MobileDocumentHeaders.Supplier
WHERE
    DATEPART(YEAR, RealImportTime) = DATEPART(YEAR, GETDATE())
-- AND DATEPART(MONTH, RealImportTime) = DATEPART(MONTH, GETDATE())
GROUP BY
    FORMAT(RealImportTime, 'MMM', 'el-GR'),
--     FORMAT(RealImportTime, 'dd MMM', 'el-GR'),
    CASE
        WHEN OrderType IN ('ΑΤΔ', 'ΑΔΠ', 'ΑΧΔ') THEN 'ΑΓΟΡΕΣ'
        WHEN OrderType = 'ΔΕΑ' THEN 'ΕΠΙΣΤΡΟΦΕΣ'
        WHEN OrderType = 'ΔΕΝ' THEN 'ΕΝΔΟΔΙΑΚΙΝΗΣΕΙΣ'
        WHEN OrderType = 'ΠΠΡ' THEN 'ΠΑΡΑΓΓΕΛΙΕΣ'
        WHEN OrderType = 'ΑΠ_ΜΟΒ' THEN 'ΡΑΦΙ ΤΙΜΕΣ'
        ELSE 'ΛΟΙΠΑ'
        END,
    IMP_MobileDocumentHeaders.CheckState,
     IMP_MobileDocumentHeaders.PdaId;