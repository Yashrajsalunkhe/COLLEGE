# Open the file 'text.txt' in write mode
with open("text.txt", 'w', encoding='utf-8') as f:
    f.write("my first line \n")
    f.write("this file \n")
    f.write("contain three lines\n")

# Check if the file is created and print its content
with open("text.txt", 'r', encoding='utf-8') as f:
    content = f.read()

# Print the content of the file to verify the data written
print(content)
