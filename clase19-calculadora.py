def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        option = int(input("Enter choice (1,2,3,4,5): "))
        if option == 5:
            print("Exiting the calculator. Goodbye!")
            break
        if option in [1,2,3,4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if option == 1:
                print(f"{num1} + {num2} = {add(num1,num2)}")
            elif option == 2:
                print(f"{num1} - {num2} = {subtract(num1,num2)}")
            elif option == 3:
                print(f"{num1} * {num2} = {multiply(num1,num2)}")
            elif option == 4:
                print(f"{num1} / {num2} = {divide(num1,num2)}")
        else:
            print("Invalid input")


calculator()