# add two numbers
def add(x, y):
    return x + y

# subtract two numbers
def subtract(x, y):
    return x - y

# multiply two numbers
def multiply(x, y):
    return x * y

# divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# user to select an operation
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

# user to input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))



if choice == '1':
    result = add(num1, num2)
    operation = "+"
elif choice == '2':
    result = subtract(num1, num2)
    operation = "-"
elif choice == '3':
    result = multiply(num1, num2)
    operation = "*"
elif choice == '4':
    result = divide(num1, num2)
    operation = "/"
else:
    print("Invalid choice")
    exit()

# Display the result
print(f"{num1} {operation} {num2} = {result}")
