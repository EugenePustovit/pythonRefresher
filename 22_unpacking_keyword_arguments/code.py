
def named(**kwargs):
    print(kwargs)


named(name='Bob', age=25)


def named_classic(name, age):
    print(name, age)


details = {'name': 'Bob', 'age': 25}

named_classic(**details)
named(**details)


def print_nicely(**kwargs):

    named(**kwargs)
    for arg, value in kwargs.items():
        print(f'{arg}: {value}')


print_nicely(name='James', age=35)


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name='James', age=35)


def myfunction(**kwargs):
    print(kwargs)


myfunction(**'James') # Error, must be mapping
myfunction(**None) # Error
