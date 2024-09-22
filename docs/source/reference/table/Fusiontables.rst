
Fusion Tables
===================================
The Fusion model is a cost model that estimates the cost of TETRA (Tokamak Engineering Test Reactor Analysis) which is a large tokamak fusion reactor basd on UKAEA's `PROCESS <https://github.com/ukaea/PROCESS>`_

The model contains three main tables: `account`,`algorithm` and `variable`. The account table contains the main cost estimation for Fusion model. The variable table contains the variable information for the Fusion model. While the algorithm table contains the algorithm information for the Fusion model. Each table is associated with a unique identifier, which is used to track and categorize costs. The tables are connected to each other through the different columns.


Fusion account Table
---------------------

This table contains the account information for the Fusion model. Each entity in the account table is associated with a unique identifier, which is used to track and categorize costs. The table is organized into multiple levels, with each level representing a different component or subtask.

The table includes the following columns:

   - **ind**: unique identifier for each account
   - **code_of_account**: code of account 
   - **account_description**: description of the account
   - **total_cost**: total cost of the account unit in dollars
   - **level**: level of the account
   - **supaccount**: superior account
   - **review_status**: review status of the account, note that the default value should always be `Unchanged`
   - **prn**: percentage of the account cost in the total direct cost
   - **alg_name**: algorithm name to calculate the cost of the account
   - **fun_unit**: algorithm function output unit
   - **variables**: variables used in the algorithm

.. csv-table:: [Insert Table Title]
   :header-rows: 1
   :file: ../../../../tutorial/ref_tables/fusion_acc.csv
   :widths: auto
   :class: wide-table

Fusion algorithm Table
--------------------------
this table contains the algorithm information for the Fusion model. Each algorithm is associated with a unique identifier, which is used to track and categorize costs. The table is connected to the account table through the `account` column, which links each algorithm to a specific account. It is also connected to the variable table through the `variables` column.

The table includes the following columns:

   - **ind**: unique identifier for each algorithm
   - **alg_name**: algorithm name
   - **alg_for**: algorithm for a cost element or a variable, `c` for cost  and `v` for variable
   - **alg_description**: description of the algorithm
   - **alg_python**: python file name in the Algorithm folder
   - **alg_formulation**: formulation of the algorithm
   - **alg_units**: unit of the algorithm output

.. csv-table:: [Insert Table Title]
   :header-rows: 1
   :file: ../../../../tutorial/ref_tables/fusion_alg.csv
   :widths: auto
   :class: wide-table

Fusion variable Table
----------------------

This table contains the variable information for the Fusion model. All variables are needed to calculate the cost of the cost in account table or a super variable. Some variables are connected to the algorithm table through the `var_alg` column, which links each variable to a specific algorithm. The table is also connected to itself through the `v_linked` and `var_needed` column, which links each variable to a superior variable and the variables needed to calculate it.

The table includes the following columns:

   - **ind**: unique identifier for each variable
   - **var_name**: variable name
   - **var_description**: description of the variable
   - **var_value**: value of the variable
   - **var_unit**: unit of the variable
   - **var_alg**: algorithm associated with the variable if any
   - **var_need**: variables needed to calculate the variable if any
   - **v_linked**: linked variable if any
   - **user_input**: user input variable if any

.. csv-table:: [Insert Table Title]
   :header-rows: 1
   :file: ../../../../tutorial/ref_tables/fusion_var.csv
   :widths: auto
   :class: wide-table

