# Wallpaper Project

## Overview
The `Wallpaper` project is designed to manage and interact with SQL data structures efficiently. It comprises SQL scripts and Python modules for database connectivity, data fetching, and analysis of sales and inventory-related information.

## Directory Structure

### **SQL_FOLDER**
This directory contains Python and SQL scripts responsible for interacting with the database. Below is a brief overview of the files:

#### Python Scripts
1. **`sql_connect.py`**  
   A Python script for establishing a connection to the database. It handles configuration details, including database host, credentials, and connection pooling.

2. **`fetch_data.py`**  
   A utility script to fetch and process data from the connected database. Queries can be dynamically run through this module.

#### SQL Scripts
1. **`ESFIPricelistItem_a.sql`**  
   SQL script for handling and analyzing price list items stored in the database. Useful for pricing-related data extraction.

2. **`ESFIItemEntry_ESFIItemPeriodics_a.sql`**  
3. **`ESFIItemEntry_ESFIItemPeriodics_b.sql`**  
4. **`ESFIItemEntry_ESFIItemPeriodics_c.sql`**  
5. **`ESFIItemEntry_ESFIItemPeriodics_d.sql`**  
   A group of SQL scripts (`a-d`) designed to process periodic data entries related to items (`ESFIItemEntry`). This includes item quantities, movements, and other related statistics.

6. **`ESFIItem_a.sql`**  
   The foundational SQL script for processing and querying item-level information. Covers base operations for managing database entities related to items.

7. **`ESFIDocumentTrade_a.sql`**  
8. **`ESFIDocumentTrade_b.sql`**  
   Scripts that handle trade document information. These scripts include queries that are likely focused on invoices, purchase orders, or sales transactions.

9. **`IMP_MobileDocumentLines_a.sql`**  
   A query for analyzing and summarizing mobile document lines, focusing on transaction types (e.g., purchases, returns, transfers). It provides aggregated data for document headers, line counts, and order types.

## Examples of Queries
Below is an example of a query used in the project:

```sql
SELECT count(distinct IMP_MobileDocumentHeaders.Code) AS DOCS,
       count(IMP_MobileDocumentLines.BarCode) AS LINES,
       CASE
           WHEN OrderType in ('ΑΤΔ', 'ΑΔΠ', 'ΑΧΔ') THEN 'ΑΓΟΡΕΣ'
           WHEN OrderType = 'ΔΕΑ' THEN 'ΕΠΙΣΤΡΟΦΕΣ'
           WHEN OrderType = 'ΔΕΝ' THEN 'ΕΝΔΟΔΙΑΚΙΝΗΣΕΙΣ'
           WHEN OrderType = 'ΠΠΡ' THEN 'ΠΑΡΑΓΓΕΛΙΕΣ'
           WHEN OrderType = 'ΑΠ_ΜΟΒ' THEN 'ΡΑΦΙ ΤΙΜΕΣ'
           ELSE 'ΛΟΙΠΑ'
       END AS 'TYPE'
FROM IMP_MobileDocumentLines
LEFT JOIN IMP_MobileDocumentHeaders
    ON IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
LEFT JOIN ESFITradeAccount
    ON ESFITradeAccount.gid = IMP_MobileDocumentHeaders.Supplier
WHERE CONVERT(VARCHAR, RealImportTime, 102) = CONVERT(VARCHAR, GETDATE(), 102)
GROUP BY
       CASE
           WHEN OrderType in ('ΑΤΔ', 'ΑΔΠ', 'ΑΧΔ') THEN 'ΑΓΟΡΕΣ'
           WHEN OrderType = 'ΔΕΑ' THEN 'ΕΠΙΣΤΡΟΦΕΣ'
           WHEN OrderType = 'ΔΕΝ' THEN 'ΕΝΔΟΔΙΑΚΙΝΗΣΕΙΣ'
           WHEN OrderType = 'ΠΠΡ' THEN 'ΠΑΡΑΓΓΕΛΙΕΣ'
           WHEN OrderType = 'ΑΠ_ΜΟΒ' THEN 'ΡΑΦΙ ΤΙΜΕΣ'
           ELSE 'ΛΟΙΠΑ'
       END
```

This query aggregates and categorizes transaction lines based on order types (e.g., purchases, returns, transfers).

## How to Use
1. **Database Connection**  
   - Configure the `sql_connect.py` script with your database credentials.
   - Use this module as a utility to connect the SQL scripts to Python functionality.

2. **Running Queries**  
   - SQL queries present in the `.sql` files can be executed via your preferred SQL client or integrated through the `fetch_data.py` script.

3. **Analysis**  
   - The SQL scripts can be modified further to cater to specific analysis needs like sales projections, demand forecasting, and inventory management.

## Requirements
- Python 3.9+
- Required Python Packages:
  - `pymssql` or appropriate DB libraries
  - `pandas` for data processing (optional)

## Contributing
If you'd like to contribute to this project, feel free to fork the repository, make your changes, and create a pull request. Suggestions and feedback are always welcome!

## License
This project is licensed under the terms of the copyright notice included in each file:
```txt
Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved.
```

---
