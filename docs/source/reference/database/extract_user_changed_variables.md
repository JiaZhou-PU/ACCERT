---
title: extract_user_changed_variables
---

# extract_user_changed_variables




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `extract_user_changed_variables`(IN table_name VARCHAR(50))
BEGIN
    SET @stmt = CONCAT('SELECT var_name,var_description, var_value, var_unit
                            FROM ', table_name, ' WHERE user_input = 1 ORDER BY var_name;');
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
