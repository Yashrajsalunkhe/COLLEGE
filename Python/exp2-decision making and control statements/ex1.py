a = input("Enter a number: ")
b = input("Enter another number: ")

# Convert inputs to integers for comparison
a = int(a)
b = int(b)

if a > b:
    print("First number is greater than second number")
elif a == b:
    print("Both numbers are equal")
else:
    print("Second number is greater than first number")
