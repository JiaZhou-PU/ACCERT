---
title: update_new_cost_elements
---

# update_new_cost_elements




## Parameters


| **Name** | **Type** |
|----------|----------|
| cel_tabl_name | VARCHAR(50) |
| var_tabl_name | VARCHAR(50) |
| alg_tabl_name | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `update_new_cost_elements`(IN cel_tabl_name VARCHAR(50), IN var_tabl_name VARCHAR(50), IN alg_tabl_name VARCHAR(50))
BEGIN
    SET SQL_SAFE_UPDATES = 0;
        SET @stmt = CONCAT("SELECT ce.ind, ce.cost_element,
           ce.cost_2017, ce.alg_name,
           ce.variables, ce.algno,
           alg.alg_python, alg.alg_formulation, alg.alg_units 
    		FROM ", cel_tabl_name, " AS ce 
    		JOIN ", alg_tabl_name, " AS alg ON ce.alg_name = alg.alg_name
    		WHERE EXISTS (
    			SELECT 1
    			FROM ", var_tabl_name, " AS va
    			WHERE va.user_input = 1
    			AND FIND_IN_SET(va.var_name, REPLACE(ce.variables, ' ', '')) > 0);");
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
