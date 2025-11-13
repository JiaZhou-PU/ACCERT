---
title: sum_cost_elements_2C_mat
---

# sum_cost_elements_2C_mat




## Parameters


| **Name** | **Type** |
|----------|----------|
| cel_tabl_name | varchar(50) |
| acc_tabl_name | varchar(50) |


## SQL Definition

```sql
CREATE PROCEDURE `sum_cost_elements_2C_mat`(IN cel_tabl_name varchar(50), IN acc_tabl_name varchar(50))
BEGIN
    SET @stmt = CONCAT('SELECT sum(cef.cost_2017) from
                            (SELECT t1.code_of_account,
                            CONCAT(t1.code_of_account,\'_mat\') as mat_name
                            FROM ', acc_tabl_name, ' AS t1
                            LEFT JOIN ', acc_tabl_name, ' as t2
                            ON t1.code_of_account = t2.supaccount
                            WHERE t2.code_of_account IS NULL
                            and t1.code_of_account!=\'2\'
                            and t1.code_of_account!=\'2C\' )as ac
                            join ', cel_tabl_name, ' as cef
                                    on cef.cost_element = ac.mat_name
                                    where ac.code_of_account!=\'2C\'');
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
