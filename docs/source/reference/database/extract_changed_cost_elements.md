---
title: extract_changed_cost_elements
---

# extract_changed_cost_elements




## Parameters


| **Name** | **Type** |
|----------|----------|
| cel_table | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `extract_changed_cost_elements`(IN cel_table VARCHAR(50))
BEGIN
    SET @stmt = CONCAT('SELECT cost_element, cost_2017
                            FROM ',cel_table,'
                            WHERE updated != 0
                            ORDER BY account, cost_element;');
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
