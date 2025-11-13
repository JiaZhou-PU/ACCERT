---
title: update_cost_element_on_name
---

# update_cost_element_on_name




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `update_cost_element_on_name`(IN table_name VARCHAR(50))
BEGIN
    SET SQL_SAFE_UPDATES = 0;

        SET @stmt = CONCAT('UPDATE ', table_name, 
                           ' SET cost_2017 = ', alg_value, 
                           ', updated = 1 WHERE cost_element = ''', ce_name, '''');
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
