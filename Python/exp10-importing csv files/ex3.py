import pandas as pd

# Load the CSV file
nifty = pd.read_csv(r"F:\pandas\Toyota.csv")

# Check the shape of the DataFrame (rows and columns)
print("Shape of the DataFrame:", nifty.shape)

# Get the index (row labels) of the DataFrame
print("Index of the DataFrame:", nifty.index)

# Get the column names of the DataFrame
print("Columns in the DataFrame:", nifty.columns)
