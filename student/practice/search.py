def linear_search(nums, value):
    for i, num in enumerate(nums):
        if num == value:
            return i
    return - 1


def binary_search(nums, value):
    first_index = 0
    last_index = len(nums) - 1

    while first_index <= last_index:
        center_index = (first_index + last_index) // 2
        if nums[center_index] == value:
            return center_index
        elif nums[center_index] < value:
            first_index = center_index + 1
        elif nums[center_index] > value:
            last_index = center_index - 1

    return - 1


def binary_search_v2(nums, value):
    def _binary_search(nums, value, first_index, last_index):
        if first_index > last_index:
            return - 1

        center_index = (first_index + last_index) // 2
        if nums[center_index] == value:
            return center_index
        elif nums[center_index] < value:
            return _binary_search(nums, value, center_index + 1, last_index)
        elif nums[center_index] > value:
            return _binary_search(nums, value, first_index, center_index - 1)

    return _binary_search(nums, value, 0, len(nums) - 1)


if __name__ == "__main__":
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    print(linear_search(nums, 20))
    print(binary_search(nums, 20))
    print(binary_search_v2(nums, 20))
