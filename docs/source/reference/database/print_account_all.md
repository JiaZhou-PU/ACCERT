---
title: print_account_all
---

# print_account_all




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | varchar(50) |
| level | int |


## SQL Definition

```sql
CREATE PROCEDURE `print_account_all`(IN table_name varchar(50), IN level int)
BEGIN
    SET @stmt=CONCAT('SELECT * FROM ',table_name,' WHERE level <= ?');
        PREPARE stmt FROM @stmt;
        SET @level=level;
        EXECUTE stmt USING @level;
        DEALLOCATE PREPARE stmt;
END;;
