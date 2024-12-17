import pandas as pd

# Ensure the file path uses proper forward slashes or double backslashes
nifty = pd.read_csv("C:\Users\HP\Desktop\py\exp10-importing csv files\Toyota.csv")


# Display the first few rows of the dataset
print(nifty.head())
