def sort(nums):
    len_nums = len(nums)

    for i in range(len_nums - 1):
        for j in range(i + 1, len_nums):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 100) for _ in range(10)]
    print(nums)
    print(sort(nums))
