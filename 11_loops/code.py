
number = 7
user_input = input('Would you like to play? (Y/n) ')

while user_input != 'n':
    user_number = int(input('Guess our number: '))
    if user_number == number:
        print('You guessed correctly!')
    elif abs(number - user_number) == 1:
        print('you were off by one')
    else:
        print('Sorry, it is wrong')

    user_input = input('Would you like to play? (Y/n) ')





