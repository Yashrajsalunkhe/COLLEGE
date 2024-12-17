import numpy as np
import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({
    "Date": pd.date_range(start="2021-10-01", periods=10, freq="D"),
    "Item": [1014] * 10,  # Repeat 1014 for all rows
    "Measure_1": np.random.randint(1, 10, size=10),  # Random integers between 1 and 10
    "Measure_2": np.random.random(10).round(2),  # Random floats rounded to 2 decimals
    "Measure_3": np.random.random(10).round(2),  # Another column of random floats
    "Measure_4": np.random.randn(10),  # Random numbers from a normal distribution
})

# Print the DataFrame
print(df)
