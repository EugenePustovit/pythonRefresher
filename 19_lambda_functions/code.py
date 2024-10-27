print((lambda x, y: x + y)(5, 7))


def double(x):
    return x * 2


sequence = [1, 3, 5, 7, 9]
doubled = [i * 2 for i in sequence]
doubled = [double(i) for i in sequence]
doubled = map(double, sequence)

doubled = [(lambda x: x * 2)(i) for i in sequence]
doubled = list(map(lambda x: x * 2, sequence))


