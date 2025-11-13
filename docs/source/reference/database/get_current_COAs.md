---
title: get_current_COAs
---

# get_current_COAs




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(50) |
| inp_id | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `get_current_COAs`(IN table_name VARCHAR(50), IN inp_id VARCHAR(50))
BEGIN
    SET @stmt = CONCAT('SELECT code_of_account, 
                           ind FROM ', table_name, ' WHERE supaccount = ?');
        PREPARE stmt FROM @stmt;
        SET @inp_id = inp_id;
        EXECUTE stmt USING @inp_id;
        DEALLOCATE PREPARE stmt;
END;;
