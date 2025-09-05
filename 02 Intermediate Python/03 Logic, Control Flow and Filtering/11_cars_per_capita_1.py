# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

cpc = cars['cars_per_cap']
# Create car_maniac: observations that have a cars_per_cap over 500
many_cars = cpc>500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)