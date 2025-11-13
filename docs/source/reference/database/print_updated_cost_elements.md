---
title: print_updated_cost_elements
---

# print_updated_cost_elements




## Parameters


| **Name** | **Type** |
|----------|----------|
| cel_table | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `print_updated_cost_elements`(IN cel_table VARCHAR(50))
BEGIN
    SET @stmt = CONCAT('SELECT ind,
                                    cost_element,
                                    cost_2017,    
                                    sup_cost_ele,
                                    account,
                                    updated
                            FROM ',cel_table,'
                            WHERE updated = 1');
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
