---
title: print_leveled_accounts_simple
---

# print_leveled_accounts_simple




## Parameters


| **Name** | **Type** |
|----------|----------|
| acc_table | VARCHAR(255) |
| level | INT |


## SQL Definition

```sql
CREATE PROCEDURE `print_leveled_accounts_simple`(IN acc_table VARCHAR(255), IN level INT)
BEGIN
    SET @stmt = CONCAT('SELECT rankedcoa.code_of_account,
                        acc.account_description,
                        acc.total_cost,
                        acc.level,
                        acc.review_status
                        FROM ',acc_table,' as acc
                        JOIN
                        (SELECT node.code_of_account AS COA , 
                        CONCAT( REPEAT(" ", node.level), node.code_of_account) AS code_of_account
                        FROM ',acc_table,' AS node
                        ORDER BY node.ind) as rankedcoa
                        ON acc.code_of_account=rankedcoa.COA
                        WHERE acc.level <= ?
                        ORDER BY acc.ind;');
        PREPARE stmt FROM @stmt;
        SET @level=level;
        EXECUTE stmt USING @level;
        DEALLOCATE PREPARE stmt;
END;;
