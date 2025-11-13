---
title: print_account_simple
---

# print_account_simple




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | varchar(50) |
| level | int |


## SQL Definition

```sql
CREATE PROCEDURE `print_account_simple`(IN table_name varchar(50), IN level int)
BEGIN
    SET @stmt=CONCAT('SELECT ind,
                                code_of_account,
                                account_description,
                                total_cost,
                                level,
                                review_status
                                FROM ',table_name,' WHERE level <= ?');
        PREPARE stmt FROM @stmt;
        SET @level=level;
        EXECUTE stmt USING @level;
        DEALLOCATE PREPARE stmt;
END;;
