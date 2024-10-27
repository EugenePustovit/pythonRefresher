
name = input('Enter your name: ')
print(name)

size_input = input('How long is your house (in sq ft): ')
sq_feet = int(size_input)
sq_meters = sq_feet / 10.8
print(f'{sq_feet} sq feet is {sq_meters:.2f} sq meters.')
