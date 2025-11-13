---
title: extract_affected_cost_elements_w_dis
---

# extract_affected_cost_elements_w_dis




## Parameters


| **Name** | **Type** |
|----------|----------|
| cel_table | varchar(50) |
| var_table | varchar(50) |


## SQL Definition

```sql
CREATE PROCEDURE `extract_affected_cost_elements_w_dis`(IN cel_table varchar(50), IN var_table varchar(50))
BEGIN
    SET @stmt = CONCAT("SELECT va.var_name,va.var_description, (SELECT GROUP_CONCAT(ce.cost_element SEPARATOR ', ')
            FROM ", cel_table, " ce
            WHERE FIND_IN_SET(va.var_name, REPLACE(ce.variables, ' ', '')) > 0) AS ce_affected
                            FROM
                            (SELECT * FROM ",var_table,"
                            WHERE user_input = 1) as va
                            WHERE (SELECT GROUP_CONCAT(ce.cost_element SEPARATOR ', ')
    								FROM cost_element ce
    						WHERE FIND_IN_SET(va.var_name, REPLACE(ce.variables, ' ', '')) > 0) IS NOT NULL
                            ");
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
