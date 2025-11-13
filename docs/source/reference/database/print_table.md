---
title: print_table
---

# print_table




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(255) |


## SQL Definition

```sql
CREATE PROCEDURE `print_table`(IN table_name VARCHAR(255))
BEGIN
    SET @stmt = CONCAT('SELECT * FROM ',table_name);
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
