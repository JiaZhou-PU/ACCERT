---
title: print_leveled_accounts_gn
---

# print_leveled_accounts_gn




## Parameters


| **Name** | **Type** |
|----------|----------|
| acc_table | VARCHAR(255) |
| map_table | VARCHAR(255) |
| level | INT |


## SQL Definition

```sql
CREATE PROCEDURE `print_leveled_accounts_gn`(IN acc_table VARCHAR(255), IN map_table VARCHAR(255), IN level INT)
BEGIN
    SET @stmt = CONCAT(
            'SELECT rankedcoa.gncoa,
    				map.gncoa_description,
                    acc.total_cost,
                    acc.gn_level,
                    acc.review_status
             FROM ', acc_table, ' AS acc
             JOIN 
             (
                 SELECT node.gncoa AS COA, 
                        CONCAT(REPEAT(" ", node.gn_level), node.gncoa) AS gncoa
                 FROM ', acc_table, ' AS node
                 ORDER BY node.gn_ind
             ) AS rankedcoa
             ON acc.gncoa = rankedcoa.COA
             JOIN ',map_table,' as map
             ON acc.gncoa = map.gncoa
             WHERE acc.gn_level <= ?
             ORDER BY acc.gn_ind;'
        );

        PREPARE stmt FROM @stmt;
        SET @level = level;
        EXECUTE stmt USING @level;
        DEALLOCATE PREPARE stmt;
END;;
