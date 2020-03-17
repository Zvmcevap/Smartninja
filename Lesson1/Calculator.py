# Variables

num_one = float(input("Enter the first number: "))
operation = input("Enter +, -, * or /: ")
num_two = float(input("Enter the second number: "))

# Lets calculate

if operation == "+":
    print(num_one + num_two)

elif operation == "-":
    print(num_one - num_two)

elif operation == "*":
    print(num_one * num_two)

elif operation == "/":
    print(num_one / num_two)

else:print("Your math is shit")
