---
title: update_super_variable
---

# update_super_variable




## Parameters


| **Name** | **Type** |
|----------|----------|
| var_table_name | VARCHAR(50) |
| alg_table_name | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `update_super_variable`(IN var_table_name VARCHAR(50), IN alg_table_name VARCHAR(50))
BEGIN
    SET @stmt = CONCAT('SELECT var.ind, var.var_name, var.var_value,
                            var.var_alg, var.var_need, alg.ind, alg.alg_python,
                            alg.alg_formulation, alg.alg_units, var.var_unit
                            FROM ', var_table_name, ' as var JOIN ', alg_table_name, ' as alg
                            ON var.var_alg=alg.alg_name
                            WHERE var.var_name=?');
    PREPARE stmt FROM @stmt;
    SET @var_name = u_i_var_name;
    EXECUTE stmt USING @var_name;
    DEALLOCATE PREPARE stmt;
END;;
