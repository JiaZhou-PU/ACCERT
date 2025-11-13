---
title: insert_new_COA
---

# insert_new_COA




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(50) |
| ind | INT |
| supaccount | VARCHAR(50) |
| level | INT |
| code_of_account | VARCHAR(50) |
| account_description | VARCHAR(50) |
| total_cost | INT |
| review_status | VARCHAR(50) |
| prn | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `insert_new_COA`(IN table_name VARCHAR(50), IN ind INT, IN supaccount VARCHAR(50), IN level INT, IN code_of_account VARCHAR(50), IN account_description VARCHAR(50), IN total_cost INT, IN review_status VARCHAR(50), IN prn VARCHAR(50))
BEGIN
    SET @stmt = CONCAT('INSERT INTO ', table_name,
    						' (ind, supaccount, level, code_of_account, account_description, 
    							total_cost, review_status, prn) 
    							VALUES (?, ?, ?, ?, ?, ?, ?, ?)');
    PREPARE stmt FROM @stmt;
    SET @ind = ind;
    SET @supaccount = supaccount;
    SET @level = level;
    SET @code_of_account = code_of_account;
    SET @account_description = account_description;
    SET @total_cost = total_cost;
    SET @review_status = review_status;
    SET @prn = prn;


    EXECUTE stmt USING @ind, @supaccount, @level, @code_of_account, @account_description,
    @total_cost, @review_status, @prn;
    DEALLOCATE PREPARE stmt;
END;;
