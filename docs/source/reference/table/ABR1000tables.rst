ABR 1000 Tables
===================================

some discussion about the table

ABR1000_account Table
---------------------
This table contains the account information for the ABR1000 model.
ABR1000 account table can also ordered by GNCOA. Each entity in the account table is associated with a unique identifier, which is used to track and categorize costs. The table is organized into multiple levels, with each level representing a different component or subtask. 

The table includes the following columns:

   - `ind`: unique identifier for each account
   - `code_of_account`: code of account 
   - `account_description`: description of the account
   - `total_cost`: total cost of the account unit in dollars
   - `level`: level of the account
   - `supaccount`: superior account
   - `review_status`: review status of the account, note that the default value should always be `Unchanged`
   - `prn`: percentage of the account cost in the total direct cost
   - `gncoa`: generalized nuclear code of account
   - `gn_level`: generalized nuclear code of account level
   - `gn_supaccount`: generalized nuclear code of account superior account
   - `gn_ind`: generalized nuclear code of account unique identifier


.. csv-table:: [ABR1000_account]
   :header-rows: 1
   :file: ../../../../tutorial/ref_tables/ABR1000_account.csv
   :widths: auto
   :class: scrollable-table

ABR1000_cost_element Table
--------------------------
This table contains the cost element information for the ABR1000 model. Each entitiy in the account 
table is divided into 3 main cost categories: Factory Equipment Costs, Labor Costs, and Material Costs.
The cost element table is associated with a unique identifier, which is used to track and categorize costs. The table is connected to the account table through the `account` column, which links each cost element to a specific account. It is also connected to the variable table through the `variables` column, and the algorithm table through the `alg_name` column.

The table includes the following columns:

   - `ind`: unique identifier for each cost element
   - `cost_element`: cost element name
   - `cost_2017`: cost of the element in 2017 dollars
   - `sup_cost_ele`: superior cost element
   - `alg_name`: algorithm name
   - `fun_unit`: algorithm function output unit
   - `variables`: variables used in the algorithm
   - `account`: account associated with the cost element
   - `algno`: algorithm number in the algorithm table
   - `updated`: updated status of the cost element, 0 for unchanged and 1 for updated, note that the default value should always be 0
 
.. csv-table:: [ABR1000_cost_element]
   :header-rows: 1
   :file: ../../../../tutorial/ref_tables/ABR1000_cost_element.csv
   :widths: auto
   :class: scrollable-table

.. csv-table:: [ABR1000_variable]
    :header-rows: 1
    :file: ../../../../tutorial/ref_tables/ABR1000_variable.csv
    :widths: auto
   :class: scrollable-table

