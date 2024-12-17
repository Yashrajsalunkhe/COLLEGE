import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({
    "Name": ['JohnDoe', 'Mary Re', 'Harley Me'],
    "gender": [1, 2, 0],
    "age": [80, 38, 12],
    "height": [101.0, 173.5, 180.5],
    "weight": [62.3, 55.7, 80.0]
})

# Custom function to calculate the sum of numeric values in a row
def custom_sum(row):
    # Summing only numeric columns
    return row[['gender', 'age', 'height', 'weight']].sum()

# Applying the custom function row-wise and adding a new column 'D'
df['D'] = df.apply(custom_sum, axis=1)

# Displaying the DataFrame
print(df)
