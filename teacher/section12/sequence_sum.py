def get_max_min_sequence_sum(nums: list, ope=max):
    result_requence, sum_sequence = 0, 0
    for num in nums:
        sum_sequence = ope(num, sum_sequence + num)
        result_requence = ope(result_requence, sum_sequence)
    return result_requence


def find_max_circular_sequence_sum(nums: list):
    max_sequence_sum = get_max_min_sequence_sum(nums)
    max_wrap_sequence = sum(nums) - get_max_min_sequence_sum(nums, ope=min)
    return max(max_sequence_sum, max_wrap_sequence)
