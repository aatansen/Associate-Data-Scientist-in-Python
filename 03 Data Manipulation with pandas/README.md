<div align="center">
<h1>Data Manipulation with pandas</h1>
</div>

# **Context**
- [**Context**](#context)
  - [**Data Manipulation with pandas**](#data-manipulation-with-pandas)
    - [Transforming DataFrames](#transforming-dataframes)
      - [Inspecting a DataFrame](#inspecting-a-dataframe)
      - [Parts of a DataFrame](#parts-of-a-dataframe)
      - [Sorting rows](#sorting-rows)
      - [Subsetting columns](#subsetting-columns)
      - [Subsetting rows](#subsetting-rows)
      - [Subsetting rows by categorical variables](#subsetting-rows-by-categorical-variables)

## **[Data Manipulation with pandas](https://www.datacamp.com/courses/data-manipulation-with-pandas)**

- Course Instructor
  - [Maggie Matsui](https://www.linkedin.com/in/maggie-matsui/)
  - [Richie Cotton](https://www.linkedin.com/in/richierocks/)
- Collaborators
  - [Amy Peterson](https://www.datacamp.com/portfolio/amy-4121b590-cc52-442a-9779-03eb58089e08)
  - [Adel Nehme](https://www.linkedin.com/in/adelnehme/)
  - [Alex Yarosh](https://www.linkedin.com/in/alexyar/)
  - [Justin Saddlemyer](https://www.linkedin.com/in/justinsaddlemyer/)
- Datasets
  - [Avocado prices](https://assets.datacamp.com/production/repositories/5386/datasets/5528f46cc712c9083a6881f787fc9b34ab53d5ea/avoplotto.pkl)
  - [Walmart sales](https://assets.datacamp.com/production/repositories/5386/datasets/5110afec30fc30bc5f3cf67b188d1513c3d6d940/sales_subset.csv)
  - [Homelessness data](https://assets.datacamp.com/production/repositories/5386/datasets/1a0ab2e8557930ec06473c16521874e516a216ae/homelessness.csv)
  - [Temperatures](https://assets.datacamp.com/production/repositories/5386/datasets/47f5fde162bae3549ca7d5c26fb4c4639f100f28/temperatures.csv)

### [Transforming DataFrames](./01%20Transforming%20DataFrames/)

#### [Inspecting a DataFrame](./01%20Transforming%20DataFrames/01_inspecting_a_dataframe.py)

- Print information about the column types and missing values in homelessness.

  ```py
  # Print the head of the homelessness data
  print(____)
  ```

- Print information about the column types and missing values in homelessness.

  ```py
  # Print information about homelessness
  print(____)
  ```

- Print the number of rows and columns in homelessness.

  ```py
  # Print the shape of homelessness
  print(____)
  ```

- Print some summary statistics that describe the homelessness DataFrame.

  ```py
  # Print a description of homelessness
  print(____)
  ```

[⬆️ Go to Context](#context)

#### [Parts of a DataFrame](./01%20Transforming%20DataFrames/02_parts_of_a_data_frame.py)

- Import `pandas` using the alias `pd`.
- Print a 2D NumPy array of the values in `homelessness`.
- Print the column names of `homelessness`.
- Print the index of `homelessness`.

  ```py
  # Import pandas using the alias pd
  ____

  # Print the values of homelessness
  ____

  # Print the column index of homelessness
  ____

  # Print the row index of homelessness
  ____
  ```

[⬆️ Go to Context](#context)

#### [Sorting rows](./01%20Transforming%20DataFrames/03_sorting_rows.py)

- Sort `homelessness` by the number of homeless individuals in the `individuals` column, from smallest to largest, and save this as homelessness_ind.
- Print the head of the sorted DataFrame.

  ```py
  # Sort homelessness by individuals
  homelessness_ind = ____

  # Print the top few rows
  print(____)
  ```

- Sort `homelessness` by the number of homeless `family_members` in descending order, and save this as `homelessness_fam`.

  ```py
  # Sort homelessness by descending family members
  homelessness_fam = ____

  print(homelessness_fam.head())
  ```

- Sort `homelessness` first by region (ascending), and then by number of family members (descending). Save this as `homelessness_reg_fam`.

  ```py
  # Sort homelessness by region, then descending family members
  homelessness_reg_fam = ____

  # Print the top few rows
  print(homelessness_reg_fam.head())
  ```

[⬆️ Go to Context](#context)

#### [Subsetting columns](./01%20Transforming%20DataFrames/04_subsetting_columns.py)

- Create a Series called `individuals` that contains only the `individuals` column of `homelessness`.

  ```py
  # Select the individuals column
  individuals = ____

  print(individuals.head())
  ```

- Create a DataFrame called `state_fam` that contains only the `state` and `family_members` columns of `homelessness`, in that order.

  ```py
  # Select the state and family_members columns
  state_fam = ____

  print(state_fam.head())
  ```

- Create a DataFrame called `ind_state` that contains the `individuals` and `state` columns of `homelessness`, in that order.

  ```py
  # Select only the individuals and state columns, in that order
  ind_state = ____

  print(ind_state.head())
  ```

[⬆️ Go to Context](#context)

#### [Subsetting rows](./01%20Transforming%20DataFrames/05_subsetting_rows.py)

- Filter `homelessness` for cases where the number of `individuals` is greater than ten thousand, assigning to `ind_gt_10k`. View the printed result.

  ```py
  # Filter for rows where individuals is greater than 10000
  ind_gt_10k = ____

  # See the result
  print(ind_gt_10k)
  ```

- Filter `homelessness` for cases where the USA Census `region` is `"Mountain"`, assigning to `mountain_reg`. View the printed result.

  ```py
  # Filter for rows where region is Mountain
  mountain_reg = ____

  # See the result
  ____
  ```

- Filter `homelessness` for cases where the number of `family_members` is less than one thousand and the `region` is `"Pacific"`, assigning to `fam_lt_1k_pac`. View the printed result.

  ```py
  # Filter for rows where family_members is less than 1000
  # and region is Pacific
  fam_lt_1k_pac = ____

  # See the result
  print(fam_lt_1k_pac)
  ```

[⬆️ Go to Context](#context)

#### [Subsetting rows by categorical variables](./01%20Transforming%20DataFrames/06_subsetting_rows_by_categorical_variables.py)

- Filter `homelessness` for cases where the USA census `state` is in the list of Mojave states, `canu`, assigning to `mojave_homelessness`. View the printed result.

  ```py
  # The Mojave Desert states
  canu = ["California", "Arizona", "Nevada", "Utah"]

  # Filter for rows in the Mojave Desert states
  mojave_homelessness = homelessness[____]

  # See the result
  print(mojave_homelessness)
  ```

[⬆️ Go to Context](#context)
