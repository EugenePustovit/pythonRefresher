# !!>> Not recommended <<!!

default_y = 3


def add(x, y=default_y):
    sum = x + y
    print(sum)


add(2)

default_y = 5
add(2)
