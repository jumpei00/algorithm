def delete_duplicate_v1(nums: list):
    ans = []
    for num in nums:
        if num not in ans:
            ans.append(num)
    return ans


def delete_duplicate_v3(nums: list):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i + 1)
        else:
            i += 1
    return nums


if __name__ == "__main__":
    nums = [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15, 15]
    print(delete_duplicate_v1(nums))
    print(delete_duplicate_v3(nums))
