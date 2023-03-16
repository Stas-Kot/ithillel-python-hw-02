def is_correct_number(str):
    try:
        number = int(str)
        if number >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

def digit_count_with_len_function():
    try:
        input_value = input('Enter non-negative integer: ')

        if not is_correct_number(input_value):
            print('You didn`t insert non-negative integer number!')
            digit_count_with_len_function()
        else:
            print(len(input_value))

    except ValueError:
        print('You didn`t insert a correct number! Program closed!')

digit_count_with_len_function()

def digit_count():
    count = 0
    try:
        input_value = input('Enter non-negative integer: ')

        if not is_correct_number(input_value):
            print('You didn`t insert non-negative integer number!')
            digit_count_with_len_function()
        else:
            for digit in input_value:
                count += 1
            print(count)

    except ValueError:
        print('You didn`t insert a correct number! Program closed!')

digit_count()