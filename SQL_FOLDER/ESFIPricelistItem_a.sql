/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

SELECT
    COUNT(ESFIItem.Code) AS COUNT -- Υπολογισμός του συνολικού αριθμού των κωδικών (Code)
FROM
    ESFIPricelistItem
    LEFT JOIN ESFIItem
        ON ESFIPricelistItem.fItemGID = ESFIItem.GID -- Σύνδεση με τον πίνακα των αντικειμένων βάσει GID
    INNER JOIN ESFIPricelist
        ON ESFIPricelistItem.fPricelistGID = ESFIPricelist.GID -- Σύνδεση με τον πίνακα των τιμοκαταλόγων βάσει GID
WHERE
    GETDATE() BETWEEN ValidFromDate AND ValidToDate -- Φίλτρο για το διάστημα ισχύος του τιμοκαταλόγου
