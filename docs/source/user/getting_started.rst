Getting Started
===========================

Welcome to ACCERT! This guide will help you get started with using ACCERT for cost estimation and analysis of nuclear reactor components.
For installation instructions, please see the :doc:`Installation Guide <install>`.


Overview
--------

**Code of Accounts (COA)**

- Every component of a nuclear reactor is assigned a unique Code of Account (COA).
- COAs are structured in hierarchical levels, typically between levels 0-3, breaking down cost elements into subtasks.
- Each COA includes three main cost categories:

  - **Factory Equipment Costs**: Usually described in dollars.
  - **Labor Costs**: Costs associated with labor required.
  - **Material Costs**: Costs of materials, quantified in specific units (e.g., square feet, tons).

**Workbench**

- ACCERT uses the NEAMS Workbench interface to display and manage cost data.
- Workbench provides a user-friendly environment for running ACCERT and viewing results.

**Databases**

- ACCERT relies on relational databases to store cost data.
- Databases compile costs of various components, organized by their COAs and levels.
- As of June 2023, ACCERT uses cost reports from two reference reactor models:

  - **Pressurized Water Reactor (PWR12-BE)**
  - **Advanced Burner Reactor (ABR-1000)**
- ACCERT algorithms adjust costs for inflation and other factors over time.

Setting Up ACCERT
-----------------

Before running ACCERT, ensure that you have completed the installation steps as described in the Installation Guide.

Using ACCERT via Python
-----------------------

1. **Prepare Your Input File**

   - ACCERT requires an input file in SON format (`.son`), which defines the parameters and variables for your reactor model.
   - You can use one of the provided reference models or create your own input file.
   - Example reference models:

     - `PWR12-BE.son`
     - `ABR1000.son`
     - `heatpipe.son`
     - `Fusion.son`


2. **Modify Reactor Parameters**

   - Open the `.son` file in your text editor or IDE (e.g., Visual Studio Code).
   - Add the required parameters for your reactor model:

     - **Thermal Power (`mwth`)**: Thermal power output of your reactor in MW.
     - **Electric Power (`mwe`)**: Electric power output of your reactor in MW.
   - Optional: Modify other variables to match your reactor design.

     Example variable modification:

     .. code-block:: text

         var(Cont_rad_out_m) { value = 30 unit = m }

     - This changes the containment radius to 30 meters.

3. **Run ACCERT**

   - In the terminal, navigate to the `tutorial` directory (or the directory containing your input file):

     .. code-block:: shell

         $ cd ../tutorial

   - Run ACCERT using the `Main.py` script and specify your input file:

     .. code-block:: shell

         $ python ../src/Main.py -i myinput.son

     - Replace `myinput.son` with the path to your input file.

4. **View the Output**

   - ACCERT generates an output file named `output.out`.
   - Open `output.out` in your text editor to view the results.
   - The output includes:

     - **User Input Summary**: Displays the reference model and parameters used.
     - **Extracted Variables**: Lists the variables that were changed and their values.
     - **Affected Cost Elements**: Shows which cost elements are affected by the changed variables.
     - **Updated Cost Elements**: Details how each cost element was updated based on the algorithms.
     - **Roll-up of Cost Elements**: Aggregates cost elements from lower levels to higher levels.
     - **Results Table**: A summary table of COAs, descriptions, costs, and review statuses.

   - Example output snippet:

     .. code-block:: text

         ======================================== Reading user input ========================================

         [USER_INPUT] Reference model is "LFR"

         Parameter "mwe" is required for cost elements:
         241_fac, 242_fac, 245_fac, 246_fac, 241_lab, ...

         [USER_INPUT] Thermal power is 1000 MW

         [USER_INPUT] Electric power is 380 MW

     - *Note*: The full output is extensive; refer to `output.out` for complete details.

5. **Review Results**

   - Analyze the results in `output.out` to understand how your input parameters affected the cost estimates.
   - Check the **Results Table** for a summary of costs and review statuses.

6. **Output Files**

   - ACCERT may generate additional output files in Excel format for detailed analysis:

     - `lfr_variable_affected_cost_elements.xlsx`
     - `lfr_updated_cost_element.xlsx`
     - `lfr_updated_account.xlsx`

     These files contain detailed data on the cost elements and accounts affected by your inputs.

Using ACCERT via NEAMS Workbench
--------------------------------

1. **Open NEAMS Workbench**

   - Launch the NEAMS Workbench application.

2. **Add ACCERT Configuration**

   - Navigate to `Workbench` > `Configurations`.
   - Click `Add` and select `ACCERT` from the list.
   - Set the **Executable** path to `Main.py` in the `ACCERT/src/` directory.
   - Load the grammar by clicking `Load Grammar`.

3. **Run ACCERT**

   - Open your input file within Workbench.
   - Click the `Run` button to execute ACCERT.
   - Open and view results `output.out` directly in Workbench.

Key Concepts
------------

**Algorithms and Cost Scaling**

- ACCERT uses algorithms to update cost elements based on input variables.
- Common algorithms include:

  - **MWth_scale**: Scales costs based on thermal power.
  - **MWe_scale**: Scales costs based on electric power.

**Review Status**

- The results table includes a **Review Status** column:

  - **Unchanged**: Cost elements not affected by input changes.
  - **Ready for Review**: Updated cost elements that may need verification.
  - **User Input**: Costs directly modified by user inputs.
  - **Updated**: Costs updated based on algorithms.

Example Output
--------------

Here is an example of ACCERT's output for a Lead-cooled Fast Reactor (LFR) model:

.. code-block:: text

   ======================================== Reading user input ========================================

   [USER_INPUT] Reference model is "LFR"

   Parameter "mwe" is required for cost elements:
   241_fac, 242_fac, 245_fac, 246_fac, 241_lab, 242_lab, 245_lab, 246_lab, 241_mat, 242_mat, 245_mat,
   246_mat

   Parameter "mwth" is required for cost elements:
   213_fac, 220A.224_fac, 222.11_fac, 222.12_fac, 222.13_fac, 222.14_fac, 222_fac, 226.4_fac, 213_lab,
   222.11_lab, 222.12_lab, 222.13_lab, 222.14_lab, 222_lab, 213_mat, 222.11_mat, 222.12_mat,
   222.13_mat, 222.14_mat, 222_mat

   [USER_INPUT] Thermal power is 1000 MW

   [USER_INPUT] Electric power is 380 MW

   =================================Extracting user changed variables==================================

   +----------+-----------------+-----------+----------+
   | var_name | var_description | var_value | var_unit |
   +----------+-----------------+-----------+----------+
   |   mwe    |  user_input MWE |   380.00  |    MW    |
   |   mwth   | user_input mwth |  1,000.00 |    MW    |
   +----------+-----------------+-----------+----------+

   ================================ Extracting affected cost elements =================================

   variable "mwe" affects cost element(s):
   241_fac, 242_fac, 245_fac, 246_fac, 241_lab, 242_lab, 245_lab, 246_lab, 241_mat, 242_mat, 245_mat,
   246_mat

   variable "mwth" affects cost element(s):
   213_fac, 220A.224_fac, 222.11_fac, 222.12_fac, 222.13_fac, 222.14_fac, 222_fac, 226.4_fac, 213_lab,
   222.11_lab, 222.12_lab, 222.13_lab, 222.14_lab, 222_lab, 213_mat, 222.11_mat, 222.12_mat,
   222.13_mat, 222.14_mat, 222_mat

   ====================================== Updating cost elements ======================================

   [Updating] Cost element [222_mat], running algorithm: [MWth_scale],
   [Updating] with formulation: cost_of_ref*(thermal_power/thermal_power_of_ref)^thermal_power_scale
   [Updated]  Reference value is : $523,270    , calculated value is: $523,270

   ... (additional cost elements updated)

   =============================== Generating results table for review ================================

   +-----------------+-------------------------------------------------+------------+-------+------------------+
   | code_of_account |               account_description               | total_cost | level |  review_status   |
   +-----------------+-------------------------------------------------+------------+-------+------------------+
   |   211           | Yardwork                                        |      71.21 |   2   |    Unchanged     |
   |   212           | Reactor containment building                    |      81.43 |   2   |    Unchanged     |
   |   213           | Turbine room and heater bay                     |      24.60 |   2   | Ready for Review |
   |   216           | Waste processing building                       |      36.75 |   2   |    User Input    |
   |   222           | Main heat transfer transport system             |       8.42 |   2   |     Updated      |
   |   241           | Switchgear                                      |      21.90 |   2   | Ready for Review |
   |   ...           | ...                                             |     ...    |  ...  |       ...        |
   +-----------------+-------------------------------------------------+------------+-------+------------------+

For the full output, please refer to the `output.out` file generated by ACCERT.

Next Steps
----------

- **Explore Variables**: Experiment with different input parameters to see how they affect cost estimates.
- **Review Algorithms**: Understand the cost scaling algorithms used by ACCERT.
- **Consult Documentation**: Refer to the User's Guide for detailed explanations of ACCERT's features. 




