def insersion(nums):
    nums_len = len(nums)
    for i in range(1, nums_len):
        temp_nums = nums[i]
        j = i - 1
        while nums[j] > temp_nums and j >= 0:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp_nums
    return nums


def bucket(nums):
    len_nums = len(nums)
    bucket = [[] for _ in range(int(max(nums) / len_nums))]

    for num in nums:
        i = int(num / len_nums)
        if i >= len(bucket):
            i = len(bucket) - 1
        bucket[i].append(num)

    for bucket_part in bucket:
        if bucket_part:
            bucket_part = insersion(bucket_part)

    ans = []
    for bucket_part in bucket:
        ans += bucket_part

    return ans
