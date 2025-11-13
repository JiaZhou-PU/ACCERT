---
title: roll_up_account_table_by_level
---

# roll_up_account_table_by_level




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | varchar(50) |
| from_level | int |
| to_level | int |


## SQL Definition

```sql
CREATE PROCEDURE `roll_up_account_table_by_level`(IN table_name varchar(50), IN from_level int, IN to_level int)
BEGIN
    SET SQL_SAFE_UPDATES = 0;
        SET @stmt = CONCAT('UPDATE ', table_name, ',',
                        '(SELECT a',to_level,'.code_of_account as ac',to_level,'_coa, ',
                                'sum(ua',from_level,'.total_cost) as a',to_level,'_cal_total_cost ',
                        'FROM ', table_name, ' as ua',from_level,
                        ' JOIN ', table_name, ' as a',to_level,
                        ' on ua',from_level,'.supaccount=a',to_level,'.code_of_account ',
                        'where ua',from_level,'.level=',from_level,
                        ' and a',to_level,'.level=',to_level,
                        ' group by a',to_level,'.code_of_account) as updated_ac',to_level,
                        ' SET ',
                        table_name,'.total_cost = updated_ac',to_level,'.a',to_level,'_cal_total_cost,',
                        table_name,'.review_status = \'Updated\' ',
                        'WHERE ',
                        table_name,'.code_of_account = updated_ac',to_level,'.ac',to_level,'_coa');
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
