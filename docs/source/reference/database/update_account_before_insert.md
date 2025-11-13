---
title: update_account_before_insert
---

# update_account_before_insert




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(50) |
| min_ind | INT |


## SQL Definition

```sql
CREATE PROCEDURE `update_account_before_insert`(IN table_name VARCHAR(50), IN min_ind INT)
BEGIN
    SET SQL_SAFE_UPDATES = 0;
        SET @stmt = CONCAT('UPDATE ', table_name,
                           ' SET ind = ind + 1 WHERE ind >?');
        PREPARE stmt FROM @stmt;
        SET @min_ind = min_ind;
        EXECUTE stmt USING @min_ind;
        DEALLOCATE PREPARE stmt;
END;;
