'''
Mergesort algorithm implementation
'''


def merge_sort(list: list) -> None:
    if len(list) > 1: # divide list until there's 1 element
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            # compare elements 1 by 1
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1


def main():
    list = [3, 2, 1, 24, 8, 9, 4, 34, 5, 5,
            22, 3, 4, 7, 79, 78, 68, 46, 43, 2, 23]
    print(f'Original list: {list}')
    merge_sort(list)
    print(f'Sorted list: {list}')


if __name__ == '__main__':
    main()
