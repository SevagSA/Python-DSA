'''
Sum of natural number using recursion
(I am practicing recursion)
'''


def sum_of_natrual_number(num: int, sum: int) -> int:
    '''
    For a given number, num, sum all the values u to num.
    Example: num = 10, output = 1+2+3+4+5+6+7+8+9+10 = 55.

    :param int num: the number that will be used to sum up
        values up to it.
    :param int sum: the sum of all numbers up to `num`
    :returns int: the sum of all numbers up to `num` (`sum`)
    '''
    if num == 0:
        return sum
    return sum_of_natrual_number(num - 1, num + sum)

print(sum_of_natrual_number(536, 0))

'''
An alternative approach:
'''
def sum_of_natrual_number(num: int) -> int:
    if num == 0:
        return num
    return num + sum_of_natrual_number(num - 1)

print(sum_of_natrual_number(536))
