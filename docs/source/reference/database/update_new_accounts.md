---
title: update_new_accounts
---

# update_new_accounts




## Parameters


| **Name** | **Type** |
|----------|----------|
| acc_tabl_name | VARCHAR(50) |
| var_tabl_name | VARCHAR(50) |
| alg_tabl_name | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `update_new_accounts`(IN acc_tabl_name VARCHAR(50), IN var_tabl_name VARCHAR(50), IN alg_tabl_name VARCHAR(50))
BEGIN
    SET SQL_SAFE_UPDATES = 0;
        SET @stmt = CONCAT("SELECT ac.ind, ac.code_of_account,
           ac.total_cost, ac.alg_name,
           ac.variables, 
           alg.alg_python, alg.alg_formulation, alg.alg_units 
    		FROM ", acc_tabl_name, " AS ac 
    		JOIN ", alg_tabl_name, " AS alg ON ac.alg_name = alg.alg_name
    		WHERE EXISTS (
    			SELECT 1
    			FROM ", var_tabl_name, " AS va
    			WHERE va.user_input = 1
    			AND FIND_IN_SET(va.var_name, REPLACE(ac.variables, ' ', '')) > 0);");
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
