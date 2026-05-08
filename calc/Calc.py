import logging
logging.basicConfig(filename='calc.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

print('Enter a number, an operator and a second number to start')
logging.debug('Start of Calc.py')

while True:
    user_input1 = input('>')
    if user_input1 == 'q':
        print('You have successfully finished calculating')
        logging.info('User has quit the program')
        break
    user_input2 = input('>') #Operator (+,-,*./)
    user_input3 = input('>')

    try:
        if user_input2 == '+':
            logging.debug(f'Calculation: {user_input1} + {user_input2} + {user_input3} = {int(user_input1) + int(user_input3)}')
            print(f'{user_input1} {user_input2} {user_input3} = {int(user_input1) + int(user_input3)}')
        elif user_input2 == '-':
            logging.debug(f'Calculation: {user_input1} - {user_input2} - {user_input3} = {int(user_input1) - int(user_input3)}')
            print(f'{user_input1} {user_input2} {user_input3} = {int(user_input1) - int(user_input3)}')
        elif user_input2 == '*':
            logging.debug(f'Calculation: {user_input1} * {user_input2} * {user_input3} = {int(user_input1) * int(user_input3)}')
            print(f'{user_input1} {user_input2} {user_input3} = {int(user_input1) * int(user_input3)}')
        elif user_input2 == '/':
            logging.debug(f'Calculation: {user_input1} / {user_input2} / {user_input3} = {int(user_input1) / int(user_input3)}')
            print(f'{user_input1} {user_input2} {user_input3} = {int(user_input1) / int(user_input3)}')
        else:
            logging.warning(f'Invalid operator entered: {user_input2}')
            print('Invalid operator. Please only input +, -, *, or /')
    except ValueError:
           logging.error(f'ValueError: input1={user_input1}, input2={user_input2}, input3={user_input3}')
           print('Invalid input. Please only input numbers')
    except ZeroDivisionError:
         logging.error(f'ZeroDivisionError: input1={user_input1}, input2={user_input2}, input3={user_input3}')
         print('Cannot divide by zero. Please input a non-zero number for the second number when using division.')
