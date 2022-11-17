'''
Fibonacci sequence algorithm implementation.
This is a non-optimized implementation, i.e. without memoization.
'''

def fibonacci(i: int) -> int:
    '''
    Return the `i`th number in the Fibonacci sequence

    :param int i: the index of the number that we want to get from
        the Fibonacci sequence
    :returns: the number in the Fibonacci sequence at the specified index `i`
    '''
    if i == 0 or i == 1:
        return i
    return fibonacci(i - 1) + fibonacci(i - 2)

for i in range(0, 13):
    print(fibonacci(i))