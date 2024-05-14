def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Enter the valid input."
    return a / b
def integer_division(a, b):
    if b == 0:
        return "Enter the valid input"
    return a // b
def modulus(a, b):
    return a % b
def exponentiation(a, b):
    return a ** b
def absolute_value(a):
    return abs(a)
def get_numbers(single=False):
    if single:
        a = float(input("Enter a number: "))
        return a
    else:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a, b
def main():
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Integer Division")
        print("6. Modulus")
        print("7. Exponentiation")
        print("8. Absolute Value")
        print("9. Exit")
        choice = input("Enter choice (1-9): ")
        if choice == '9':
            print("Exiting the program")
            break
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            a, b = get_numbers()
            if choice == '1':
                print(f"The result is: {add(a, b)}")
            elif choice == '2':
                print(f"The result is: {subtract(a, b)}")
            elif choice == '3':
                print(f"The result is: {multiply(a, b)}")
            elif choice == '4':
                print(f"The result is: {divide(a, b)}")
            elif choice == '5':
                print(f"The result is: {integer_division(a, b)}")
            elif choice == '6':
                print(f"The result is: {modulus(a, b)}")
            elif choice == '7':
                print(f"The result is: {exponentiation(a, b)}")
            elif choice == '8':
                 a = get_numbers(single=True)
                 print(f"The result is: {absolute_value(a)}")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")
        another = input("Do you want to perform another operation? (yes/no): ")
        if another.lower() != 'yes':
            print("Thankyou")
            break
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Enter the valid input."
    return a / b
def integer_division(a, b):
    if b == 0:
        return "Enter the valid input"
    return a // b
def modulus(a, b):
    return a % b
def exponentiation(a, b):
    return a ** b
def absolute_value(a):
    return abs(a)
def get_numbers(single=False):
    if single:
        a = float(input("Enter a number: "))
        return a
    else:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a, b
def main():
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Integer Division")
        print("6. Modulus")
        print("7. Exponentiation")
        print("8. Absolute Value")
        print("9. Exit")
        choice = input("Enter choice (1-9): ")
        if choice == '9':
            print("Exiting the program")
            break
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            a, b = get_numbers()
            if choice == '1':
                print(f"The result is: {add(a, b)}")
            elif choice == '2':
                print(f"The result is: {subtract(a, b)}")
            elif choice == '3':
                print(f"The result is: {multiply(a, b)}")
            elif choice == '4':
                print(f"The result is: {divide(a, b)}")
            elif choice == '5':
                print(f"The result is: {integer_division(a, b)}")
            elif choice == '6':
                print(f"The result is: {modulus(a, b)}")
            elif choice == '7':
                print(f"The result is: {exponentiation(a, b)}")
            elif choice == '8':
                 a = get_numbers(single=True)
                 print(f"The result is: {absolute_value(a)}")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")
        another = input("Do you want to perform another operation? (yes/no): ")
        if another.lower() != 'yes':
            print("Thankyou")
            break
if __name__ == "__main__":
    main()

