import pandas as pd

# Assuming the CSV file exists and is valid
nifty = pd.read_csv(r"F:\pandas\Toyota.csv")

# Drop a column
nifty = nifty.drop("Price", axis=1)  # axis=1 means columns
print(nifty)
