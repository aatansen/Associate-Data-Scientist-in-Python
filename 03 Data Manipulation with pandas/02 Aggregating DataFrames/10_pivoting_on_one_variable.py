#1
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales",index="type", aggfunc=["mean"]) # here aggfunc not required as by default it is mean

# Print mean_sales_by_type
print(mean_sales_by_type)

#2
# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales",index="type",aggfunc=["mean","median"])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

#3
# Pivot for mean weekly_sales by store type and holiday
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales",index="type",columns="is_holiday")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)