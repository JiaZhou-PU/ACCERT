---
title: cal_direct_cost_elements
---

# cal_direct_cost_elements




## Parameters


| **Name** | **Type** |
|----------|----------|
| acc_table | VARCHAR(50) |
| cel_table | varchar(50) |


## SQL Definition

```sql
CREATE PROCEDURE `cal_direct_cost_elements`(IN acc_table VARCHAR(50), IN cel_table varchar(50))
BEGIN
    DECLARE tprn DECIMAL(18,6);

        -- Calculate tprn (sum of 'prn' in the account table)
        SET @query = CONCAT('SELECT SUM(t1.prn) INTO @tprn
                             FROM ', acc_table, ' AS t1
                             LEFT JOIN ', acc_table, ' AS t2
                             ON t1.code_of_account = t2.supaccount
                             WHERE t2.code_of_account IS NULL
                             AND t1.code_of_account != ''2''
                             AND t1.code_of_account != ''2C'';');
        PREPARE stmt FROM @query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        -- Get the calculated tprn value
        SET tprn = @tprn;

        -- Select the calculated 'fac', 'lab', and 'mat' values
        SET @query = CONCAT('SELECT cost_2017 / ', tprn, ' AS fac FROM ', cel_table, '
                            WHERE account = ''2'' AND cost_element = ''2c_fac'';');
        PREPARE stmt FROM @query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        SET @query = CONCAT('SELECT cost_2017 / ', tprn, ' AS lab FROM ', cel_table, '
                            WHERE account = ''2'' AND cost_element = ''2c_lab'';');
        PREPARE stmt FROM @query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        SET @query = CONCAT('SELECT cost_2017 / ', tprn, ' AS mat FROM ', cel_table, '
                            WHERE account = ''2'' AND cost_element = ''2c_mat'';');
        PREPARE stmt FROM @query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        SET @query = CONCAT('SELECT 
            (SELECT cost_2017 / ', tprn, ' FROM ', cel_table, ' WHERE account = ''2'' AND cost_element = ''2c_fac'') AS fac,
            (SELECT cost_2017 / ', tprn, ' FROM ', cel_table, ' WHERE account = ''2'' AND cost_element = ''2c_lab'') AS lab,
            (SELECT cost_2017 / ', tprn, ' FROM ', cel_table, ' WHERE account = ''2'' AND cost_element = ''2c_mat'') AS mat;');

        PREPARE stmt FROM @query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
