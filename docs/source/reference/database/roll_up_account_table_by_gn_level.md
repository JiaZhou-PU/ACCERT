---
title: roll_up_account_table_by_gn_level
---

# roll_up_account_table_by_gn_level




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(50) |
| from_level | INT |
| to_level | INT |


## SQL Definition

```sql
CREATE PROCEDURE `roll_up_account_table_by_gn_level`(IN table_name VARCHAR(50), IN from_level INT, IN to_level INT)
BEGIN
    SET SQL_SAFE_UPDATES = 0;

        SET @stmt = CONCAT(
            'UPDATE ', table_name, ',',
            '(SELECT a', to_level, '.gncoa AS ac', to_level, '_coa, ',
                    'SUM(ua', from_level, '.total_cost) AS a', to_level, '_cal_total_cost ',
            'FROM ', table_name, ' AS ua', from_level,
            ' JOIN ', table_name, ' AS a', to_level,
            ' ON ua', from_level, '.gn_supaccount = a', to_level, '.gncoa ',
            'WHERE ua', from_level, '.gn_level = ', from_level,
            ' AND a', to_level, '.gn_level = ', to_level,
            ' GROUP BY a', to_level, '.gncoa) AS updated_ac', to_level,
            ' SET ',
            table_name, '.total_cost = updated_ac', to_level, '.a', to_level, '_cal_total_cost, ',
            table_name, '.review_status = \'Updated\' ',
            'WHERE ',
            table_name, '.gncoa = updated_ac', to_level, '.ac', to_level, '_coa'
        );

        -- Debug: Print the constructed SQL statement
        SELECT @stmt;

        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
