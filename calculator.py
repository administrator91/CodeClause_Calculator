#-------------------------------------------------------------------------------
# Name   :   SIMPLE CALCULATOR
# Purpose: You can perform here Arithmetic operation,SQUARE,CUBE,SQUARE ROOT,MODULUS function purpose..
# Create :   Rajarshi Sarkar
# Created:     03-12-2023
#--------------------------------------------------------------------------------
import math
################################ FUNCTION'S HERE ##########################################
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def square_root(x):
    return math.sqrt(x)

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Cannot perform modulus with divisor zero"

def calculator():
    print("\nHey Buddy!! This is a Simple Calculator Program made By Rajarshi.. ")
    print("          With help of Python Programming Language..           \n")
    while True:
        
        print("\t_____________Simple Calculator_____________")
        print("\t         -----------------------           ")
        print("\t            1. Run Calculator              ")
        print("\t            2. Exit                        ")
        print("\t         -----------------------           ")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            print("\nPerform Operations:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Square (^2)")
            print("6. Cube (^3)")
            print("7. Square Root (sr)")
            print("8. Modulus (%)")

            ############################## USER I/P ##################################
            num1 = float(input("\tEnter the first number: "))
            operation = input("\tEnter the operation (+, -, *, /, ^2, ^3, sr, %): ")

            ########################## arithmetic operations here ##############################
            if operation in ('+', '-', '*', '/'):
                num2 = float(input("\tEnter the second number: "))
                if operation == '+':
                    result = add(num1, num2)
                elif operation == '-':
                    result = subtract(num1, num2)
                elif operation == '*':
                    result = multiply(num1, num2)
                elif operation == '/':
                    result = divide(num1, num2)
            ################ logic for SQUARE,CUBE, and SQUARE ROOT ##############################
            elif operation == '^2':
                result = square(num1)
            elif operation == '^3':
                result = cube(num1)
            elif operation == 'sr':
                result = square_root(num1)
            ######################### logic for MODULUS find ################################
            elif operation == '%':
                num2 = float(input("\tEnter the modulus divisor: "))
                result = modulus(num1, num2)
            else:
                result = "Invalid operation"

            ######################## O/P HERE #############################################33
            print(f"\n\tResult: {result}")

        elif choice == '2':
            print("\n     THANK YOU ")
            print("Exiting the Calculator...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    calculator()
