def linear_search(nums, value):
    for i, num in enumerate(nums):
        if num == value:
            return i
    return -1


def banary_search(nums, value):
    left, right = 0, len(nums) - 1

    while left <= right:
        center = (left + right) // 2

        if nums[center] == value:
            return center
        elif nums[center] < value:
            left = center + 1
        else:
            right = center - 1

    return - 1


def banary_search_v2(nums, value):
    def _banary_search_v2(nums, value, left, right):
        if left > right:
            return -1

        center = (left + right) // 2

        if nums[center] == value:
            return center
        elif nums[center] < value:
            return _banary_search_v2(nums, value, center + 1, right)
        else:
            return _banary_search_v2(nums, value, left, right - 1)

    return _banary_search_v2(nums, value, 0, len(nums) - 1)


print(linear_search([0, 1, 5, 7, 9, 11, 15, 20, 24], 15))
print(banary_search([0, 1, 5, 7, 9, 11, 15, 20, 24], 15))
print(banary_search_v2([0, 1, 5, 7, 9, 11, 15, 20, 24], 15))
