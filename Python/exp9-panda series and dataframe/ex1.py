import pandas as pd

# Create a list
Temp_List1 = [2, 4, 56, 7, 8, 8]

# Create an empty Series
pd_series = pd.Series([])
print("Created Empty Series:")
print(pd_series)

# Convert the list to a Pandas Series
pd_series = pd.Series(Temp_List1)
print("Print the entire series:")
print(pd_series)

# Print the first element of the Series
print("Print the first element of the Series:")
print(pd_series[0])
