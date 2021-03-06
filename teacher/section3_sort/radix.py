def counting_sort(numbers, place):
    counts = [0] * 10
    result = [0] * len(numbers)

    for num in numbers:
        index = int(num / place) % 10
        counts[index] += 1

    for i in range(1, 10):
        counts[i] += counts[i - 1]

    i = len(numbers) - 1
    while i >= 0:
        index = int(numbers[i] / place) % 10
        result[counts[index] - 1] = numbers[i]
        counts[index] -= 1
        i -= 1

    return result


def radix_sort(numbers):
    max_num = max(numbers)
    place = 1
    while place < max_num:
        numbers = counting_sort(numbers, place)
        place *= 10

    return numbers
