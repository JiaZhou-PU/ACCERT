---
title: print_user_request_parameter
---

# print_user_request_parameter




## Parameters


| **Name** | **Type** |
|----------|----------|
| all_col | BOOLEAN |
| var_table | VARCHAR(50) |
| cel_table | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `print_user_request_parameter`(IN all_col BOOLEAN, IN var_table VARCHAR(50), IN cel_table VARCHAR(50))
BEGIN
    IF all_col THEN
    		SET @stmt = CONCAT("SELECT va.ind, va.var_name, 
           (SELECT GROUP_CONCAT(ce.cost_element SEPARATOR ', ')
            FROM ", cel_table, " ce
            WHERE FIND_IN_SET(va.var_name, REPLACE(ce.variables, ' ', '')) > 0) AS ce_affected
    		FROM ",var_table," as va
    		WHERE va.var_value IS NULL
    		ORDER BY va.ind;");
        ELSE
            SET @stmt = CONCAT("SELECT va.var_name, 
           (SELECT GROUP_CONCAT(ce.cost_element SEPARATOR ', ')
            FROM ", cel_table, " ce
            WHERE FIND_IN_SET(va.var_name, REPLACE(ce.variables, ' ', '')) > 0) AS ce_affected
    		FROM ",var_table," as va
    		WHERE va.var_value IS NULL
    		ORDER BY va.ind;");
        END IF;
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
