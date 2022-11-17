'''
Binary search implementation (recursive)
'''


def binary_search(list: list, left: int, right: int, num: int) -> int:
    '''
    Search a number withing a list using the binary search algorithm.

    :param list list: the list that will be searched through
    :param int left: the left bound of the list. This is where the search
        will start.
    :param int right: the right bound of the list. This is where the search
        will end.
    :param int num: this is the number that the function will search for
    :returns int: the index of `num` within `list`
    '''
    if left > right:
        return -1
    mid = (left + right) // 2

    if num == list[mid]:
        return mid
    if num < list[mid]:
        return binary_search(list, left, mid - 1, num)
    return binary_search(list, mid + 1, right, num)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
left = 0
right = len(nums) - 1
print(binary_search(nums, left, right, 2))
print(binary_search(nums, left, right, 13))
