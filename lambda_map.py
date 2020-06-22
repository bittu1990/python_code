# Lambda function is a small anonymous function.
# It can take any arguments but can have only one expression

x = lambda a: a + 10
print(x(5))

y = lambda a, b: a + b
print(y(1, 2))


# lambda function within a function

def myfunc(n):
    """
   function
    :param n:
    :return:
    """
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))


# Map
def faren(t):
    """
    fahrenheit
    :param t:
    :return:
    """
    return (float(9) / 5) * t + 32


def celsius(t):
    """
    celsius
    :param t:
    :return:
    """
    return (float(5) / 9) * t - 32


temp = (36.5, 37, 37.5, 38, 39)
F = list(map(faren, temp))
C = list(map(celsius, F))

print(F)
print(C)


