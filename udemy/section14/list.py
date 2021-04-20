def order_even_first_odd_last(nums: list) -> None:
    nums_len = len(nums)
    index = -1

    for i in range(nums_len):
        if nums[i] % 2 == 0:
            index += 1
            nums[index], nums[i] = nums[i], nums[index]


def order_even_first_odd_last_v2(nums: list) -> None:
    i, j = 0, len(nums) - 1

    while i < j:
        if nums[i] % 2 == 0:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1


def order_change_by_indexes_v1(chars: list, indexes: list) -> str:
    temp = [None] * len(chars)
    for i, index in enumerate(indexes):
        temp[index] = chars[i]
    return ''.join(temp)


def order_change_by_indexes_v2(chars: list, indexes: list) -> str:
    for i in range(len(indexes)):
        index = indexes.index(i)
        chars[i], chars[index] = chars[index], chars[i]
        indexes[i], indexes[index] = indexes[index], indexes[i]
    return ''.join(chars)


if __name__ == "__main__":
    # nums = [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8]
    # order_even_first_odd_last(nums)
    # order_even_first_odd_last_v2(nums)
    # print(nums)
    chars = ['h', 'y', 'n', 'p', 't', 'o']
    indexes = [3, 1, 5, 0, 2, 4]
    print(order_change_by_indexes_v2(chars, indexes))
