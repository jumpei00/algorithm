def delete_duplicate_v2(nums: list):
    tmp = [nums[0]]
    i, len_num = 0, len(nums) - 1
    while i < len_num:
        if nums[i] != nums[i + 1]:
            tmp.append(nums[i + 1])
        i += 1
    return tmp


def delete_duplicate_v4(nums):
    i = len(nums) - 1
    while i > 0:
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        i -= 1
