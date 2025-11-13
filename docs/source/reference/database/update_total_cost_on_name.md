---
title: update_total_cost_on_name
---

# update_total_cost_on_name




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `update_total_cost_on_name`(IN table_name VARCHAR(50))
BEGIN
    SET SQL_SAFE_UPDATES = 0;
        SET @stmt = CONCAT('UPDATE ', table_name, ' SET total_cost = ?, 
                                                  review_status = "User Input" WHERE code_of_account = ?');
        PREPARE stmt FROM @stmt;
        SET @tc_id = tc_id;
        SET @u_i_tc_value = u_i_tc_value;
        EXECUTE stmt USING @u_i_tc_value, @tc_id;
        DEALLOCATE PREPARE stmt;
END;;
