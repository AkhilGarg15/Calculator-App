history = []

def add(num1, num2):
    a = num1 + num2
    return f"{num1} + {num2} = {a}"

def subtract(num1, num2):
    return f"{num1} - {num2} = {num1 - num2}"

def multiply(num1, num2):
    return f"{num1} * {num2} = {num1 * num2}"

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return f"{num1} / {num2} = {num1 / num2}"

def power(num1, num2):
    return f"{num1} ^ {num2} = {num1 ** num2}"

def square_root(num1):
    if num1 < 0:
        return "Error: Cannot calculate square root of a negative number."
    else:
        return f"√{num1} = {num1 ** 0.5}"

def modulus(num1, num2):
    return f"{num1} % {num2} = {num1 % num2}"

def save_history(result):
    entry = result
    history.append(entry)
    with open("history.txt", "a") as file:
        file.write(entry + "\n")

while True:
    print("\n----- Basic Calculator -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. View History")
    print("9. Exit")
    

    try:
        choice = int(input("Enter your choice (1/2/3/4/5/6/7/8/9): "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 9.")
        continue

    if choice == 9:
        print("Exiting the calculator. Goodbye!")
        break

    if choice in (1, 2, 3, 4, 5, 6):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid number input. Please enter numeric values.")
            continue

        if choice == 1:
            result = add(num1, num2)
            save_history(result)
            print("Result:", result)
        elif choice == 2:
            result = subtract(num1, num2)
            save_history(result)
            print("Result:", result)
        elif choice == 3:
            result = multiply(num1, num2)
            save_history(result)
            print("Result:", result)
        elif choice == 4:
            result = divide(num1, num2)
            save_history(result)
            print("Result:", result)
        elif choice == 5:
            result = power(num1, num2)
            save_history(result)
            print("Result:", result)
        elif choice == 6:
            result = modulus(num1, num2)
            save_history(result)
            print("Result:", result)
    elif choice == 7:
        try:
            num1 = float(input("Enter the number: "))
        except ValueError:
            print("Invalid number input. Please enter a numeric value.")
            continue
        result = square_root(num1)
        save_history(result)
        print("Result:", result)

    elif choice == 8:
        if len(history) == 0:
            print("No history available.")
        else:
            with open("history.txt", "r") as file:
                print(file.read())

    else:
        print("Invalid choice. Please try again.")
