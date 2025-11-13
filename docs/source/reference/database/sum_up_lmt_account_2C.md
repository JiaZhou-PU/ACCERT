---
title: sum_up_lmt_account_2C
---

# sum_up_lmt_account_2C




## Parameters


| **Name** | **Type** |
|----------|----------|
| acc_tabl_name | varchar(50) |


## SQL Definition

```sql
CREATE PROCEDURE `sum_up_lmt_account_2C`(IN acc_tabl_name varchar(50))
BEGIN
    SET @stmt = CONCAT('UPDATE ', acc_tabl_name, ',',
                            '(SELECT sum(t1.total_cost) as tc, sum(t1.prn) as tprn FROM
                                ', acc_tabl_name, ' AS t1 LEFT JOIN ', acc_tabl_name, ' as t2
                                ON t1.code_of_account = t2.supaccount
                                WHERE t2.code_of_account IS NULL
                                and t1.code_of_account!=\'2\'
                                and t1.code_of_account!=\'2C\') as dircost
                            SET ', acc_tabl_name, '.total_cost = dircost.tc,
                            ', acc_tabl_name, '.prn=dircost.tprn,
                            review_status = \'Ready for Review\'
                            WHERE ', acc_tabl_name, '.code_of_account = \'2C\';');
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
