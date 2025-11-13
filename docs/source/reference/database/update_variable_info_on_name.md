---
title: update_variable_info_on_name
---

# update_variable_info_on_name




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `update_variable_info_on_name`(IN table_name VARCHAR(50))
BEGIN
    SET SQL_SAFE_UPDATES = 0;
        SET @stmt = CONCAT('UPDATE ', table_name, ' SET var_value = ?,
                            var_unit = ?,
                            user_input = ? WHERE var_name = ?');
    PREPARE stmt FROM @stmt;
    SET @var_value = value;
    SET @var_unit = unit;
    SET @user_input = 1;
    SET @var_name = u_i_var_name;
    EXECUTE stmt USING @var_value, @var_unit, @user_input, @var_name;
    DEALLOCATE PREPARE stmt;
END;;
