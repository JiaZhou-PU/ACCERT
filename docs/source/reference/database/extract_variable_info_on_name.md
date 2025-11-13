---
title: extract_variable_info_on_name
---

# extract_variable_info_on_name




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(50) |
| var_name | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `extract_variable_info_on_name`(IN table_name VARCHAR(50), IN var_name VARCHAR(50))
BEGIN
    SET @stmt = CONCAT('SELECT var_value, var_unit FROM ', table_name, ' WHERE var_name = ?');
    PREPARE stmt FROM @stmt;
    SET @var_name = var_name;
    EXECUTE stmt USING @var_name;
    DEALLOCATE PREPARE stmt;
END;;
