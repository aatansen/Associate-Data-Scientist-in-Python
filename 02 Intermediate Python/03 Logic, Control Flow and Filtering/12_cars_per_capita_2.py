# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np
cpc = cars['cars_per_cap']
# Create medium: observations with cars_per_cap between 100 and 500
between=np.logical_and(100<cpc,cpc<500)
medium = cars[between]

# Print medium
print(medium)