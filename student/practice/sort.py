import random
from datetime import datetime


def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]


def bubble(nums):
    len_nums = len(nums)
    for i in range(len_nums - 1):
        for j in range(len_nums - i - 1):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)
    return nums


def selection(nums):
    len_nums = len(nums)
    for i in range(len_nums):
        temp_index = i
        for j in range(i, len_nums):
            if nums[j] < nums[temp_index]:
                temp_index = j
        swap(nums, i, temp_index)
    return nums


def insertion(nums):
    len_nums = len(nums)
    i = 0
    while i < len_nums - 1:
        if nums[i] > nums[i + 1]:
            temp = nums[i + 1]
            j = i
            while nums[j] > temp and j >= 0:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = temp
        i += 1
    return nums


def quick(nums):
    def _quick(nums, first, last):
        if first >= last:
            return

        i = first - 1
        for j in range(first, last):
            if nums[j] < nums[last]:
                i += 1
                swap(nums, i, j)
        swap(nums, i + 1, last)

        _quick(nums, first, i)
        _quick(nums, i + 2, last)

        return nums

    return _quick(nums, 0, len(nums) - 1)


def merge(nums):
    if len(nums) <= 1:
        return nums

    center = len(nums) // 2
    left_nums = nums[:center]
    right_nums = nums[center:]

    merge(left_nums)
    merge(right_nums)

    i = li = ri = 0
    while li < len(left_nums) and ri < len(right_nums):
        if left_nums[li] <= right_nums[ri]:
            nums[i] = left_nums[li]
            li += 1
        else:
            nums[i] = right_nums[ri]
            ri += 1
        i += 1

    while li < len(left_nums):
        nums[i] = left_nums[li]
        li += 1
        i += 1

    while ri < len(right_nums):
        nums[i] = right_nums[ri]
        ri += 1
        i += 1

    return nums


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10000)]
    # print(nums)
    start = datetime.now()
    # print(bubble(nums))
    # print(selection(nums))
    # print(insertion(nums))
    # print(quick(nums))
    # print(merge(nums))
    # bubble(nums)
    # insertion(nums)
    selection(nums)
    # quick(nums)
    # merge(nums)
    end = datetime.now()
    print(f'time: {end - start}')
