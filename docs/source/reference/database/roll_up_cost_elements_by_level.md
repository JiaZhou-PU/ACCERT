---
title: roll_up_cost_elements_by_level
---

# roll_up_cost_elements_by_level




## Parameters


| **Name** | **Type** |
|----------|----------|
| table_name | varchar(50) |
| from_level | int |
| to_level | int |


## SQL Definition

```sql
CREATE PROCEDURE `roll_up_cost_elements_by_level`(IN table_name varchar(50), IN from_level int, IN to_level int)
BEGIN
    SET @stmt = CONCAT('UPDATE ', table_name, ',',
                            '(SELECT c',to_level,'.cost_element as ce',to_level,'_ce, ',
                                'sum(uc',from_level,'.cost_2017) as c',to_level,'_cal_total_cost ',
                            'FROM ', table_name, ' as uc',from_level,
                            ' JOIN ', table_name, ' as c',to_level,
                            ' on uc',from_level,'.sup_cost_ele=c',to_level,'.cost_element ',
                            'join account as ac',to_level,
                            ' on c',to_level,'.account = ac',to_level,'.code_of_account ',
                            'where ac',to_level,'.level=',to_level,
                            ' group by c',to_level,'.cost_element) as updated_ce',to_level,
                            ' SET ',
                            table_name,'.cost_2017 = updated_ce',to_level,'.c',to_level,'_cal_total_cost,',
                            table_name,'.updated = 1 ',
                            'WHERE ',
                            table_name,'.cost_element = updated_ce',to_level,'.ce',to_level,'_ce');
        PREPARE stmt FROM @stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
END;;
