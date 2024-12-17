num_string = "12"
num_integer = 23

print("Data Type of num_string before type conversion:", type(num_string))

# Converting num_string to an integer
num_string = int(num_string)
print("Data Type of num_string after type conversion:", type(num_string))

# Adding the converted num_string to num_integer
num_sum = num_integer + num_string
print("Sum:", num_sum)

# Displaying the data type of num_sum
print("Data type of num_sum:", type(num_sum))
