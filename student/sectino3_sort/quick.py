def execute(nums, first_index, last_index):
    pivot = nums[last_index]

    i = first_index - 1
    for j in range(first_index, last_index):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[last_index] = nums[last_index], nums[i + 1]
    return i + 1


def quick(nums):
    def _quick(nums, first_index, last_index):
        if first_index < last_index:
            mid_index = execute(nums, first_index, last_index)
            _quick(nums, first_index, mid_index - 1)
            _quick(nums, mid_index + 1, last_index)

    _quick(nums, 0, len(nums) - 1)
    return nums
