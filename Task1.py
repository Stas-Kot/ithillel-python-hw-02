try:
    print('Lets find the minimum number!')
    print()
    inputted_numbers = (input('Enter your numbers, separated by comma: '))
    numbers_list = inputted_numbers.split(',')
    print(numbers_list)
    minimum = float(numbers_list[0])
    for number in numbers_list:
        if minimum > float(number):
            minimum = float(number)

    print(f'The minimum number is {minimum}')

except ValueError:
    print('You didn`t insert numbers, separated by comma correct! Program closed!')
