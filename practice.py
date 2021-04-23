def quick(nums):
    def _quick(nums, left, right):
        if left >= right:
            return

        i = left - 1
        for j in range(left, right):
            if nums[j] < nums[right]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        i += 1
        nums[i], nums[right] = nums[right], nums[i]
        _quick(nums, left, i - 1)
        _quick(nums, i + 1, right)

    _quick(nums, 0, len(nums) - 1)


def binary_search(nums, value):
    print(value)
    quick(nums)

    def _binary_search(nums, left, right, value):
        if left > right:
            return False

        mid = (left + right) // 2
        if nums[mid] < value:
            return _binary_search(nums, mid + 1, right, value)
        elif nums[mid] > value:
            return _binary_search(nums, left, mid - 1, value)
        else:
            return True

    return _binary_search(nums, 0, len(nums) - 1, value)


if __name__ == "__main__":
    import random

    nums = [random.randint(0, 100) for _ in range(100)]
    print(nums)
    print(binary_search(nums, random.randint(0, 100)))
    print(nums)
