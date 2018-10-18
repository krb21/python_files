def square_root(number):
    '''(number) -> float

    Returns the square root of the input number.

    >>> square_root(0)
    0
    >>> square_root(4)
    2
    >>> square_root(9.0)
    3.0
    '''
    return pow(number, (1/2))


def absolute(number):
    '''(number) -> float
    
    Returns the absolute value of the input number.
    
    >>> absolute(-2)
    2.0
    >>> absolute(4.5)
    4.5
    >>> absolute(-92.1)
    92.1
    '''
    return square_root(pow(number, 2))


# You can play here
def test_absolute():
    print(absolute(-2))
    print(absolute(4.5))


# Calling the tests
test_absolute()
