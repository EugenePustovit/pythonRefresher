
def years_to_months(years):
    return years * 12


user_age = input('Enter your age: ')
years = int(user_age)

months = years_to_months(years)
print(f'{years} years is {months} months')
