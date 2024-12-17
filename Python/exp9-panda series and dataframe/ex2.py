import pandas as pd

# List and index
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

# Dictionary for creating a series
dict_data = { 1: 'Test_Value1', 2: 'Test_Value2', 3: 'Test_Value3' }

# Creating Pandas Series with default index
pd_series_default_index = pd.Series(List)
print("Pandas Series with default index:\n", pd_series_default_index)

# Creating Pandas Series with manipulated index
pd_series_manipulated_index = pd.Series(List, index=index)
print("Pandas Series with manipulated index:\n", pd_series_manipulated_index)

# Creating Pandas Series with manipulated index and changed data type
pd_series_manipulated_data_type = pd.Series(List, dtype=str)
print("Pandas Series with manipulated data type:\n", pd_series_manipulated_data_type)

# Print type of first element
print("Print type of first element:\n", type(pd_series_manipulated_data_type[0]))

# Creating Pandas Series from dictionary
pd_series_dict = pd.Series(dict_data)
print("Pandas Series with dictionary type:\n", pd_series_dict)

# Accessing an element from the Pandas Series created from dictionary
print("Pandas Series with dictionary type:\n", pd_series_dict[3])
