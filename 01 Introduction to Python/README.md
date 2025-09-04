<div align="center">
<h1>Introduction to Python</h1>
</div>

# **Context**
- [**Context**](#context)
  - [**Introduction to Python**](#introduction-to-python)
    - [Python Basics](#python-basics)
      - [Your first Python code](#your-first-python-code)
      - [Python as a calculator](#python-as-a-calculator)
      - [Variable Assignment](#variable-assignment)
      - [Calculations with variables](#calculations-with-variables)
      - [Other variable types](#other-variable-types)
      - [Operations with other types](#operations-with-other-types)
    - [Python Lists](#python-lists)
      - [Python Data Types](#python-data-types)
      - [Create a list](#create-a-list)
      - [Create lists with different types](#create-lists-with-different-types)
      - [List of lists](#list-of-lists)
      - [Subset and conquer](#subset-and-conquer)
      - [Slicing and dicing](#slicing-and-dicing)
      - [Subsetting lists of lists](#subsetting-lists-of-lists)
      - [Replace list elements](#replace-list-elements)
      - [Extend a list](#extend-a-list)
      - [Delete list elements](#delete-list-elements)
      - [Inner workings of lists](#inner-workings-of-lists)
    - [Functions and Packages](#functions-and-packages)
      - [Familiar functions](#familiar-functions)
      - [Help](#help)
      - [Multiple arguments](#multiple-arguments)
      - [String Methods](#string-methods)
      - [List Methods](#list-methods)
      - [List Methods (2)](#list-methods-2)
      - [Import package](#import-package)
      - [Selective import](#selective-import)
      - [Different ways of importing](#different-ways-of-importing)
    - [NumPy](#numpy)
      - [Your First NumPy Array](#your-first-numpy-array)
      - [Baseball players' height](#baseball-players-height)
      - [NumPy Side Effects](#numpy-side-effects)
      - [Subsetting NumPy Arrays](#subsetting-numpy-arrays)
      - [Your First 2D NumPy Array](#your-first-2d-numpy-array)
      - [Baseball data in 2D form](#baseball-data-in-2d-form)
      - [Subsetting 2D NumPy Arrays](#subsetting-2d-numpy-arrays)
      - [2D Arithmetic](#2d-arithmetic)
      - [Average versus median](#average-versus-median)
      - [Explore the baseball data](#explore-the-baseball-data)

## **[Introduction to Python](https://www.datacamp.com/courses/intro-to-python-for-data-science)**

- Course Instructor: [Hugo Bowne-Anderson](https://www.linkedin.com/in/hugo-bowne-anderson-045939a5/)
- Collaborators
  - [Vincent Vankrunkelsven](https://www.linkedin.com/in/vincent-vankrunkelsven-130248103/)
  - [Filip Schouwenaars](https://www.linkedin.com/in/fschouw/)
- Datasets
  - [MLB (baseball)](https://assets.datacamp.com/production/repositories/288/datasets/e5d60ff535f86d27609312f9e41c35a1d737ddc0/baseball.csv)
  - [FIFA (soccer)](https://assets.datacamp.com/production/repositories/288/datasets/026a5211b906ac118a09b1a0dbf7df48faafb379/fifa.csv)

### [Python Basics](./01%20Python%20Basics/)

#### [Your first Python code](./01%20Python%20Basics/01_your_first_python_code.py)

- Hit the run code button to see the output of `print(5 / 8)`.

  ```py
  # Hit run code to see the output!
  print(5 / 8)
  ```

[⬆️ Go to Context](#context)

#### [Python as a calculator](./01%20Python%20Basics/02_python_as_a_calculator.py)

- Print the result of subtracting `5` from `5` under `# Subtraction` using `print()`.
- Print the result of multiplying `3` by `5` under `# Multiplication`.

  ```py
  # Addition and division
  print(4 + 5)
  print(10 / 2)

  # Subtraction
  print()

  # Multiplication
  ```

[⬆️ Go to Context](#context)

#### [Variable Assignment](./01%20Python%20Basics/03_variable_assignment.py)

- Create a variable `savings` with the value of `100`.
- Check out this variable by typing `print(savings)` in the script.

  ```py
  # Create a variable savings
  ____

  # Print out savings
  ____
  ```

[⬆️ Go to Context](#context)

#### [Calculations with variables](./01%20Python%20Basics/04_calculations_with_variables.py)

- Create a variable `monthly_savings`, equal to `10` and `num_months`, equal to `4`.
- Multiply monthly_savings by `num_months` and assign it to `new_savings`.
- Print the value of `new_savings`.

  ```py
  # Create the variables monthly_savings and num_months



  # Multiply monthly_savings and num_months
  new_savings = ____

  # Print new_savings

  ```

[⬆️ Go to Context](#context)

#### [Other variable types](./01%20Python%20Basics/05_other_variable_types.py)

- Create a new `float`, `half`, with the value `0.5`.
- Create a new `string`, `intro`, with the value `"Hello! How are you?"`.
- Create a new `boolean`, `is_good`, with the value `True`.

  ```py
  # Create a variable half


  # Create a variable intro


  # Create a variable is_good

  ```

[⬆️ Go to Context](#context)

#### Operations with other types

- **[Task 01](./01%20Python%20Basics/06_operations_with_other_types_01.py)**: Add `savings` and `new_savings` and assign it to `total_savings`. Use `type()` to print the resulting type of `total_savings`.

  ```py
  savings = 100
  new_savings = 40

  # Calculate total_savings using savings and new_savings
  total_savings=savings+new_savings
  print(total_savings)

  # Print the type of total_savings
  print(type(total_savings))
  ```

- **[Task 02](./01%20Python%20Basics/06_operations_with_other_types_02.py)**: Calculate the sum of `intro` and `intro` and assign the result to `doubleintro`. Print out `doubleintro`. Did you expect this?

  ```py
  intro = "Hello! How are you?"

  # Assign sum of intro and intro to doubleintro
  doubleintro=intro+intro

  # Print out doubleintro
  print(doubleintro)
  ```

[⬆️ Go to Context](#context)

### [Python Lists](./02%20Python%20List/)

#### Python Data Types

- `float` - real numbers
- `int` - integer numbers
- `str` - string, text
- `bool` - True, False.

---

- Problem
  - Data Science: many data points
- Solution
  - Python List

[⬆️ Go to Context](#context)

#### [Create a list](./02%20Python%20List/01_create_a_list.py)

- Create a list, `areas`, that contains the area of the hallway (`hall`), kitchen (`kit`), living room (`liv`), bedroom (`bed`) and bathroom (`bath`), in this order. Use the predefined variables.
- Print `areas` with the `print()` function.

  ```py
  hall = 11.25
  kit = 18.0
  liv = 20.0
  bed = 10.75
  bath = 9.50

  # Create list areas


  # Print areas

  ```

[⬆️ Go to Context](#context)

#### [Create lists with different types](./02%20Python%20List/02_create_lists_with_different_types.py)

- Finish the code that creates the `areas` list. Build the list so that the list first contains the name of each room as a string and then its area. In other words, add the strings `"hallway"`, `"kitchen"` and `"bedroom"` at the appropriate locations.
- Print `areas` again; is the printout more informative this time?

  ```py
  hall = 11.25
  kit = 18.0
  liv = 20.0
  bed = 10.75
  bath = 9.50

  # Adapt list areas
  areas = [____, hall, ____, kit, "living room", liv, ____, bed, "bathroom", bath]

  # Print areas
  ____
  ```

[⬆️ Go to Context](#context)

#### [List of lists](./02%20Python%20List/03_list_of_lists.py)

- Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
- Print out `house`; does this way of structuring your data make more sense?

  ```py
  hall = 11.25
  kit = 18.0
  liv = 20.0
  bed = 10.75
  bath = 9.50

  # House information as list of lists
  house = [["hallway", hall],
          ["kitchen", kit],
          ["living room", liv],
          ____,
          ____]

  # Print out house
  ____
  ```

[⬆️ Go to Context](#context)

#### [Subset and conquer](./02%20Python%20List/04_subset_and_conquer.py)

- Print out the second element from the `areas` list (it has the value `11.25`).
- Subset and print out the last element of `areas`, being `9.50`. Using a negative index makes sense here!
- Select the number representing the area of the living room (`20.0`) and print it out.

  ```py
  # Create the areas list
  areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

  # Print out second element from areas
  print(areas[____])

  # Print out last element from areas
  print(areas[____])

  # Print out the area of the living room
  print(areas[____])
  ```

[⬆️ Go to Context](#context)

#### [Slicing and dicing](./02%20Python%20List/05_slicing_and_dicing.py)

- Use slicing to create a list, `downstairs`, that contains the first 6 elements of areas.
- Create `upstairs`, as the last `4` elements of `areas`. This time, simplify the slicing by omitting the `end` index.
- Print both `downstairs` and upstairs using `print()`.

  ```py
  # Create the areas list
  areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

  # Use slicing to create downstairs
  downstairs = areas[____]

  # Use slicing to create upstairs
  upstairs = areas[____]

  # Print out downstairs and upstairs
  ____
  ____
  ```

[⬆️ Go to Context](#context)

#### [Subsetting lists of lists](./02%20Python%20List/06_subsetting_lists_of_lists.py)

- Subset the house list to get the float 9.5.

  ```py
  house = [["hallway", 11.25],
          ["kitchen", 18.0],
          ["living room", 20.0],
          ["bedroom", 10.75],
          ["bathroom", 9.50]]

  # Subset the house list
  house___
  ```

[⬆️ Go to Context](#context)

#### [Replace list elements](./02%20Python%20List/07_replace_list_elements.py)

- Update the area of the `bathroom` to be `10.50` square meters instead of `9.50` using negative indexing.
- Make the areas list more trendy! Change "`living room`" to "`chill zone`".Don't use negative indexing this time.

  ```py
  # Create the areas list
  areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

  # Correct the bathroom area


  # Change "living room" to "chill zone"

  ```

[⬆️ Go to Context](#context)

#### [Extend a list](./02%20Python%20List/08_extend_a_list.py)

- Use the `'+'` operator to paste the list `["poolhouse", 24.5]` to the end of the areas list. Store the resulting list as areas_1.
- Further extend `areas_1` by adding data on your `garage`. Add the string `"garage"` and float `15.45`. Name the resulting list `areas_2`.

  ```py
  # Create the areas list and make some changes
  areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
          "bedroom", 10.75, "bathroom", 10.50]

  # Add poolhouse data to areas, new list is areas_1
  areas_1 = ____

  # Add garage data to areas_1, new list is areas_2
  areas_2 = ____
  ```

[⬆️ Go to Context](#context)

#### [Delete list elements](./02%20Python%20List/09_delete_list_elements.py)

- Delete the string and float for the `"poolhouse"` from your `areas` list.
- Print the updated `areas` list.

  ```py
  areas = ["hallway", 11.25, "kitchen", 18.0,
          "chill zone", 20.0, "bedroom", 10.75,
          "bathroom", 10.50, "poolhouse", 24.5,
          "garage", 15.45]

  # Delete the poolhouse items from the list


  # Print the updated list

  ```

[⬆️ Go to Context](#context)

#### Inner workings of lists

- Change the second command, that creates the variable `areas_copy`, such that `areas_copy` is an explicit copy of `areas`. After your edit, changes made to `areas_copy` shouldn't affect `areas`. Submit the answer to check this.

  ```py
  # Create list areas
  areas = [11.25, 18.0, 20.0, 10.75, 9.50]

  # Change this command
  areas_copy = areas

  # Change areas_copy
  areas_copy[0] = 5.0

  # Print areas
  print(areas)
  ```

[⬆️ Go to Context](#context)

### [Functions and Packages](./03%20Functions%20and%20Packages/)

#### [Familiar functions](./03%20Functions%20and%20Packages/01_familiar_functions.py)

- Use `print()` in combination with `type()` to print out the type of `var1`.
- Use `len()` to get the length of the list `var1`. Wrap it in a `print()` call to directly print it out.
- Use `int()` to convert `var2` to an `integer`. Store the output as `out2`.

  ```py
  # Create variables var1 and var2
  var1 = [1, 2, 3, 4]
  var2 = True

  # Print out type of var1
  ____

  # Print out length of var1
  ____

  # Convert var2 to an integer: out2
  out2 = ____
  ```

[⬆️ Go to Context](#context)

#### Help

- Which of the following statements is true?
  - [ ] `pow()` takes three arguments: `base`, `exp`, and `mod`. Without `mod`, the function will return an error.
  - [ ] `pow()` takes three required arguments: `base`, `exp`, and `None`.
  - [ ] `pow()` requires `base` and `exp` arguments; `mod` is optional.
  - [ ] `pow()` takes two arguments: `exp` and `mod`. Missing `exp` results in an error.

  > [Answer](# "pow() requires base and exp arguments; mod is optional.")

[⬆️ Go to Context](#context)

#### [Multiple arguments](./03%20Functions%20and%20Packages/02_multiple_arguments.py)

- Use `'+'` to merge the contents of first and second into a new list: `full`.
- Call `sorted()` and on `full` and specify the reverse argument to be True. Save the sorted `list` as `full_sorted`.
- Finish off by printing out `full_sorted`.

  ```py
  # Create lists first and second
  first = [11.25, 18.0, 20.0]
  second = [10.75, 9.50]

  # Paste together first and second: full
  full = ____ + ____

  # Sort full in descending order: full_sorted
  full_sorted = ____

  # Print out full_sorted
  ____
  ```

[⬆️ Go to Context](#context)

#### [String Methods](./03%20Functions%20and%20Packages/03_string_methods.py)

- Use the `.upper()` method on place and store the result in `place_up`. Use the syntax for calling methods that you learned in the previous video.
- Print out place and `place_up`. Did both change?
- Print out the number of `o`'s on the variable place by calling .`count()` on place and passing the letter `'o'` as an input to the method. We're talking about the variable place, not the word `"place"`!

  ```py
  # string to experiment with: place
  place = "poolhouse"

  # Use upper() on place
  place_up =

  # Print out place and place_up



  # Print out the number of o's in place

  ```

[⬆️ Go to Context](#context)

#### [List Methods](./03%20Functions%20and%20Packages/04_list_methods.py)

- Use the `.index()` method to get the index of the element in areas that is equal to `20.0`. Print out this index.
- Call `.count()` on areas to find out how many times `9.50` appears in the list. Again, simply print out this number.

  ```py
  # Create list areas
  areas = [11.25, 18.0, 20.0, 10.75, 9.50]

  # Print out the index of the element 20.0


  # Print out how often 9.50 appears in areas

  ```

[⬆️ Go to Context](#context)

#### [List Methods (2)](./03%20Functions%20and%20Packages/05_list_methods_02.py)

- Use `.append()` twice to add the size of the `poolhouse` and the garage again: `24.5` and `15.45`, respectively. Make sure to add them in this order.
- Print out `areas`
- Use the `.reverse()` method to `reverse` the order of the elements in `areas`.
- Print out `areas` once more.

  ```py
  # Create list areas
  areas = [11.25, 18.0, 20.0, 10.75, 9.50]

  # Use append twice to add poolhouse and garage size



  # Print out areas


  # Reverse the orders of the elements in areas


  # Print out areas

  ```

[⬆️ Go to Context](#context)

#### [Import package](./03%20Functions%20and%20Packages/06_import_package.py)

- Import the `math` package.
- Use `math.pi` to calculate the `circumference` of the `circle` and store it in `C`.
- Use `math.pi` to calculate the area of the circle and store it in `A`.

  ```py
  # Import the math package
  import ____

  # Calculate C
  C = 2 * 0.43 * ____

  # Calculate A
  A = ____ * 0.43 ** 2

  print("Circumference: " + str(C))
  print("Area: " + str(A))
  ```

[⬆️ Go to Context](#context)

#### [Selective import](./03%20Functions%20and%20Packages/07_selective_import.py)

- Perform a selective import from the math package where you only import the `pi` function.
- Use `pi` to calculate the `circumference` of the `circle` and store it in `C`.
- Use `pi` to calculate the `area` of the `circle` and store it in `A`.

  ```py
  # Import pi function of math package
  from math import ____

  # Calculate C
  C = 2 * 0.43 * ____

  # Calculate A
  A = ____ * 0.43 ** 2

  print("Circumference: " + str(C))
  print("Area: " + str(A))
  ```

[⬆️ Go to Context](#context)

#### Different ways of importing

- Suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package. You want to be able to use this function as follows:

  ```py
  my_inv([[1,2], [3,4]])
  ```

- Which import statement will you need in order to run the above code without an error?
  - [ ] import `scipy`
  - [ ] import `scipy.linalg`
  - [ ] from `scipy.linalg` import `my_inv`
  - [ ] from `scipy.linalg` import `inv` as `my_inv`

  > [Answer](# "from scipy.linalg import inv as my_inv")

[⬆️ Go to Context](#context)

### NumPy

#### [Your First NumPy Array](./04%20NumPy/01_your_first_num_py_array.py)

- Import the `numpy` package as `np`, so that you can refer to `numpy` with `np`.
- Use `np.array()` to create a `numpy` array from `baseball`. Name this array `np_baseball`.
- Print out the type of `np_baseball` to check that you got it right.

  ```py
  # Import the numpy package as np


  baseball = [180, 215, 210, 210, 188, 176, 209, 200]

  # Create a numpy array from baseball: np_baseball


  # Print out type of np_baseball

  ```

[⬆️ Go to Context](#context)

#### [Baseball players' height](./04%20NumPy/02_baseball_players_height.py)

- Create a `numpy` array from `height_in`. Name this new array `np_height_in`.
- Print `np_height_in`.
- Multiply `np_height_in` with `0.0254` to convert all height measurements from inches to meters. Store the new values in a new array, `np_height_m`.
- Print out `np_height_m` and check if the output makes sense.

  ```py
  # Import numpy
  import numpy as np

  # Create a numpy array from height_in: np_height_in


  # Print out np_height_in


  # Convert np_height_in to m: np_height_m


  # Print np_height_m

  ```

[⬆️ Go to Context](#context)

#### NumPy Side Effects

- `numpy` is great for doing vector arithmetic. If you compare its functionality with regular Python lists, however, some things have changed.
- First of all, numpy arrays cannot contain elements with different types. Second, the typical arithmetic operators, such as +, -, * and / have a different meaning for regular Python lists and numpy arrays.
- Some lines of code have been provided for you. Try these out and select the one that would match this:

  ```py
  np.array([True, 1, 2]) + np.array([3, 4, False])
  ```

- The `numpy` package is already imported as `np`.

  - [ ] `np.array([True, 1, 2, 3, 4, False])`

  - [ ] `np.array([4, 3, 0]) + np.array([0, 2, 2])`

  - [ ] `np.array([1, 1, 2]) + np.array([3, 4, -1])`

  - [ ] `np.array([0, 1, 2, 3, 4, 5])`

  > [Answer](# "np.array([4, 3, 0]) + np.array([0, 2, 2])")

[⬆️ Go to Context](#context)

#### [Subsetting NumPy Arrays](./04%20NumPy/03_subsetting_num_py_arrays.py)

- Subset `np_weight_lb` by printing out the element at index 50.
- Print out a sub-array of `np_height_in` that contains the elements at index 100 up to and including index `110`.

  ```py
  import numpy as np

  np_weight_lb = np.array(weight_lb)
  np_height_in = np.array(height_in)

  # Print out the weight at index 50


  # Print out sub-array of np_height_in: index 100 up to and including index 110

  ```

[⬆️ Go to Context](#context)

#### [Your First 2D NumPy Array](./04%20NumPy/04_your_first_2_d_num_py_array.py)

- Use `np.array()` to create a 2D `numpy` array from `baseball`. Name it `np_baseball`.
- Print out the type of `np_baseball`.
- Print out the shape attribute of `np_baseball`. Use `np_baseball`.shape.

  ```py
  import numpy as np

  baseball = [[180, 78.4],
              [215, 102.7],
              [210, 98.5],
              [188, 75.2]]

  # Create a 2D numpy array from baseball: np_baseball


  # Print out the type of np_baseball


  # Print out the shape of np_baseball

  ```

[⬆️ Go to Context](#context)

#### [Baseball data in 2D form](./04%20NumPy/05_baseball_data_in_2_d_form.py)

- Use `np.array()` to create a 2D numpy array from baseball. Name it `np_baseball`.
- Print out the shape attribute of `np_baseball`.

  ```py
  import numpy as np

  # Create a 2D numpy array from baseball: np_baseball
  np_baseball =

  # Print out the shape of np_baseball

  ```

[⬆️ Go to Context](#context)

#### [Subsetting 2D NumPy Arrays](./04%20NumPy/06_subsetting_2_d_num_py_arrays.py)

- Print out the `50th` row of `np_baseball`.
- Make a new variable, `np_weight_lb`, containing the entire second column of np_baseball.
- Select the height (first column) of the `124th` baseball player in `np_baseball` and print it out.

  ```py
  import numpy as np

  np_baseball = np.array(baseball)

  # Print out the 50th row of np_baseball


  # Select the entire second column of np_baseball: np_weight_lb


  # Print out height of 124th player

  ```

[⬆️ Go to Context](#context)

#### [2D Arithmetic](./04%20NumPy/07_2_d_arithmetic.py)

- You managed to get hold of the changes in `height`, `weight` and `age` of all baseball players. It is available as a 2D numpy array, updated. Add `np_baseball` and updated and print out the result.
- You want to convert the units of height and weight to metric (meters and kilograms, respectively). As a first step, create a numpy array with three values: `0.0254`, `0.453592` and `1`. Name this array conversion.
- Multiply `np_baseball` with conversion and print out the result.

  ```py
  import numpy as np

  np_baseball = np.array(baseball)

  # Print out addition of np_baseball and updated


  # Create numpy array: conversion


  # Print out product of np_baseball and conversion

  ```

[⬆️ Go to Context](#context)

#### [Average versus median](./04%20NumPy/08_average_versus_median.py)

- Create numpy array `np_height_in` that is equal to first column of `np_baseball`.
- Print out the mean of `np_height_in`.
- Print out the median of `np_height_in`.

  ```py
  import numpy as np

  # Create np_height_in from np_baseball


  # Print out the mean of np_height_in


  # Print out the median of np_height_in

  ```

[⬆️ Go to Context](#context)

#### [Explore the baseball data](./04%20NumPy/09_explore_the_baseball_data.py)

- The code to print out the mean height is already included. Complete the code for the median height.
- Use `np.std()` on the first column of `np_baseball` to calculate `stddev`.
- Do big players tend to be heavier? Use `np.corrcoef()` to store the correlation between the first and second column of `np_baseball` in `corr`.

  ```py
  avg = np.mean(np_baseball[:,0])
  print("Average: " + str(avg))

  # Print median height
  med = ____
  print("Median: " + str(med))

  # Print out the standard deviation on height
  stddev = ____
  print("Standard Deviation: " + str(stddev))

  # Print out correlation between first and second column
  corr = ____
  print("Correlation: " + str(corr))
  ```

[⬆️ Go to Context](#context)
