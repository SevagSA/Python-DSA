'''
Quicksort algorithm implementation
'''


def quicksort(list: list, left: int, right: int) -> None:
    if left >= right:
        return

    pivot = partition(list, left, right)

    quicksort(list, left, pivot - 1)
    quicksort(list, pivot + 1, right)


def partition(list: list, left: int, right: int) -> int:
    pivot = list[right]  # arbitrarily picking the last node

    i = left - 1
    for j in range(left, right):
        if list[j] < pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[right] = list[right], list[i + 1]
    return i+1


def main() -> None:
    a1 = [3, 2, 1]
    a2 = [1, 2, 3]
    a3 = []
    a4 = [3, 1, -1, 0, 2, 5]
    a5 = [2, 2, 1, 1, 0, 0, 4, 4, 2, 2, 2]
    a6 = [0]
    a7 = [3, -2, -1, 0, 2, 4, 1]
    a8 = [1, 2, 3, 4, 5, 6, 7]
    a9 = [2, 2, 2, 2, 2, 2, 2]

    quicksort(a1, 0, len(a1)-1)
    quicksort(a2, 0, len(a2)-1)
    quicksort(a3, 0, len(a3)-1)
    quicksort(a4, 0, len(a4)-1)
    quicksort(a5, 0, len(a5)-1)
    quicksort(a6, 0, len(a6)-1)
    quicksort(a7, 0, len(a7)-1)
    quicksort(a8, 0, len(a8)-1)
    quicksort(a9, 0, len(a9)-1)

    assert a1 == [1, 2, 3]
    assert a2 == [1, 2, 3]
    assert a3 == []
    assert a4 == [-1, 0, 1, 2, 3, 5]
    assert a5 == [0, 0, 1, 1, 2, 2, 2, 2, 2, 4, 4]
    assert a6 == [0]
    assert a7 == [-2, -1, 0, 1, 2, 3, 4]
    assert a8 == [1, 2, 3, 4, 5, 6, 7]
    assert a9 == [2, 2, 2, 2, 2, 2, 2]


if __name__ == '__main__':
    main()
