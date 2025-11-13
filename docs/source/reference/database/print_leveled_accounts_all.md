---
title: print_leveled_accounts_all
---

# print_leveled_accounts_all




## Parameters


| **Name** | **Type** |
|----------|----------|
| acc_table | varchar(50) |
| cel_table | varchar(50) |
| level | int |


## SQL Definition

```sql
CREATE PROCEDURE `print_leveled_accounts_all`(IN acc_table varchar(50), IN cel_table varchar(50), IN level int)
BEGIN
    SET @stmt=CONCAT('SELECT acc.level,
                                rankedcoa.code_of_account as code_of_account,
                                acc.account_description,
                                sorted_ce.fac_cost,
                                sorted_ce.lab_cost,
                                sorted_ce.mat_cost,
                                acc.total_cost,
                                acc.review_status
                                FROM ',acc_table,' as acc
                                JOIN
                                (SELECT node.code_of_account AS COA , 
    								CONCAT( REPEAT(" ", node.level), node.code_of_account) AS code_of_account
    								FROM ',acc_table,' AS node
    								ORDER BY node.ind) as rankedcoa
                                    ON acc.code_of_account=rankedcoa.COA
                                    JOIN (SELECT splt_act.code_of_account,
    											   cef.cost_2017 AS fac_cost,
    											   cel.cost_2017 AS lab_cost,
    											   cem.cost_2017 AS mat_cost
    										FROM 
    											(SELECT code_of_account, 
    													CONCAT(code_of_account, "_fac") AS fac_name,
    													CONCAT(code_of_account, "_lab") AS lab_name,
    													CONCAT(code_of_account, "_mat") AS mat_name
    											 FROM ',acc_table,') AS splt_act
    										LEFT JOIN ',cel_table,' AS cef
    											ON cef.cost_element = splt_act.fac_name
    										LEFT JOIN ',cel_table,' AS cel
    											ON cel.cost_element = splt_act.lab_name
    										LEFT JOIN ',cel_table,' AS cem
    											ON cem.cost_element = splt_act.mat_name) as sorted_ce
                                        ON sorted_ce.code_of_account=acc.code_of_account
                                        WHERE acc.level <= ?
                                        ORDER BY acc.ind;');
        PREPARE stmt FROM @stmt;
        SET @level=level;
        EXECUTE stmt USING @level;
        DEALLOCATE PREPARE stmt;
END;;
