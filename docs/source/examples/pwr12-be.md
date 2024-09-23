
# ACCERT Running Example: PWR12-BE and Other Reactor Designs

This document provides a comprehensive explanation of the ACCERT (Advanced Cost Estimation and Reference Tool) running examples, including the **PWR12-BE**, **ABR1000**, and **fusion** reactor models. It integrates key ACCERT concepts to elucidate how the input files are structured and why they are designed in a particular manner.

---

## Table of Contents

1. [Introduction to ACCERT](#introduction-to-accert)
2. [ACCERT Methodology Overview](#accert-methodology-overview)
3. [PWR12-BE Input File Explained](#pwr12-be-input-file-explained)
    - [General Structure](#general-structure)
    - [Required Parameters](#required-parameters)
    - [Optional Parameters](#optional-parameters)
    - [Codes of Accounts (COA) Hierarchy](#codes-of-accounts-coa-hierarchy)
    - [Cost Elements and Algorithms](#cost-elements-and-algorithms)
4. [ABR1000 Input File Explained](#abr1000-input-file-explained)
    - [General Structure](#general-structure-1)
    - [Defined Parameters](#defined-parameters)
5. [Fusion Reactor Input File Explained](#fusion-reactor-input-file-explained)
    - [General Structure](#general-structure-2)
    - [Defined Algorithms and Variables](#defined-algorithms-and-variables)
6. [ACCERT Concepts Integrated](#accert-concepts-integrated)
    - [Relational Database Structure](#relational-database-structure)
    - [Hierarchical Decomposition (COA)](#hierarchical-decomposition-coa)
    - [Algorithm Execution and Cost Escalation](#algorithm-execution-and-cost-escalation)
7. [Structure and Purpose of `.son` Input Files](#structure-and-purpose-of-son-input-files)
    - [Why `.son` Inputs are Structured This Way](#why-son-inputs-are-structured-this-way)
8. [Conclusion](#conclusion)

---

## Introduction to ACCERT

ACCERT is a sophisticated tool designed to estimate the capital costs of nuclear reactor designs and other large facilities through a detailed, item-by-item approach. By leveraging historical cost data and customizable algorithms, ACCERT provides transparent, defensible, and scalable cost estimates tailored to various reactor concepts.

---

## ACCERT Methodology Overview

The ACCERT methodology encompasses the following key steps:

1. **Reference Model Selection**: Begin with a well-documented reference reactor (e.g., PWR12-BE) with extensive historical cost data.
2. **Component Ranking**: Identify and rank reactor components based on their fractional contribution to total direct costs.
3. **Cost Model Development**: Develop detailed cost models for significant components (those contributing >2% to total direct costs).
4. **Indirect Cost Estimation**: Estimate indirect costs (owner’s, contingencies) based on historical proportions relative to direct costs.
5. **Application to New Designs**: Utilize developed models and algorithms to estimate costs for new reactor designs (e.g., ABR1000).

This approach ensures efficiency by focusing on major cost drivers while maintaining flexibility to incorporate more detailed components as needed.

---

## PWR12-BE Input File Explained

### General Structure

The **PWR12-BE** input file (`PWR12-BE.son`) is a detailed configuration that serves as the reference model for ACCERT. It defines the reactor's parameters, hierarchical cost structure, and specific cost estimation algorithms.

```plaintext
accert{
    ref_model = "PWR12-BE"
    ...
}
```

- **`accert{}`**: Denotes the start of the ACCERT input configuration.
- **`ref_model`**: Specifies the reference reactor model, "PWR12-BE" in this case.

### Required Parameters

These parameters are essential for scaling cost estimates based on the reactor's power output.

```plaintext
power(Thermal){ value = 3000   unit = MW }  % Reference value for PWR-12BE is 3431 MW
power(Electric){ value = 1000   unit = MW } % Reference value for PWR-12BE is 1143 MW
```

- **`power(Thermal)`**: Thermal power output (3000 MW vs. reference 3431 MW).
- **`power(Electric)`**: Electrical power output (1000 MW vs. reference 1143 MW).

### Optional Parameters

These allow for customization based on specific design features.

```plaintext
% var(Cont_rad_out_m){value = 20 unit = m}% Reference value for PWR-12BE is 23 m
```

- **`var(Cont_rad_out_m)`**: Containment radius (20 meters vs. reference 23 meters).

### Codes of Accounts (COA) Hierarchy

ACCERT organizes costs using a hierarchical "Codes of Accounts" (COA) structure, reflecting major systems and subsystems.

```plaintext
l0COA(2){
    l1COA(21){
        l2COA(211){
            ce("211_fac"){
                alg("esc_1987"){
                    var(ref_211_fac){ value = 0.27   unit = million }
                    var(ref_211_mat){ value = 10.3   unit = million }
                }
            }   
        }
        ...
    }
    ...
}
```

- **`l0COA(2)`**: Top-level COA category.
- **`l1COA(21)`**, **`l1COA(22)`**, **`l1COA(23)`**: Subcategories under COA `2`.
- **`l2COA`**, **`l3COA`**, etc.: Further subdivisions representing specific components or cost elements.

### Cost Elements and Algorithms

Each COA can contain cost elements (`ce`) calculated using specific algorithms (`alg`).

#### Example: COA 21

```plaintext
l1COA(21){
    l2COA(211){
        ce("211_fac"){
            alg("esc_1987"){
                var(ref_211_fac){ value = 0.27   unit = million }
                var(ref_211_mat){ value = 10.3   unit = million }
            }
        }   
    }
    l2COA(213){
        ce("213_fac"){
            alg("MWth_scale"){
                var(c_213_fac){ value = 1.79   unit = million }
            }
        }   
    }
    l2COA(217){
        total_cost{value = 28149700 unit = dollar}       
    }
    l2COA(new){ 
        newCOA(useraddcoa){descr = 'a user added coa'}
        total_cost{value = 9 unit = million}       
    }
}
```

- **`ce("211_fac")`**: Cost element for facility `211_fac` using `esc_1987` algorithm.
    - **Variables**:
        - `ref_211_fac`: Reference facility cost (`0.27 million USD`).
        - `ref_211_mat`: Reference material cost (`10.3 million USD`).
- **`ce("213_fac")`**: Cost element `213_fac` using `MWth_scale` algorithm.
    - **Variable**:
        - `c_213_fac`: Cost value (`1.79 million USD`).
- **`total_cost`**: Directly specifies total costs for COA `217` and user-added COA `new`.

#### Example: COA 22

```plaintext
l1COA(22){
    l2COA("220A"){
        l3COA("221.12"){
            ce("221.12_fac"){
                alg("unit_weights"){
                    var("c_221.12_cs_weight"){value = 538 unit = ton} 
                    var("c_221.12_ss_weight"){value = 40340 unit = lbs}
                }
            }
        }
    }
}
```

- **`ce("221.12_fac")`**: Cost element `221.12_fac` using `unit_weights` algorithm.
    - **Variables**:
        - `c_221.12_cs_weight`: Copper-steel weight (`538 tons`).
        - `c_221.12_ss_weight`: Stainless steel weight (`40,340 lbs`).

#### Example: COA 23

```plaintext
l1COA(23){
   l2COA("231"){
        ce("231_fac"){
            alg("dev_factor_ref"){
                var("n_231"){
                    alg("tur_exp_n"){
                        var(p_in){ value = 68  unit = bar }
                    }
                }
            }  
        }
    }
}
```

- **`ce("231_fac")`**: Cost element `231_fac` using `dev_factor_ref` algorithm.
    - **Variable**:
        - `n_231`: Defined using nested `tur_exp_n` algorithm with input pressure (`68 bar`).

### Summary of PWR12-BE Input File Components

- **Reference Model**: `PWR12-BE` serves as the baseline.
- **Required Parameters**: Thermal and electrical power outputs.
- **Optional Parameters**: Customizable attributes like containment radius.
- **Codes of Accounts (COA)**: Hierarchical structure organizing cost components.
- **Cost Elements (`ce`)**: Specific cost items with associated algorithms.
- **Algorithms (`alg`)**: Define methodologies for cost calculation using variables (`var`).
- **Total Costs**: Aggregated at various COA levels for comprehensive cost estimation.

---

## ABR1000 Input File Explained

### General Structure

The **ABR1000** input file (`ABR1000.son`) is a simplified configuration compared to PWR12-BE, focusing on essential parameters and a few cost elements.

```plaintext
accert{
    ref_model = "ABR1000"
    power( Thermal ){ value = 1000   unit = MW } 
   
    var(Cont_H_wall_m){ value = 20  unit = m }
    %var(c_pump_ap1000){ value = 30  unit = million }
}
```

- **`ref_model`**: Specifies "ABR1000" as the reference model.
- **`power(Thermal)`**: Thermal power output (`1000 MW`).
- **`var(Cont_H_wall_m)`**: Containment wall height (`20 meters`).
- **Commented Variable**: `%var(c_pump_ap1000)` demonstrates how to include or exclude variables.

### Defined Parameters

- **Thermal Power**: Essential for scaling cost models.
- **Containment Wall Height**: Custom attribute affecting containment building costs.
- **Optional Variables**: Commented lines indicate flexibility in defining additional parameters.

---

## Fusion Reactor Input File Explained

### General Structure

The **fusion** reactor input file (`fusion.son`) demonstrates ACCERT's capability to handle different reactor types with unique cost elements and algorithms.

```plaintext
accert{
    ref_model = "fusion"
    l0COA(2){  
        l1COA(21){
            l2COA("211"){
                alg("acc211"){
                    var("csi"){value = 16 unit = million} 
                    var("lsa"){value = 4 unit = 1}
                }
            }
        }
    }
}
```

- **`ref_model`**: Specifies "fusion" as the reference model.
- **COA Hierarchy**: Similar to PWR12-BE but tailored for fusion-specific components.

### Defined Algorithms and Variables

- **`alg("acc211")`**: Custom algorithm `acc211` for specific cost calculations.
    - **Variables**:
        - `csi`: Cost-specific index (`16 million USD`).
        - `lsa`: Local scaling attribute (`4`).

This structure highlights ACCERT's flexibility in accommodating different reactor technologies by allowing the definition of custom algorithms and variables.

---

## ACCERT Concepts Integrated

### Relational Database Structure

ACCERT utilizes a relational database to ensure data integrity and efficient information management. Each piece of information is entered once and linked through various relationships, facilitating easy access and manipulation.

- **Advantages**:
    - **Data Consistency**: Avoids duplication.
    - **Scalability**: Handles large datasets effectively.
    - **Flexibility**: Easily accommodates new data types and relationships.

### Hierarchical Decomposition (COA)

Costs are organized hierarchically using Codes of Accounts (COA), allowing detailed breakdowns of facilities into manageable components.

- **Levels**:
    - **Level 0 (l0COA)**: Top-level categories.
    - **Level 1 (l1COA)**: Subcategories.
    - **Subsequent Levels (l2COA, l3COA, etc.)**: Further subdivisions for detailed cost elements.

### Algorithm Execution and Cost Escalation

ACCERT employs algorithms to calculate costs based on defined variables. The process involves:

1. **Algorithm Identification**: Determines which algorithm to use for each cost element.
2. **Variable Extraction**: Gathers necessary input variables.
3. **Cost Computation**: Applies the algorithm to compute the cost.
4. **Cost Escalation**: Adjusts costs to the desired year using escalation factors.

This systematic approach ensures accurate and up-to-date cost estimates.

---

## Structure and Purpose of `.son` Input Files

### Why `.son` Inputs are Structured This Way

The `.son` (Structured Object Notation) files are designed to encapsulate all necessary information for ACCERT in a clear, hierarchical, and modular format. This structure offers several benefits:

1. **Clarity**: Hierarchical indentation and labeling make the file easy to read and understand.
2. **Modularity**: Each COA and cost element is self-contained, facilitating updates and maintenance.
3. **Scalability**: Supports complex reactor designs with multiple nested cost components.
4. **Flexibility**: Allows users to define custom algorithms and variables tailored to specific reactor technologies.
5. **Automation-Friendly**: The structured format can be easily parsed and processed by software algorithms, enabling seamless cost estimation workflows.

### Key Components of `.son` Files

- **`accert{}` Block**: Encapsulates the entire configuration.
- **Reference Model (`ref_model`)**: Specifies the reactor or facility being modeled.
- **Parameters (`power`, `var`)**: Define essential and optional attributes influencing cost estimates.
- **COA Hierarchy (`l0COA`, `l1COA`, etc.)**: Organizes costs into a multi-level structure.
- **Cost Elements (`ce`)**: Define specific cost items within each COA.
- **Algorithms (`alg`)**: Specify the methodology for calculating each cost element.
- **Variables (`var`)**: Provide input values required by algorithms for cost computation.

This structured approach ensures that all necessary information is systematically organized, facilitating accurate and efficient cost estimation.

---

## Conclusion

The ACCERT running examples for **PWR12-BE**, **ABR1000**, and **fusion** reactors demonstrate the tool's versatility and robustness in estimating capital costs for various nuclear reactor designs. By leveraging a hierarchical COA structure, customizable algorithms, and a relational database framework, ACCERT provides detailed, transparent, and scalable cost estimates. The `.son` input files are meticulously structured to reflect the complexity and specific requirements of each reactor model, ensuring that ACCERT can adapt to diverse cost estimation needs effectively.

Whether you're working with traditional PWR designs, advanced fast reactors like ABR1000, or emerging fusion technologies, ACCERT offers a comprehensive framework to support informed decision-making and cost optimization in nuclear reactor development.

