
number = 7

user_input = input('Enter "Y" if you want to play: ')

if user_input in ('y', 'Y'):
    user_number = int(input('Guess our number: '))
    if user_number == number:
        print('You guessed correctly!')
    elif abs(number - user_number) == 1:
        print('you were off by one')
    else:
        print('Sorry, it is wrong')
