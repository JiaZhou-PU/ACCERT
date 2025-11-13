---
title: sum_up_lmt_direct_cost
---

# sum_up_lmt_direct_cost




## Parameters


| **Name** | **Type** |
|----------|----------|
| acc_tabl_name | varchar(50) |


## SQL Definition

```sql
CREATE PROCEDURE `sum_up_lmt_direct_cost`(IN acc_tabl_name varchar(50))
BEGIN
    SET @stmt = CONCAT('UPDATE ', acc_tabl_name, ',',
                            '(SELECT  (total_cost/prn) as talcost
                                FROM ', acc_tabl_name, ' as pre_acc
                                WHERE pre_acc.code_of_account =\'2C\') as calcost
                            SET ', acc_tabl_name, '.total_cost = calcost.talcost,
                            review_status = \'Ready for Review\'
                            WHERE ', acc_tabl_name, '.code_of_account = \'2\';');
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
