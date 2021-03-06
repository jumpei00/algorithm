def add_one_to_list(nums: list):
    nums.reverse()

    i = 0
    while i < len(nums):
        num = nums[i] + 1
        if num < 10:
            nums[i] = num
            break
        else:
            nums[i] = 0
            i += 1
    else:
        nums.append(1)

    nums.reverse()
    nums_str = ''.join(map(str, nums)).lstrip('0')

    return int(nums_str)


def remove_zero(nums: list) -> None:
    if nums and nums[0] == 0:
        nums.pop(0)
        remove_zero(nums)


def list_to_int(nums: list) -> int:
    sum_nums = 0
    for i, num in enumerate(reversed(nums)):
        sum_nums += num * (10 ** i)
    return sum_nums


def list_to_add_one(nums: list) -> int:
    i = len(nums) - 1
    while i >= 0:
        nums[i] += 1
        if nums[i] < 10:
            remove_zero(nums)
            break

        nums[i] = 0
        i -= 1
    else:
        nums[0] = 1
        nums.append(0)

    return list_to_int(nums)


if __name__ == "__main__":
    t = [9, 9, 9, 9]
    print(list_to_add_one(t))
