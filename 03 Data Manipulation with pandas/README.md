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
      - [Adding new columns](#adding-new-columns)
      - [Combo-attack](#combo-attack)
    - [Aggregating DataFrames](#aggregating-dataframes)
      - [Mean and median](#mean-and-median)
      - [Summarizing dates](#summarizing-dates)
      - [Efficient summaries](#efficient-summaries)
      - [Cumulative statistics](#cumulative-statistics)
      - [Dropping duplicates](#dropping-duplicates)
      - [Counting categorical variables](#counting-categorical-variables)
      - [What percent of sales occurred at each store type](#what-percent-of-sales-occurred-at-each-store-type)
      - [Calculations with groupby](#calculations-with-groupby)
      - [Multiple grouped summaries](#multiple-grouped-summaries)
      - [Pivoting on one variable](#pivoting-on-one-variable)

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

#### [Adding new columns](./01%20Transforming%20DataFrames/07_adding_new_columns.py)

- Add a new column to `homelessness`, named `total`, containing the sum of the `individuals` and `family_members` columns.
- Add another column to `homelessness`, named `p_homeless`, containing the proportion of the `total` homeless population to the total population in each state `state_pop`.

  ```py
  # Add total col as sum of individuals and family_members
  ____

  # Add p_homeless col as proportion of total homeless population to the state population
  ____

  # See the result
  print(homelessness)
  ```

[⬆️ Go to Context](#context)

#### [Combo-attack](./01%20Transforming%20DataFrames/08_combo_attack.py)

- Add a column to `homelessness`, `indiv_per_10k`, containing the number of homeless individuals per ten thousand people in each state, using `state_pop` for state population.
- Subset rows where `indiv_per_10k` is higher than `20`, assigning to `high_homelessness`.
- Sort `high_homelessness` by descending `indiv_per_10k`, assigning to `high_homelessness_srt`.
- Select only the `state` and `indiv_per_10k` columns of `high_homelessness_srt` and save as `result`. *Look at the `result`.*

  ```py
  # Create indiv_per_10k col as homeless individuals per 10k state pop
  homelessness["indiv_per_10k"] = 10000 * ____ / ____

  # Subset rows for indiv_per_10k greater than 20
  high_homelessness = ____

  # Sort high_homelessness by descending indiv_per_10k
  high_homelessness_srt = ____

  # From high_homelessness_srt, select the state and indiv_per_10k cols
  result = ____

  # See the result
  print(result)
  ```

[⬆️ Go to Context](#context)

### [Aggregating DataFrames](./02%20Aggregating%20DataFrames/)

#### [Mean and median](./02%20Aggregating%20DataFrames/01_mean_and_median.py)

- Explore your new DataFrame first by printing the first few rows of the `sales` DataFrame.
- Print information about the columns in `sales`.
- Print the mean of the `weekly_sales` column.
- Print the median of the `weekly_sales` column.

  ```py
  # Print the head of the sales DataFrame
  print(___)

  # Print the info about the sales DataFrame
  print(___)

  # Print the mean of weekly_sales
  print(___)

  # Print the median of weekly_sales
  print(___)
  ```

[⬆️ Go to Context](#context)

#### [Summarizing dates](./02%20Aggregating%20DataFrames/02_summarizing_dates.py)

- Print the maximum of the `date` column.
- Print the minimum of the `date` column.

  ```py
  # Print the maximum of the date column
  ___

  # Print the minimum of the date column
  ___
  ```

[⬆️ Go to Context](#context)

#### [Efficient summaries](./02%20Aggregating%20DataFrames/03_efficient_summaries.py)

- Use the custom `iqr` function defined for you along with `.agg()` to print the IQR of the `temperature_c` column of `sales`.

  ```py
  # A custom IQR function
  def iqr(column):
      return column.quantile(0.75) - column.quantile(0.25)

  # Print IQR of the temperature_c column
  print(____)
  ```

- Update the column selection to use the custom `iqr` function with `.agg()` to print the IQR of `temperature_c`, `fuel_price_usd_per_l`, and `unemployment`, in that order.

  ```py
  # A custom IQR function
  def iqr(column):
      return column.quantile(0.75) - column.quantile(0.25)

  # Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
  print(sales[["temperature_c", ____, ____]].agg(iqr))
  ```

- Update the aggregation functions called by `.agg()`: include `iqr` and `"median"` in that order.

  ```py
  # Create a custom IQR function
  def iqr(column):
      return column.quantile(0.75) - column.quantile(0.25)

  # Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
  print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))
  ```

[⬆️ Go to Context](#context)

#### [Cumulative statistics](./02%20Aggregating%20DataFrames/04_cumulative_statistics.py)

- Sort the rows of `sales_1_1` by the `date` column in ascending order.
- Get the cumulative sum of `weekly_sales` and add it as a new column of `sales_1_1` called `cum_weekly_sales`.
- Get the cumulative maximum of `weekly_sales`, and add it as a column called `cum_max_sales`.
- Print the `date`, `weekly_sales`, `cum_weekly_sales`, and `cum_max_sales` columns.

  ```py
  # Sort sales_1_1 by date
  sales_1_1 = ____

  # Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
  sales_1_1[____] = ____

  # Get the cumulative max of weekly_sales, add as cum_max_sales col
  ____

  # See the columns you calculated
  print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
  ```

[⬆️ Go to Context](#context)

#### [Dropping duplicates](./02%20Aggregating%20DataFrames/05_dropping_duplicates.py)

- Remove rows of `sales` with duplicate pairs of `store` and `type` and save as `store_types` and print the head.
- Remove rows of `sales` with duplicate pairs of `store` and `department` and save as `store_depts` and print the head.
- Subset the rows that are holiday weeks using the `is_holiday` column, and drop the duplicate `date`s, saving as `holiday_dates`.
- Select the `date` column of `holiday_dates`, and print.

  ```py
  # Drop duplicate store/type combinations
  store_types = ____
  print(store_types.head())

  # Drop duplicate store/department combinations
  store_depts = ____
  print(store_depts.head())

  # Subset the rows where is_holiday is True and drop duplicate dates
  holiday_dates = sales[sales[____]].drop_duplicates(____)

  # Print date col of holiday_dates
  print(____)
  ```

[⬆️ Go to Context](#context)

#### [Counting categorical variables](./02%20Aggregating%20DataFrames/06_counting_categorical_variables.py)

- Count the number of stores of each store `type` in `store_types`.
- Count the proportion of stores of each store `type` in `store_types`.
- Count the number of stores of each `department` in `store_depts`, sorting the counts in descending order.
- Count the proportion of stores of each `department` in `store_depts`, sorting the proportions in descending order.

  ```py
  # Count the number of stores of each type
  store_counts = ____
  print(store_counts)

  # Get the proportion of stores of each type
  store_props = ____
  print(store_props)

  # Count the number of stores for each department and sort
  dept_counts_sorted = ____
  print(dept_counts_sorted)

  # Get the proportion of stores in each department and sort
  dept_props_sorted = ____.____(sort=____, normalize=____)
  print(dept_props_sorted)
  ```

[⬆️ Go to Context](#context)

#### [What percent of sales occurred at each store type](./02%20Aggregating%20DataFrames/07_what_percent_of_sales_occurred_at_each_store_type.PY)

- Calculate the total `weekly_sales` over the whole dataset.
- Subset for `type` `"A"` stores, and calculate their total weekly sales.
- Do the same for `type` `"B"` and `type` `"C"` stores.
- Combine the A/B/C results into a list, and divide by `sales_all` to get the proportion of sales by type.

  ```py
  # Calc total weekly sales
  sales_all = ____["____"].____()

  # Subset for type A stores, calc total weekly sales
  sales_A = ____[____["____"] == "____"]["____"].____()

  # Subset for type B stores, calc total weekly sales
  sales_B = ____

  # Subset for type C stores, calc total weekly sales
  sales_C = ____

  # Get proportion for each type
  sales_propn_by_type = [sales_A, ____, ____] / ____
  print(sales_propn_by_type)
  ```

[⬆️ Go to Context](#context)

#### [Calculations with groupby](./02%20Aggregating%20DataFrames/08_calculations_with_groupby.py)

- Group `sales` by `"type"`, take the sum of `"weekly_sales"`, and store as `sales_by_type`.
- Calculate the proportion of sales at each store type by dividing by the sum of `sales_by_type`. Assign to `sales_propn_by_type`.

  ```py
  # Group by type; calc total weekly sales
  sales_by_type = sales.____("____")["____"].____()

  # Get proportion for each type
  sales_propn_by_type = ____ / sum(____)
  print(sales_propn_by_type)
  ```

- Group `sales` by `"type"` and "`is_holiday`", take the sum of `weekly_sales`, and store as `sales_by_type_is_holiday`.

  ```py
  # From previous step
  sales_by_type = sales.groupby("type")["weekly_sales"].sum()

  # Group by type and is_holiday; calc total weekly sales
  sales_by_type_is_holiday = ____
  print(sales_by_type_is_holiday)
  ```

[⬆️ Go to Context](#context)

#### [Multiple grouped summaries]()

- Get the min, max, mean, and median of `weekly_sales` for each store type using `.groupby()` and `.agg()`. Store this as `sales_stats`.
- Get the min, max, mean, and median of `unemployment` and `fuel_price_usd_per_l` for each store type. Store this as `unemp_fuel_stats`.

  ```py
  # For each store type, aggregate weekly_sales: get min, max, mean, and median
  sales_stats = ____

  # Print sales_stats
  print(sales_stats)

  # For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
  unemp_fuel_stats = ____

  # Print unemp_fuel_stats
  print(unemp_fuel_stats)
  ```

[⬆️ Go to Context](#context)

#### [Pivoting on one variable](./02%20Aggregating%20DataFrames/10_pivoting_on_one_variable.py)

- Get the mean `weekly_sales` by `type` using `.pivot_table()` and store as `mean_sales_by_type`.

  ```py
  # Pivot for mean weekly_sales for each store type
  mean_sales_by_type = sales.___

  # Print mean_sales_by_type
  print(mean_sales_by_type)
  ```

- Get the mean and median of `weekly_sales` by `type` using `.pivot_table()` and store as `mean_med_sales_by_type`.

```py
# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(___)

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)
```

- Get the mean of `weekly_sales` by `type` and `is_holiday` using `.pivot_table()` and store as `mean_sales_by_type_holiday`.

  ```py
  # Pivot for mean weekly_sales by store type and holiday
  mean_sales_by_type_holiday = sales.pivot_table(___)

  # Print mean_sales_by_type_holiday
  print(mean_sales_by_type_holiday)
  ```

[⬆️ Go to Context](#context)
