---
title: get_var_value_by_name
---

# get_var_value_by_name




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `get_var_value_by_name`(IN table_name VARCHAR(50))
BEGIN
    SET @stmt = CONCAT('SELECT var_value FROM ', table_name, ' WHERE var_name = ?');
        PREPARE stmt FROM @stmt;
        SET @var_name = var_name;
        EXECUTE stmt USING @var_name;
        DEALLOCATE PREPARE stmt;
END;;
