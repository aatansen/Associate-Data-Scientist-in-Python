<div align="center">
<h1>Intermediate Python</h1>
</div>

# **Context**
- [**Context**](#context)
  - [**Intermediate Python**](#intermediate-python)
    - [Matplotlib](#matplotlib)
      - [Line plot (1)](#line-plot-1)
      - [Line Plot (2): Interpretation](#line-plot-2-interpretation)
      - [Line plot (3)](#line-plot-3)
      - [Scatter Plot (1)](#scatter-plot-1)
      - [Scatter plot (2)](#scatter-plot-2)
      - [Build a histogram (1)](#build-a-histogram-1)
      - [Build a histogram (2): bins](#build-a-histogram-2-bins)
      - [Build a histogram (3): compare](#build-a-histogram-3-compare)
      - [Choose the right plot (1)](#choose-the-right-plot-1)
      - [Choose the right plot (2)](#choose-the-right-plot-2)
      - [Labels](#labels)
      - [Ticks](#ticks)
      - [Sizes](#sizes)
      - [Colors](#colors)
      - [Additional Customizations](#additional-customizations)
      - [Interpretation](#interpretation)
    - [Dictionaries \& Pandas](#dictionaries--pandas)
      - [Motivation for dictionaries](#motivation-for-dictionaries)
      - [Create dictionary](#create-dictionary)
      - [Access dictionary](#access-dictionary)
      - [Dictionary Manipulation (1)](#dictionary-manipulation-1)
      - [Dictionary Manipulation (2)](#dictionary-manipulation-2)
      - [Dictionariception](#dictionariception)
      - [Dictionary to DataFrame (1)](#dictionary-to-dataframe-1)
      - [Dictionary to DataFrame (2)](#dictionary-to-dataframe-2)
      - [CSV to DataFrame (1)](#csv-to-dataframe-1)
      - [CSV to DataFrame (2)](#csv-to-dataframe-2)
      - [Square Brackets (1)](#square-brackets-1)
      - [Square Brackets (2)](#square-brackets-2)
      - [loc and iloc (1)](#loc-and-iloc-1)
      - [loc and iloc (2)](#loc-and-iloc-2)
      - [loc and iloc (3)](#loc-and-iloc-3)
    - [Logic, Control Flow and Filtering](#logic-control-flow-and-filtering)
      - [Equality](#equality)
      - [Greater and less than](#greater-and-less-than)
      - [Compare arrays](#compare-arrays)
      - [and, or, not (1)](#and-or-not-1)
      - [and, or, not (2)](#and-or-not-2)
      - [Boolean operators with NumPy](#boolean-operators-with-numpy)
      - [Warmup](#warmup)
      - [if](#if)
      - [Add else](#add-else)
      - [Customize further: elif](#customize-further-elif)
      - [Driving right (1)](#driving-right-1)
      - [Driving right (2)](#driving-right-2)
      - [Cars per capita (1)](#cars-per-capita-1)
      - [Cars per capita (2)](#cars-per-capita-2)

## **[Intermediate Python](https://www.datacamp.com/courses/intermediate-python)**

- Course Instructor: [Hugo Bowne-Anderson](https://www.linkedin.com/in/hugo-bowne-anderson-045939a5/)
- Collaborators
  - [Vincent Vankrunkelsven](https://www.linkedin.com/in/vincent-vankrunkelsven-130248103/)
  - [Filip Schouwenaars](https://www.linkedin.com/in/fschouw/)
- Datasets
  - [Gapminder](https://assets.datacamp.com/production/repositories/287/datasets/5b1e4356f9fa5b5ce32e9bd2b75c777284819cca/gapminder.csv)
  - [Cars](https://assets.datacamp.com/production/repositories/287/datasets/79b3c22c47a2f45a800c62cae39035ff2ea4e609/cars.csv)
  - [BRICS](https://assets.datacamp.com/production/repositories/287/datasets/b60fb5bdbeb4e4ab0545c485d351e6ff5428a155/brics.csv)

### [Matplotlib](./01%20Matplotlib/)

#### [Line plot (1)](./01%20Matplotlib/01_line_plot_1.py)

- `print()` the last item from both the year and the pop list to see what the predicted population for the year `2100` is. Use two `print()` functions.
- Before you can start, you should import `matplotlib.pyplot` as `plt`. pyplot is a sub-package of `matplotlib`, hence the dot.
- Use `plt.plot()` to build a line plot. `year` should be mapped on the horizontal axis, `pop` on the vertical axis. Don't forget to finish off with the `plt.show()` function to actually display the plot.

  ```py
  # Print the last item from year and pop



  # Import matplotlib.pyplot as plt


  # Make a line plot: year on the x-axis, pop on the y-axis


  # Display the plot with plt.show()

  ```

[⬆️ Go to Context](#context)

#### Line Plot (2): Interpretation

![Line Plot (2): Interpretation](https://i.imgur.com/xSnqG3w.png)

- Have another look at the plot you created in the previous exercise; it's shown on the right. Based on the plot, in **approximately** what year will there be more than ten billion human beings on this planet?
  - [ ] 2040
  - [ ] 2060
  - [ ] 2085
  - [ ] 2095

  > [Answer](# "2060")

[⬆️ Go to Context](#context)

#### [Line plot (3)](./01%20Matplotlib/02_line_plot_3.py)

- Print the last item from both the list `gdp_cap`, and the list `life_exp`; it is information about `Zimbabwe`.
- Build a line chart, with `gdp_cap` on the `x-axis`, and `life_exp` on the `y-axis`. Does it make sense to plot this data on a line plot?
- Don't forget to finish off with a `plt.show()` command, to actually display the plot.

  ```py
  # Print the last item of gdp_cap and life_exp



  # Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis


  # Display the plot

  ```

  ![Line plot (3)](https://i.imgur.com/a5JmAhE.png)

[⬆️ Go to Context](#context)

#### [Scatter Plot (1)](./01%20Matplotlib/03_scatter_plot_1.py)

- Change the line plot that's coded in the script to a scatter plot.
- A correlation will become clear when you display the GDP per capita on a logarithmic scale. Add the line `plt.xscale('log')`.
- Finish off your script with `plt.show()` to display the plot.

  ```py
  # Change the line plot below to a scatter plot
  plt.plot(gdp_cap, life_exp)

  # Put the x-axis on a logarithmic scale


  # Show plot

  ```

  ![Scatter Plot (1)](https://i.imgur.com/OfJCV23.png)

[⬆️ Go to Context](#context)

#### [Scatter plot (2)](./01%20Matplotlib/04_scatter_plot_2.py)

- Start from scratch: import `matplotlib.pyplot` as `plt`.
- Build a scatter plot, where pop is mapped on the horizontal axis, and `life_exp` is mapped on the vertical axis.
- Finish the script with `plt.show()` to actually display the plot. Do you see a correlation?

  ```py
  # Import package


  # Build Scatter plot


  # Show plot

  ```

  ![Scatter plot (2)](https://i.imgur.com/H6UvmyQ.png)

[⬆️ Go to Context](#context)

#### [Build a histogram (1)](./01%20Matplotlib/05_build_a_histogram_1.py)

- Use `plt.hist()` to create a histogram of the values in `life_exp`. Do not specify the number of bins; Python will set the number of bins to 10 by default for you.
- Add `plt.show()` to actually display the histogram. Can you tell which bin contains the most observations?

  ```py
  # Create histogram of life_exp data


  # Display histogram

  ```

  ![Build a histogram (1)](https://i.imgur.com/4ousNgG.png)

[⬆️ Go to Context](#context)

#### [Build a histogram (2): bins](./01%20Matplotlib/06_build_a_histogram_2_bins.py)

- Build a histogram of `life_exp`, with 5 bins. Can you tell which bin contains the most observations?
- Build another histogram of `life_exp`, this time with 20 bins. Is this better?

  ```py
  # Build histogram with 5 bins


  # Show and clean up plot
  plt.show()
  plt.clf()

  # Build histogram with 20 bins


  # Show and clean up again
  plt.show()
  plt.clf()
  ```

  ![Build a histogram (2): bins](https://i.imgur.com/YgH7roR.png)

[⬆️ Go to Context](#context)

#### [Build a histogram (3): compare](./01%20Matplotlib/07_build_a_histogram_3_compare.py)

- Build a histogram of `life_exp` with `15` bins.
- Build a histogram of `life_exp1950`, also with `15` bins. Is there a big difference with the histogram for the `2007` data?

  ```py
  # Histogram of life_exp, 15 bins


  # Show and clear plot
  plt.show()
  plt.clf()

  # Histogram of life_exp1950, 15 bins


  # Show and clear plot again
  plt.show()
  plt.clf()
  ```

  ![Build a histogram (3): compare](https://i.imgur.com/djFs692.png)

[⬆️ Go to Context](#context)

#### Choose the right plot (1)

- You're a professor teaching Data Science with Python, and you want to visually assess if the grades on your exam follow a particular distribution. Which plot do you use?

  - [ ] Line plot
  - [ ] Scatter plot
  - [ ] Histogram

  > [Answer](# "Histogram")

[⬆️ Go to Context](#context)

#### Choose the right plot (2)

- You're a professor in Data Analytics with Python, and you want to visually assess if longer answers on exam questions lead to higher grades. Which plot do you use?

  - [ ] Line plot
  - [ ] Scatter plot
  - [ ] Histogram

  > [Answer](# "Scatter plot")

[⬆️ Go to Context](#context)

#### [Labels](./01%20Matplotlib/08_labels.py)

- The strings xlab and ylab are already set for you. Use these variables to set the label of the `x-` and `y-axis`.
- The string title is also coded for you. Use it to add a title to the plot.
- After these customizations, finish the script with `plt.show()` to actually display the plot.

  ```py
  # Basic scatter plot, log scale
  plt.scatter(gdp_cap, life_exp)
  plt.xscale('log')

  # Strings
  xlab = 'GDP per Capita [in USD]'
  ylab = 'Life Expectancy [in years]'
  title = 'World Development in 2007'

  # Add axis labels



  # Add title


  # After customizing, display the plot

  ```

  ![Labels](https://i.imgur.com/OR0On7t.png)

[⬆️ Go to Context](#context)

#### [Ticks](./01%20Matplotlib/10_ticks.py)

- Use tick_val and tick_lab as inputs to the xticks() function to make the the plot more readable.
- As usual, display the plot with plt.show() after you've added the customizations.

  ```py
  # Scatter plot
  plt.scatter(gdp_cap, life_exp)

  # Previous customizations
  plt.xscale('log')
  plt.xlabel('GDP per Capita [in USD]')
  plt.ylabel('Life Expectancy [in years]')
  plt.title('World Development in 2007')

  # Definition of tick_val and tick_lab
  tick_val = [1000, 10000, 100000]
  tick_lab = ['1k', '10k', '100k']

  # Adapt the ticks on the x-axis


  # After customizing, display the plot

  ```

![Ticks](https://i.imgur.com/pujfK0R.png)

[⬆️ Go to Context](#context)

#### [Sizes](./01%20Matplotlib/11_sizes.py)

- Run the script to see how the plot changes.
- Looks good, but increasing the size of the bubbles will make things stand out more.
  - Import the `numpy` package as `np`.
  - Use `np.array()` to create a `numpy` array from the list pop. Call this NumPy array np_p`op.
  - Double the values in `np_pop` setting the value of `np_pop` equal to `np_pop` * 2. Because `np_pop` is a NumPy array, each array element will be doubled.
  - Change the s argument inside `plt.scatter()` to be `np_pop` instead of `pop`.

  ```py
  # Import numpy as np


  # Store pop as a numpy array: np_pop


  # Double np_pop


  # Update: set s argument to np_pop
  plt.scatter(gdp_cap, life_exp, s = pop)

  # Previous customizations
  plt.xscale('log')
  plt.xlabel('GDP per Capita [in USD]')
  plt.ylabel('Life Expectancy [in years]')
  plt.title('World Development in 2007')
  plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

  # Display the plot
  plt.show()
  ```

  ![Sizes](https://i.imgur.com/5Gc0Nh7.png)

[⬆️ Go to Context](#context)

#### [Colors](./01%20Matplotlib/12_colors.py)

- Add `c = col` to the arguments of the `plt.scatter()` function.
- Change the opacity of the bubbles by setting the alpha argument to `0.8` inside `plt.scatter()`. Alpha can be set from zero to one, where zero is totally transparent, and one is not at all transparent.

  ```py
  # Specify c and alpha inside plt.scatter()
  plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2)

  # Previous customizations
  plt.xscale('log')
  plt.xlabel('GDP per Capita [in USD]')
  plt.ylabel('Life Expectancy [in years]')
  plt.title('World Development in 2007')
  plt.xticks([1000,10000,100000], ['1k','10k','100k'])

  # Show the plot
  plt.show()
  ```

  ![Colors](https://i.imgur.com/ah6ULQU.png)

[⬆️ Go to Context](#context)

#### [Additional Customizations](./01%20Matplotlib/13_additional_customizations.py)

- Add `plt.grid(True)` after the `plt.text()` calls so that gridlines are drawn on the plot.

  ```py
  # Scatter plot
  plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

  # Previous customizations
  plt.xscale('log')
  plt.xlabel('GDP per Capita [in USD]')
  plt.ylabel('Life Expectancy [in years]')
  plt.title('World Development in 2007')
  plt.xticks([1000,10000,100000], ['1k','10k','100k'])

  # Additional customizations
  plt.text(1550, 71, 'India')
  plt.text(5700, 80, 'China')

  # Add grid() call


  # Show the plot
  plt.show()
  ```

  ![Additional Customizations](https://i.imgur.com/imkg2oq.png)

[⬆️ Go to Context](#context)

#### Interpretation

![Interpretation](https://i.imgur.com/RCPuygF.png)

- If you have a look at your colorful plot, it's clear that people live longer in countries with a higher GDP per capita. No high income countries have really short life expectancy, and no low income countries have very long life expectancy. Still, there is a huge difference in life expectancy between countries on the same income level. Most people live in middle income countries where difference in lifespan is huge between countries; depending on how income is distributed and how it is used.
- What can you say about the plot?
  - [ ] The countries in blue, corresponding to Africa, have both low life expectancy and a low GDP per capita.
  - [ ] There is a negative correlation between GDP per capita and life expectancy.
  - [ ] China has both a lower GDP per capita and lower life expectancy compared to India.

  > [Answer](# "The countries in blue, corresponding to Africa, have both low life expectancy and a low GDP per capita.")

[⬆️ Go to Context](#context)

### Dictionaries & Pandas

#### [Motivation for dictionaries](./02%20Dictionaries%20&%20Pandas/01_motivation_for_dictionaries.py)

- Use the `index()` method on countries to find the index of '`germany`'. Store this index as `ind_ger`.
- Use `ind_ger` to access the capital of Germany from the capitals list. Print it out.

  ```py
  # Definition of countries and capital
  countries = ['spain', 'france', 'germany', 'norway']
  capitals = ['madrid', 'paris', 'berlin', 'oslo']

  # Get index of 'germany': ind_ger


  # Use ind_ger to print out capital of Germany

  ```

[⬆️ Go to Context](#context)

#### [Create dictionary](./02%20Dictionaries%20&%20Pandas/02_create_dictionary.py)

- With the strings in `countries` and `capitals`, create a dictionary called europe with 4 `key:value` pairs. Beware of capitalization! Make sure you use lowercase characters everywhere.
- Print out europe to see if the result is what you expected.

  ```py
  # Definition of countries and capital
  countries = ['spain', 'france', 'germany', 'norway']
  capitals = ['madrid', 'paris', 'berlin', 'oslo']

  # From string in countries and capitals, create dictionary europe
  europe = {'spain':'madrid', ___, ___, ___ }

  # Print europe

  ```

[⬆️ Go to Context](#context)

#### [Access dictionary](./02%20Dictionaries%20&%20Pandas/03_access_dictionary.py)

- Check out which keys are in `europe` by calling the `keys()` method on `europe`. Print out the `result`.
- Print out the value that belongs to the key '`norway`'.

  ```py
  # Definition of dictionary
  europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

  # Print out the keys in europe


  # Print out value that belongs to key 'norway'

  ```

[⬆️ Go to Context](#context)

#### [Dictionary Manipulation (1)](./02%20Dictionaries%20&%20Pandas/04_dictionary_manipulation_1.py)

- Add the key '`italy`' with the value '`rome`' to `europe`.
- To assert that '`italy`' is now a key in `europe`, print out '`italy`' in `europe`.
- Add another `key:value` pair to `europe`: '`poland`' is the key, '`warsaw`' is the corresponding value.
- Print out `europe`.

  ```py
  # Definition of dictionary
  europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

  # Add italy to europe


  # Print out italy in europe


  # Add poland to europe


  # Print europe

  ```

[⬆️ Go to Context](#context)

#### [Dictionary Manipulation (2)](./02%20Dictionaries%20&%20Pandas/05_dictionary_manipulation_2.py)

- The capital of Germany is not '`bonn`'; it's '`berlin`'. Update its value.
- Australia is not in Europe, Austria is! Remove the key '`australia`' from europe.
- Print out europe to see if your cleaning work paid off.

  ```py
  # Definition of dictionary
  europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
            'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
            'australia':'vienna' }

  # Update capital of germany


  # Remove australia


  # Print europe

  ```

[⬆️ Go to Context](#context)

#### [Dictionariception](./02%20Dictionaries%20&%20Pandas/06_dictionariception.py)

- Use chained square brackets to select and print out the capital of France.
- Create a dictionary, named data, with the keys '`capital`' and '`population`'. Set them to '`rome`' and `59.83`, respectively.
- Add a new `key-value` pair to europe; the key is '`italy`' and the value is `data`, the dictionary you just built.

  ```py
  # Dictionary of dictionaries
  europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
            'france': { 'capital':'paris', 'population':66.03 },
            'germany': { 'capital':'berlin', 'population':80.62 },
            'norway': { 'capital':'oslo', 'population':5.084 } }


  # Print out the capital of France


  # Create sub-dictionary data


  # Add data to europe under key 'italy'


  # Print europe

  ```

[⬆️ Go to Context](#context)

#### [Dictionary to DataFrame (1)](./02%20Dictionaries%20&%20Pandas/07_dictionary_to_data_frame_1.py)

- Import `pandas` as `pd`.
- Use the pre-defined lists to create a dictionary called `my_dict`. There should be three key value pairs:
  - key '`country`' and value names.
  - key '`drives_right`' and value `dr`.
  - key '`cars_per_cap`' and value `cpc`.
  - Use `pd.DataFrame()` to turn your dict into a DataFrame called `cars`.
  - Print out `cars` and see how beautiful it is.

  ```py
  # Pre-defined lists
  names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
  dr =  [True, False, False, False, True, True, True]
  cpc = [809, 731, 588, 18, 200, 70, 45]

  # Import pandas as pd


  # Create dictionary my_dict with three key:value pairs: my_dict


  # Build a DataFrame cars from my_dict: cars


  # Print cars

  ```

[⬆️ Go to Context](#context)

#### [Dictionary to DataFrame (2)](./02%20Dictionaries%20&%20Pandas/08_dictionary_to_data_frame_2.py)

- Hit Run Code to see that, indeed, the row labels are not correctly set.
- Specify the row labels by setting `cars.index` equal to `row_labels`.
- Print out `cars` again and check if the row labels are correct this time.

  ```py
  import pandas as pd

  # Build cars DataFrame
  names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
  dr =  [True, False, False, False, True, True, True]
  cpc = [809, 731, 588, 18, 200, 70, 45]
  cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
  cars = pd.DataFrame(cars_dict)
  print(cars)

  # Definition of row_labels
  row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

  # Specify row labels of cars


  # Print cars again

  ```

[⬆️ Go to Context](#context)

#### [CSV to DataFrame (1)](./02%20Dictionaries%20&%20Pandas/09_csv_to_data_frame_1.py)

- To import CSV files you still need the `pandas` package: import it as `pd`.
- Use `pd.read_csv()` to import cars.csv data as a DataFrame. Store this DataFrame as cars.
- Print out cars. Does everything look OK?

  ```py
  # Import pandas as pd


  # Import the cars.csv data: cars


  # Print out cars

  ```

[⬆️ Go to Context](#context)

#### [CSV to DataFrame (2)](./02%20Dictionaries%20&%20Pandas/10_csv_to_data_frame_2.py)

- Run the code with Run Code and assert that the first column should actually be used as row labels.
- Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
- Has the printout of cars improved now?

  ```py
  # Import pandas as pd
  import pandas as pd

  # Fix import by including index_col
  cars = pd.read_csv('cars.csv')

  # Print out cars
  print(cars)
  ```

[⬆️ Go to Context](#context)

#### [Square Brackets (1)](./02%20Dictionaries%20&%20Pandas/11_square_brackets_1.py)

- Use single square brackets to print out the country column of `cars` as a `Pandas` Series.
- Use double square brackets to print out the country column of `cars` as a `Pandas` DataFrame.
- Use double square brackets to print out a DataFrame with both the country and `drives_right` columns of `cars`, in this order.

  ```py
  # Import cars data
  import pandas as pd
  cars = pd.read_csv('cars.csv', index_col = 0)

  # Print out country column as Pandas Series


  # Print out country column as Pandas DataFrame


  # Print out DataFrame with country and drives_right columns

  ```

[⬆️ Go to Context](#context)

#### [Square Brackets (2)](./02%20Dictionaries%20&%20Pandas/12_square_brackets_2.py)

- Select the first 3 observations from `cars` and print them out.
- Select the fourth, fifth and sixth observation, corresponding to row indexes 3, 4 and 5, and print them out.

  ```py
  # Import cars data
  import pandas as pd
  cars = pd.read_csv('cars.csv', index_col = 0)

  # Print out first 3 observations


  # Print out fourth, fifth and sixth observation

  ```

[⬆️ Go to Context](#context)

#### [loc and iloc (1)](./02%20Dictionaries%20&%20Pandas/13_loc_and_iloc_1.py)

- Use `loc` or `iloc` to select the observation corresponding to Japan as a Series. The label of this row is JPN, the index is `2`. Make sure to print the resulting Series.
- Use `loc` or `iloc` to select the observations for Australia and Egypt as a DataFrame. You can find out about the labels/indexes of these rows by inspecting `cars`. Make sure to print the resulting DataFrame.

  ```py
  # Import cars data
  import pandas as pd
  cars = pd.read_csv('cars.csv', index_col = 0)

  # Print out observation for Japan


  # Print out observations for Australia and Egypt

  ```

[⬆️ Go to Context](#context)

#### [loc and iloc (2)](./02%20Dictionaries%20&%20Pandas/14_loc_and_iloc_2.py)

- Print out the `drives_right` value of the row corresponding to Morocco (its row label is `MOR`)
- Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns `country` and `drives_right`.

  ```py
  # Import cars data
  import pandas as pd
  cars = pd.read_csv('cars.csv', index_col = 0)

  # Print out drives_right value of Morocco


  # Print sub-DataFrame

  ```

[⬆️ Go to Context](#context)

#### [loc and iloc (3)](./02%20Dictionaries%20&%20Pandas/15_loc_and_iloc_3.py)

- Print out the `drives_right` column as a Series using `loc` or `iloc`.
- Print out the `drives_right` column as a DataFrame using `loc` or `iloc`.
- Print out both the `cars_per_cap` and `drives_right` column as a DataFrame using `loc` or ilo`c.

  ```py
  # Import cars data
  import pandas as pd
  cars = pd.read_csv('cars.csv', index_col = 0)

  # Print out drives_right column as Series


  # Print out drives_right column as DataFrame


  # Print out cars_per_cap and drives_right as DataFrame


  ```

[⬆️ Go to Context](#context)

### Logic, Control Flow and Filtering

#### [Equality](./03%20Logic,%20Control%20Flow%20and%20Filtering/01_equality.py)

- Write code to see if `True` equals `False`.
- Write Python code to check if ` -5 * 15 is` not equal to `75`.
- Ask Python whether the strings "`pyscript`" and "`PyScript`" are equal.
- What happens if you compare booleans and integers? Write code to see if `True` and `1` are equal.

  ```py
  # Comparison of booleans


  # Comparison of integers


  # Comparison of strings


  # Compare a boolean with an integer

  ```

[⬆️ Go to Context](#context)

#### [Greater and less than](./03%20Logic,%20Control%20Flow%20and%20Filtering/02_greater_and_less_than.py)

- Write Python expressions, wrapped in a `print()` function, to check whether:
  - `x` is greater than or equal to ` -10`. x has already been defined for you.
  - "`test`" is less than or equal to `y`. `y has already been defined for you.
  - `True` is greater than `False`.

  ```py
  # Comparison of integers
  x = -3 * 6


  # Comparison of strings
  y = "test"


  # Comparison of booleans

  ```

[⬆️ Go to Context](#context)

#### [Compare arrays](./03%20Logic,%20Control%20Flow%20and%20Filtering/03_compare_arrays.py)

- Using comparison operators, generate boolean arrays that answer the following questions:
  - Which areas in `my_house` are greater than or equal to `18`?
  - You can also compare two NumPy arrays element-wise. Which areas in `my_house` are smaller than the ones in `your_house`?
  - Make sure to wrap both commands in a `print()` statement so that you can inspect the output!

  ```py
  # Create arrays
  import numpy as np
  my_house = np.array([18.0, 20.0, 10.75, 9.50])
  your_house = np.array([14.0, 24.0, 14.25, 9.0])

  # my_house greater than or equal to 18


  # my_house less than your_house

  ```

[⬆️ Go to Context](#context)

#### [and, or, not (1)](./03%20Logic,%20Control%20Flow%20and%20Filtering/04_and_or_not_1.py)

- Write Python expressions, wrapped in a print() function, to check whether:
  - `my_kitchen` is bigger than `10` and smaller than `18`.
  - `my_kitchen` is smaller than `14` or bigger than `17`.
  - double the area of `my_kitchen` is smaller than triple the area of `your_kitchen`.

  ```py
  # Define variables
  my_kitchen = 18.0
  your_kitchen = 14.0

  # my_kitchen bigger than 10 and smaller than 18?


  # my_kitchen smaller than 14 or bigger than 17?


  # Double my_kitchen smaller than triple your_kitchen?

  ```

[⬆️ Go to Context](#context)

#### and, or, not (2)

- To see if you completely understood the boolean operators, have a look at the following piece of Python code:

  ```py
  x = 8
  y = 9
  not(not(x < 3) and not(y > 14 or y > 10))
  ```

- What will the result be if you execute these three commands?

  *NB: Notice that not has a higher priority than and and or, it is executed first.*

  - [ ] True
  - [ ] False
  - [ ] Running these commands will result in an error.

  > [Answer](# "False")

[⬆️ Go to Context](#context)

#### [Boolean operators with NumPy](./03%20Logic,%20Control%20Flow%20and%20Filtering/05_boolean_operators_with_numpy.py)

- Generate boolean arrays that answer the following questions:
  - Which areas in `my_house` are greater than `18.5` or smaller than `10`?
  - Which areas are smaller than 11 in both `my_house` and `your_house`? Make sure to wrap both commands in `print()` statement, so that you can inspect the output.

  ```py
  # Create arrays
  import numpy as np
  my_house = np.array([18.0, 20.0, 10.75, 9.50])
  your_house = np.array([14.0, 24.0, 14.25, 9.0])

  # my_house greater than 18.5 or smaller than 10


  # Both my_house and your_house smaller than 11

  ```

[⬆️ Go to Context](#context)

#### Warmup

- To experiment with if and else a bit, have a look at this code sample:

  ```py
  area = 10.0
  if(area < 9) :
      print("small")
  elif(area < 12) :
      print("medium")
  else :
      print("large")
  ```

  What will the output be if you run this piece of code?

  - [ ] small
  - [ ] medium
  - [ ] large
  - [ ] The syntax is incorrect; this code will produce an error.

  > [Answer](# "medium")

[⬆️ Go to Context](#context)

#### [if](./03%20Logic,%20Control%20Flow%20and%20Filtering/06_if.py)

- Examine the if statement that prints out "`looking around in the kitchen.`" if room equals "`kit`".
- Write another if statement that prints out "`big place!`" if area is greater than `15`.

```py
# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area

```

[⬆️ Go to Context](#context)

#### [Add else](./03%20Logic,%20Control%20Flow%20and%20Filtering/01_equality.py)

- Add an else statement to the second control structure so that "`pretty small.`" is printed out if `area > 15` evaluates to `False`.

  ```py
  # Define variables
  room = "kit"
  area = 14.0

  # if-else construct for room
  if room == "kit" :
      print("looking around in the kitchen.")
  else :
      print("looking around elsewhere.")

  # if-else construct for area
  if area > 15 :
      print("big place!")
  ```

[⬆️ Go to Context](#context)

#### [Customize further: elif](./03%20Logic,%20Control%20Flow%20and%20Filtering/08_customize_further_elif.py)

- Add an `elif` to the second control structure such that "`medium size, nice!`" is printed out if `area` is greater than `10`.

  ```py
  # Define variables
  room = "bed"
  area = 14.0

  # if-elif-else construct for room
  if room == "kit" :
      print("looking around in the kitchen.")
  elif room == "bed":
      print("looking around in the bedroom.")
  else :
      print("looking around elsewhere.")

  # if-elif-else construct for area
  if area > 15 :
      print("big place!")
  else :
      print("pretty small.")
  ```

[⬆️ Go to Context](#context)

#### [Driving right (1)](./03%20Logic,%20Control%20Flow%20and%20Filtering/09_driving_right_1.py)

- Extract the drives_right column as a Pandas Series and store it as dr.
- Use dr, a boolean Series, to subset the cars DataFrame. Store the resulting selection in sel.
- Print sel, and assert that drives_right is True for all observations.

  ```py
  # Import cars data
  import pandas as pd
  cars = pd.read_csv('cars.csv', index_col = 0)

  # Extract drives_right column as Series: dr


  # Use dr to subset cars: sel


  # Print sel

  ```

[⬆️ Go to Context](#context)

#### [Driving right (2)](./03%20Logic,%20Control%20Flow%20and%20Filtering/10_driving_right_2.py)

- Convert the code to a one-liner that calculates the variable `sel` as before.

  ```py
  # Import cars data
  import pandas as pd
  cars = pd.read_csv('cars.csv', index_col = 0)

  # Convert code to a one-liner
  dr = cars['drives_right']
  sel = cars[dr]

  # Print sel
  print(sel)
  ```

[⬆️ Go to Context](#context)

#### [Cars per capita (1)](./03%20Logic,%20Control%20Flow%20and%20Filtering/11_cars_per_capita_1.py)

- Select the `cars_per_cap` column from `cars` as a Pandas Series and store it as `cpc`.
- Use `cpc` in combination with a comparison operator and `500`. You want to end up with a boolean Series that's True if the corresponding country has a `cars_per_cap` of more than `500` and `False` otherwise. Store this boolean Series as `many_cars`.
- Use `many_cars` to subset `cars`, similar to what you did before. Store the result as `car_maniac`.
- Print out `car_maniac` to see if you got it right.

  ```py
  # Import cars data
  import pandas as pd
  cars = pd.read_csv('cars.csv', index_col = 0)

  # Create car_maniac: observations that have a cars_per_cap over 500




  # Print car_maniac

  ```

[⬆️ Go to Context](#context)

#### [Cars per capita (2)](./03%20Logic,%20Control%20Flow%20and%20Filtering/12_cars_per_capita_2.py)

- Use the code sample provided to create a `DataFrame` medium, that includes all the observations of `cars` that have a `cars_per_cap` between `100` and `500`.
- Print out `medium`.

  ```py
  # Import cars data
  import pandas as pd
  cars = pd.read_csv('cars.csv', index_col = 0)

  # Import numpy, you'll need this
  import numpy as np

  # Create medium: observations with cars_per_cap between 100 and 500




  # Print medium

  ```

[⬆️ Go to Context](#context)

