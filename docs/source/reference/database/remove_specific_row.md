---
title: remove_specific_row
---

# remove_specific_row




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | VARCHAR(50) |
| target_code | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `remove_specific_row`(IN table_name VARCHAR(50), IN target_code VARCHAR(50))
BEGIN
    SET SQL_SAFE_UPDATES = 0;

        SET @stmt = CONCAT(
            'DELETE FROM ', table_name,
            ' WHERE code_of_account = \'', target_code, '\''
        );

        -- Debug: Print the constructed SQL statement
        SELECT @stmt;

        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
