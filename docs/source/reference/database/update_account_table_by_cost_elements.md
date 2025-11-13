---
title: update_account_table_by_cost_elements
---

# update_account_table_by_cost_elements




## Parameters


| **Name** | **Type** |
|----------|----------|
| acc_tabl_name | varchar(50) |
| cel_tabl_name | varchar(50) |


## SQL Definition

```sql
CREATE PROCEDURE `update_account_table_by_cost_elements`(IN acc_tabl_name varchar(50), IN cel_tabl_name varchar(50))
BEGIN
    SET SQL_SAFE_UPDATES = 0;
    	SET @stmt = CONCAT('UPDATE ', acc_tabl_name, ',',
    						'(SELECT ', acc_tabl_name, '.code_of_account,
    								ce.total_cost as cost,
    								ce.updated as updated
    						FROM ', acc_tabl_name, '
    						JOIN (SELECT account,
    									sum(cost_2017) as total_cost,
    									sum(updated) as updated
    							FROM ', cel_tabl_name, '
    							GROUP BY ', cel_tabl_name, '.account ) as ce
    						on ', acc_tabl_name, '.code_of_account = ce.account
    						ORDER BY ', acc_tabl_name, '.ind) as updated_account
    						SET ', acc_tabl_name, '.total_cost = updated_account.cost,
    						review_status = \'Ready for Review\'
    						WHERE updated_account.updated > 0
    						and ', acc_tabl_name, '.code_of_account = updated_account.code_of_account;');
    	PREPARE stmt FROM @stmt;
    	EXECUTE stmt;
    	DEALLOCATE PREPARE stmt;
END;;
