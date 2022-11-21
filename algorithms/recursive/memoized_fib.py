'''
Fibonacci sequence algorithm implementation.
This is an optimized implementation, i.e. using memoization.
'''

memoized_cache = {0: 1, 1: 1}


def fibonacci(i: int) -> int:
    '''
    Return the `i`th number in the Fibonacci sequence

    :param int i: the index of the number that we want to get from
        the Fibonacci sequence
    :returns: the number in the Fibonacci sequence at the specified index `i`
    '''
    if i == 0 or i == 1:
        return i
    if memoized_cache.get(i):
        return memoized_cache.get(i)
    result = fibonacci(i - 1) + fibonacci(i - 2)
    memoized_cache[i] = result
    return result


for i in range(0, 13):
    print(fibonacci(i))
