###1 sposob
def first_method(a, b):
    import math
    return math.sqrt(a ** b)


###2 sposob
def second_method(a, b):
    from math import sqrt
    return sqrt(a ** b)


a = float(input('Pierwsza liczba: '))
b = float(input('Druga liczba liczba: '))

print(first_method(a, b))
print(second_method(a, b))