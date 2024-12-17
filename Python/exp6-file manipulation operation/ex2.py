fob = open("app.log", "wb")

# Display file name
print("File name:", fob.name)

# Display state of the file (whether the file is closed or not)
print("File state:", fob.closed)

# Print the opening mode
print("Opening mode:", fob.mode)

# Close the file after operations
fob.close()
