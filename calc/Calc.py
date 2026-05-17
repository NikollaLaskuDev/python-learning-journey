import logging
logging.basicConfig(filename='calc.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
import math
memory = []
last_result = None

print('Enter a number, an operator and a second number to start')
logging.debug('Start of Calc.py')

while True:
    user_input1 = input('>')
    if user_input1 == 'q':
        print('You have successfully finished calculating')
        logging.info('User has quit the program')
        break
    if user_input1 == 'ms':
        if last_result is None:
            print('No result to save yet!')
        else:
            memory.append(last_result)
            print(f'Saved {last_result} to memory')
            logging.info(f'Memory saved: {last_result}')
        continue
    if user_input1 == 'mr':
        if len(memory) == 0:
            print('Memory is empty!')
        else:
            print(f'Memory: {memory[-1]}')
            logging.info(f'Memory recalled: {memory[-1]}')
        continue
    if user_input1 == 'r':
        number = input('Enter a number to calculate its square root: ')
        try:
            result = math.sqrt(float(number))
            print(f'√{number} = {result}')
            last_result = result
            logging.debug(f'Square root: √{number} = {result}')
        except ValueError:
            logging.error(f'ValueError: invalid input for square root: {number}')
            print('Invalid input. Please enter a valid number for square root calculation.')
        continue    
    user_input2 = input('>') #Operator (+,-,*./)
    user_input3 = input('>')

    try:
        if user_input2 == '+':
            result = int(user_input1) + int(user_input3)
            logging.debug(f'Calculation: {user_input1} {user_input2} {user_input3} = {result}')
            print(f'Result: {result}')
            last_result = result
        elif user_input2 == '-':
            result = int(user_input1) - int(user_input3)
            logging.debug(f'Calculation: {user_input1} {user_input2} {user_input3} = {result}')
            print(f'Result: {result}')
            last_result = result    
        elif user_input2 == '*':
            result = int(user_input1) * int(user_input3)
            logging.debug(f'Calculation: {user_input1} {user_input2} {user_input3} = {result}')
            print(f'Result: {result}')
            last_result = result
        elif user_input2 == '/':
            result = int(user_input1) / int(user_input3)
            logging.debug(f'Calculation: {user_input1} {user_input2} {user_input3} = {result}')
            print(f'Result: {result}')
            last_result = result
        elif user_input2 == '%':
            result = float(user_input1) * (float(user_input3) / 100)
            logging.debug(f'Calculation: {user_input1} {user_input2} {user_input3} = {result}')
            print(f'Result: {result}')
            last_result = result
        else:
            logging.warning(f'Invalid operator entered: {user_input2}')
            print('Invalid operator. Please only input +, -, *, or /')
    except ValueError:
        logging.error(f'ValueError: input1={user_input1}, input2={user_input2}, input3={user_input3}')
        print('Invalid input. Please only input numbers')
    except ZeroDivisionError:
        logging.error(f'ZeroDivisionError: input1={user_input1}, input2={user_input2}, input3={user_input3}')
        print('Cannot divide by zero. Please input a non-zero number for the second number when using division.')
