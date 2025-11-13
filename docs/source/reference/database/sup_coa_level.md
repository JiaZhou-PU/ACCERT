---
title: sup_coa_level
---

# sup_coa_level




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(50) |
| supaccount | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `sup_coa_level`(IN table_name VARCHAR(50), IN supaccount VARCHAR(50))
BEGIN
    SET @stmt = CONCAT('SELECT level FROM ', table_name, ' WHERE code_of_account = ?');
    PREPARE stmt FROM @stmt;
    SET @supaccount = supaccount;
    EXECUTE stmt USING @supaccount;
    DEALLOCATE PREPARE stmt;
END;;
