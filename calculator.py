# calculator.py

#Function to add two numbers.
def add(a, b):
    return a + b

#Function to subtract the second number from the first.
def subtract(a, b):
    return a - b

#Function to multiply two numbers.
def multiply(a, b):
    return a * b

#Function to divide the first number by the second, handling division by zero.
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    else:
        return a / b
    
#Function to get a valid number from the user with input validation.
def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#Main function to run the calculator program.
def calculator():
    while True:
        print("\nSimple Calculator")
        print("-----------------")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("X. Exit")

        choice = input("Enter choice (1/2/3/4/X): ").strip().upper()

        if choice == 'X' or choice == 'N':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                result = add(num1, num2)
                operation = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                operation = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                operation = '*'
            elif choice == '4':
                result = divide(num1, num2)
                operation = '/'
            
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator()