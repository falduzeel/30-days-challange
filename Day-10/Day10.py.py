def add(n1, n2):
    """Returns the sum of two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Returns the difference between two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Returns the quotient of two numbers."""
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    """Runs a continuous calculator session using recursion."""
    print("\n--- Day 10: Python Calculator ---")
    
    num1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
        
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))

        calculation_function = operations.get(operation_symbol)
        
        if calculation_function:
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ").lower()
            if choice == 'y':
                num1 = answer
            else:
                should_continue = False
                calculator()
        else:
            print("Invalid operator selected.")

if __name__ == "__main__":
    calculator()