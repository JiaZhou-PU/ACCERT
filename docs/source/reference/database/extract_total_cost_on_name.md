---
title: extract_total_cost_on_name
---

# extract_total_cost_on_name




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(50) |
| tc_name | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `extract_total_cost_on_name`(IN table_name VARCHAR(50), IN tc_name VARCHAR(50))
BEGIN
    SET @stmt = CONCAT('SELECT code_of_account, account_description, total_cost
                            FROM ', table_name, ' WHERE code_of_account = ?');
    PREPARE stmt FROM @stmt;
    SET @tc_name = tc_name;
    EXECUTE stmt USING @tc_name;
    DEALLOCATE PREPARE stmt;
END;;
