def buble(nums: list) -> list:
    len_nums = len(nums)
    for i in range(len_nums - 1):
        for j in range(len_nums - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def insersion(nums: list) -> list:
    len_nums = len(nums)

    for i in range(len_nums):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp

    return nums


def selection(nums: list) -> list:
    len_nums = len(nums)

    for i in range(len_nums):
        min_index = i
        for j in range(i + 1, len_nums):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


def shell(nums: list) -> list:
    len_nums = len(nums)
    gap = len_nums

    while gap != 1:
        gap = gap // 2
        for i in range(gap, len_nums):
            temp = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > temp:
                nums[j + gap] = nums[j]
                j -= gap
            nums[j + gap] = temp

    return nums


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 100) for _ in range(10)]
    print(nums)
    print(shell(nums))
