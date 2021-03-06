def linear_search(numbers, value):
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return - 1


def banary_search(numbers, value):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def banary_search_v2(numbers, value):
    def _banary_search_v2(numbers, value, left, right):
        if left > right:
            return - 1

        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _banary_search_v2(numbers, value, mid + 1, right)
        else:
            return _banary_search_v2(numbers, value, left, mid - 1)

    return _banary_search_v2(numbers, value, 0, len(numbers) - 1)
