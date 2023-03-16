def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def split_number():
    try:
        input_value = input('Enter your number, between 10 and 99 inclusive: ')
        numbers = []
        if not is_number(input_value):
            print('You didn`t insert an integer number!')
            split_number()
        elif int(input_value) >=10 and int(input_value) <=99 and len(input_value) == 2:
            for digit in input_value:
                numbers.append(int(digit))
            print(f'{numbers[0]} {numbers[1]}')

        else:
            print('Number must be between 10 and 99 inclusive')
            split_number()

    except ValueError:
        print('You didn`t insert an integer number! Program closed!')

split_number()