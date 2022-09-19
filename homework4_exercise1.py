try:
    number1 = float(input('Enter first number: '))
    menu = '''1 - Add
2 - Subtract
3 - Multiply
4 - Divide
5 - Exponentiation
Select operation: '''

    # take input from the menu
    user_choice = int(input(menu))
    number2 = float(input('Enter second number: '))
    # check if user choice is one of the five options
    if user_choice in range(1, 6):

        if user_choice == 1:
            result = number1 + number2
        elif user_choice == 2:
            result = number1 - number2
        elif user_choice == 3:
            result = number1 * number2
        elif user_choice == 4:
            result = number1 / number2
        elif user_choice == 5:
            result = number1 ** number2
    else:
        print("Invalid Input")

    print(f'Result: {result}')

# Error info
except ValueError:
    print("Do not enter letters or symbols(except dot). Please, restart the program and enter NUMBER")
except ZeroDivisionError:
    print("You can't divide by zero")
