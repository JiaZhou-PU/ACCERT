---
title: extract_affected_accounts
---

# extract_affected_accounts




## Parameters


| **Name** | **Type** |
|----------|----------|
| acc_table | VARCHAR(50) |
| var_table | VARCHAR(50) |


## SQL Definition

```sql
CREATE PROCEDURE `extract_affected_accounts`(IN acc_table VARCHAR(50), IN var_table VARCHAR(50))
BEGIN
    SET @stmt = CONCAT("SELECT va.var_name, (SELECT GROUP_CONCAT(ac.code_of_account SEPARATOR ', ')
            FROM ", acc_table, " ac
            WHERE FIND_IN_SET(va.var_name, REPLACE(ac.variables, ' ', '')) > 0) AS ac_affected
                            FROM
                            (SELECT * FROM ",var_table,"
                            WHERE user_input = 1) as va
                            WHERE (SELECT GROUP_CONCAT(ac.code_of_account SEPARATOR ', ')
    								FROM ", acc_table, " ac
    						WHERE FIND_IN_SET(va.var_name, REPLACE(ac.variables, ' ', '')) > 0) IS NOT NULL
                            ");
    	PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
