# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numb ers
def subtract(x, y):
    return x - y

# This function multiples two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operations :")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1 / 2 / 3 / 4) : ")

    # Check if choice is one of the four option
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number : "))
            num2 = float(input("Enter the second number : "))
        except ValueError:
            print("Invalid input, please enter the number correctly!")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        #   Check if user want another calculation
        #   Break the while if user choose no

        next_calculation = input("Do you want another calculation ? (yes/no) : ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input!")