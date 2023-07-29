#  Copyright (c) Ioannis E. Kommas 2022. All Rights Reserved


def sales_elounda(year, month, day):
    return f"""
        SELECT 

       DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) AS 'YEAR',
       isnull(Sum(ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_TurnOver),0) AS 'TurnOver',
       isnull(Sum(ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty),0) AS 'Quantity'



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
        AND DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) >= {year}
        AND DATEPART(Month,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {month}
        AND DATEPART(DAY,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) <= {day}



GROUP BY 
DATEPART(year, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate)

        """


def sales_elounda_graph(year, month):
    return f"""
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
        AND DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) >= {year}
        AND DATEPART(Month,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {month}



GROUP BY 
DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate),
DATEPART(month,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate),
DATEPART(DAY,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate)

ORDER BY 3,2,1

        """


def sales_elounda_today(year, month, day):
    return f"""
        SELECT 
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
        AND DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {year}
        AND DATEPART(Month,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {month}
        AND DATEPART(DAY,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {day}


        """


def count_elounda(year, month, day):
    return f"""
        SELECT 

       DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) AS 'YEAR',
       count( DISTINCT ESFIItemEntry_ESFIItemPeriodics.DocumentCode) AS 'TurnOver'



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
        AND DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) >= {year}
        AND DATEPART(Month,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {month}
        AND DATEPART(DAY,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) <= {day}



GROUP BY 
DATEPART(year, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate)

        """


def count_elounda_today(year, month, day):
    return f"""
        SELECT 
        count( DISTINCT ESFIItemEntry_ESFIItemPeriodics.DocumentCode) AS 'TurnOver'



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
        AND DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {year}
        AND DATEPART(Month,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {month}
        AND DATEPART(DAY,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {day}


        """


def quantity_for_tree_map(year, month):
    return f"""
SELECT 
    ESFIZItemCategory.Description as 'category',
    isnull(Sum(ESFIItemEntry_ESFIItemPeriodics.Quantity),0) AS 'QUANTITY',
    isnull(Sum(ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_TurnOver),0) AS 'SALES'

FROM ESFIItemEntry_ESFIItemPeriodics

     LEFT JOIN ESFIItem
       ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = ESFIItem.GID
     LEFT JOIN ESFIZItemFamily
       ON ESFIItem.fItemFamilyCode = ESFIZItemFamily.Code
     LEFT JOIN ESFIZItemSubfamily
       ON ESFIItem.fItemGroupCode = ESFIZItemSubfamily.Code
     LEFT JOIN ESFIZItemCategory
       ON ESFIItem.fItemCategoryCode = ESFIZItemCategory.Code
     LEFT JOIN ESGOSites AS FK_ESFIItemEntry_ESGOSites_Site
       ON ESFIItemEntry_ESFIItemPeriodics.fSiteGID = FK_ESFIItemEntry_ESGOSites_Site.GID
     LEFT JOIN ESFISalesPerson AS FK_ESFIItemEntry_ESFISalesPerson
       ON ESFIItemEntry_ESFIItemPeriodics.fSalesPersonGID = FK_ESFIItemEntry_ESFISalesPerson.GID
WHERE

        (ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty <> 0)
        AND ESFIItemEntry_ESFIItemPeriodics.fSiteGID= '86947579-6885-4E86-914E-46378DB3794F'
        AND convert(varchar, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate, 102) = convert(varchar, getdate(), 102)
GROUP BY
--     ESFIZItemFamily.Description
--     ESFIZItemSubfamily.Description
    ESFIZItemCategory.Description
--     ESFIItem.Description,
--     ESFIItem.BarCode
ORDER BY 3 DESC
        """


def quantity_for_subcategory(year, month):
    return f"""
SELECT 
--     ESFIItem.Description  AS 'ΠΕΡΙΓΡΑΦΗ',
--     ESFIItem.BarCode AS 'ΚΩΔΙΚΟΣ',
--     ESFIZItemFamily.Description as 'ΟΙΚΟΓΕΝΕΙΑ',
--     ESFIZItemSubfamily.Description as 'ΟΜΑΔΑ',
--     ESFIZItemCategory.Description as 'category',
    ESFIItem.fItemSubcategoryCode as 'category',
    isnull(Sum(ESFIItemEntry_ESFIItemPeriodics.Quantity),0) AS 'QUANTITY'

FROM ESFIItemEntry_ESFIItemPeriodics

     LEFT JOIN ESFIItem
       ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = ESFIItem.GID
     LEFT JOIN ESFIZItemFamily
       ON ESFIItem.fItemFamilyCode = ESFIZItemFamily.Code
     LEFT JOIN ESFIZItemSubfamily
       ON ESFIItem.fItemGroupCode = ESFIZItemSubfamily.Code
     LEFT JOIN ESFIZItemCategory
       ON ESFIItem.fItemCategoryCode = ESFIZItemCategory.Code
     LEFT JOIN ESGOSites AS FK_ESFIItemEntry_ESGOSites_Site
       ON ESFIItemEntry_ESFIItemPeriodics.fSiteGID = FK_ESFIItemEntry_ESGOSites_Site.GID
     LEFT JOIN ESFISalesPerson AS FK_ESFIItemEntry_ESFISalesPerson
       ON ESFIItemEntry_ESFIItemPeriodics.fSalesPersonGID = FK_ESFIItemEntry_ESFISalesPerson.GID
WHERE

        (ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty <> 0)
        AND ESFIItemEntry_ESFIItemPeriodics.fSiteGID= '86947579-6885-4E86-914E-46378DB3794F'
        AND DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {year}
        AND DATEPART(Month,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {month}
GROUP BY
ESFIItem.fItemSubcategoryCode
--     ESFIZItemFamily.Description
--     ESFIZItemSubfamily.Description
--     ESFIZItemCategory.Description
--     ESFIItem.Description,
--     ESFIItem.BarCode
ORDER BY 2 DESC
        """


def quantity_for_team(year, month):
    return f"""
SELECT 
--     ESFIItem.Description  AS 'ΠΕΡΙΓΡΑΦΗ',
--     ESFIItem.BarCode AS 'ΚΩΔΙΚΟΣ',
--     ESFIZItemFamily.Description as 'ΟΙΚΟΓΕΝΕΙΑ',
    ESFIZItemSubfamily.Description as 'category',
--     ESFIZItemCategory.Description as 'category',
--     ESFIItem.fItemSubcategoryCode as 'category',
    isnull(Sum(ESFIItemEntry_ESFIItemPeriodics.Quantity),0) AS 'QUANTITY'

FROM ESFIItemEntry_ESFIItemPeriodics

     LEFT JOIN ESFIItem
       ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = ESFIItem.GID
     LEFT JOIN ESFIZItemFamily
       ON ESFIItem.fItemFamilyCode = ESFIZItemFamily.Code
     LEFT JOIN ESFIZItemSubfamily
       ON ESFIItem.fItemGroupCode = ESFIZItemSubfamily.Code
     LEFT JOIN ESFIZItemCategory
       ON ESFIItem.fItemCategoryCode = ESFIZItemCategory.Code
     LEFT JOIN ESGOSites AS FK_ESFIItemEntry_ESGOSites_Site
       ON ESFIItemEntry_ESFIItemPeriodics.fSiteGID = FK_ESFIItemEntry_ESGOSites_Site.GID
     LEFT JOIN ESFISalesPerson AS FK_ESFIItemEntry_ESFISalesPerson
       ON ESFIItemEntry_ESFIItemPeriodics.fSalesPersonGID = FK_ESFIItemEntry_ESFISalesPerson.GID
WHERE

        (ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty <> 0)
        AND ESFIItemEntry_ESFIItemPeriodics.fSiteGID= '86947579-6885-4E86-914E-46378DB3794F'
        AND DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {year}
        AND DATEPART(Month,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {month}
GROUP BY
ESFIZItemSubfamily.Description
--     ESFIZItemFamily.Description
--     ESFIZItemSubfamily.Description
--     ESFIZItemCategory.Description
--     ESFIItem.Description,
--     ESFIItem.BarCode
ORDER BY 2 DESC
        """


def randar_query(year, month):
    return f"""
    SELECT TOP 10
       ESFIItem.fItemSubcategoryCode                                                 AS 'BRAND',
       isnull(Sum(ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_TurnOver),0)     AS 'SALES'

FROM ESFIItemEntry_ESFIItemPeriodics

     LEFT JOIN ESFIItem
       ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = ESFIItem.GID

WHERE
         (ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty <> 0)
        AND ESFIItemEntry_ESFIItemPeriodics.fSiteGID= '86947579-6885-4E86-914E-46378DB3794F'
        AND DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {year}
        AND DATEPART(Month,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {month}
GROUP BY
       ESFIItem.fItemSubcategoryCode
ORDER BY 2 DESC
    """


def today_products(year, month, day):
    return f"""
    SELECT TOP 10
       ESFIItem.Description                                                          AS 'Description',
       ESFIItem.BarCode                                                              AS 'BarCode',
       isnull(Sum(ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty),0)     AS 'Quantity',
       isnull(Sum(ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_TurnOver),0)     AS 'SALES'

FROM ESFIItemEntry_ESFIItemPeriodics

     LEFT JOIN ESFIItem
       ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = ESFIItem.GID

WHERE
         (ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty <> 0)
        AND ESFIItemEntry_ESFIItemPeriodics.fSiteGID= '86947579-6885-4E86-914E-46378DB3794F'
        AND DATEPART(year,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {year}
        AND DATEPART(Month,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {month}
        AND DATEPART(Day,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {day}
GROUP BY
       ESFIItem.Description, ESFIItem.BarCode
ORDER BY 3 DESC, 4 DESC
    """


def pda_alert():
    return f"""
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
            
    """


def price_changes_today():
    return f"""
select isnull(count(ESFIItem.Code),0)                                       AS COUNT
FROM ESFIItem
    LEFT JOIN ES00HistoryLogRawData
        ON ESFIItem.GID = ES00HistoryLogRawData.fPK

WHERE
       convert(varchar, ESDModified, 102) = convert(varchar, getdate(), 102)
AND (ES00HistoryLogRawData.TableID = 'ESMMStockItem')
AND (ES00HistoryLogRawData.FieldID = 'RetailPrice')
AND convert(varchar, ES00HistoryLogRawData.HDate, 102) = convert(varchar, getdate(), 102)
    """


def new_products():
    return f"""
    select 
    isnull(count(ESFIItem.Code),0)                                      AS COUNT
FROM ESFIItem
LEFT JOIN ESFIItemEntry_ESFIItemPeriodics
                            ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = ESFIItem.GID
WHERE
       convert(varchar, ESFIItem.ESDCreated, 102) =  convert(varchar, getdate(), 102)
    """


def special_price():
    return f"""
    SELECT
       isnull(count(ESFIItem.Code),0)                                                     AS COUNT
FROM ESFIPricelistItem
         LEFT JOIN ESFIItem
                   on ESFIPricelistItem.fItemGID = ESFIItem.GID
         INNER JOIN ESFIPricelist
                    on ESFIPricelistItem.fPricelistGID = ESFIPricelist.GID
WHERE GETDATE() BETWEEN  ValidFromDate AND ValidToDate
    """


def customer_prefer():
    return f"""
    SELECT
    isnull(count(Distinct ESFIItem.Code),0)                                                                    AS COUNT
FROM ESFIItemEntry_ESFIItemPeriodics
     LEFT JOIN ESFIItem
        ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = ESFIItem.GID
WHERE   ESFIItemEntry_ESFIItemPeriodics.fSiteGID= '86947579-6885-4E86-914E-46378DB3794F'
        AND (ESFIItemEntry_ESFIItemPeriodics.DocumentCode like 'ΑΠΛ%' or ESFIItemEntry_ESFIItemPeriodics.DocumentCode like 'ΤΔΑ%')
        AND convert(varchar, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate, 102) = convert(varchar, getdate(), 102)
    """


def check_online_user(user):
    return f"""
SELECT TOP 1 * from ES00EventLog WHERE
id IN ('ESLOGIN','ESLOGOUT')
AND UserID = '{user}'
ORDER BY EDate DESC
    """