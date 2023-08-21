/*
 * Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved
 */

SELECT

       DATEPART(DAY,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) as 'DAY',
       DATEPART(month,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) as 'MONTH',
       DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) as 'YEAR',
       isnull(Sum(ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_TurnOver),0) AS 'TurnOver'



FROM ESFIItemEntry_ESFIItemPeriodics AS ESFIItemEntry_ESFIItemPeriodics

     LEFT JOIN ESFIItem AS FK_ESFIItemEntry_ESFIItemPeriodics_ESFIItem
       ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = FK_ESFIItemEntry_ESFIItemPeriodics_ESFIItem.GID
     LEFT JOIN ESGOSites AS FK_ESFIItemEntry_ESGOSites_Site
       ON ESFIItemEntry_ESFIItemPeriodics.fSiteGID = FK_ESFIItemEntry_ESGOSites_Site.GID
     LEFT JOIN ESFISalesPerson AS FK_ESFIItemEntry_ESFISalesPerson
       ON ESFIItemEntry_ESFIItemPeriodics.fSalesPersonGID = FK_ESFIItemEntry_ESFISalesPerson.GID
WHERE
        (ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty <> 0)
        AND ESFIItemEntry_ESFIItemPeriodics.fSiteGID= '86947579-6885-4E86-914E-46378DB3794F'
        AND DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) >= :year
        AND DATEPART(Month,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = :month

GROUP BY
DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate),
DATEPART(month,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate),
DATEPART(DAY,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate)

ORDER BY 3,2,1