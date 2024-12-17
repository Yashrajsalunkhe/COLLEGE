# Writing to the file 'app.log'
with open('app.log', 'w', encoding='utf-8') as f:
    # First line
    f.write("my first file\n")
    # Second line
    f.write("this file\n")
    # Third line
    f.write("contain three file\n")

# Reading from the file 'app.log'
with open('app.log', 'r', encoding='utf-8') as f:
    content = f.readlines()

# Printing each line from the file
for line in content:
    print(line)
