print('Enter a number, an operator and a second number to start')

while True:
    user_input1 = input('>')
    if user_input1 == 'q':
        print('You have successfully finished calculating')
        break
    user_input2 = input('>') #Operator (+,-,*./)
    user_input3 = input('>')

    try:
        if user_input2 == '+':
            print(user_input1, user_input2, user_input3, '=', int(user_input1) + int(user_input3))
        elif user_input2 == '-':
            print(user_input1, user_input2, user_input3, '=', int(user_input1) - int(user_input3))
        elif user_input2 == '*':
            print(user_input1, user_input2, user_input3, '=', int(user_input1) * int(user_input3))
        elif user_input2 == '/':
            print(user_input1, user_input2, user_input3, '=', int(user_input1) / int(user_input3))
        else:
             print('Invalid operator. Please only input +, -, *, or /')
    except ValueError:
            print('Invalid input. Please only input numbers')
    except ZeroDivisionError:
         print('Cannot divide by zero. Please input a non-zero number for the second number when using division.')