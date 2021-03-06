def gnome_sort(numbers):
    len_numbers = len(numbers)
    index = 0
    while index < len_numbers:
        if index == 0:
            index = index + 1
        if numbers[index] >= numbers[index - 1]:
            index = index + 1
        else:
            numbers[index], numbers[index - 1] = \
                numbers[index - 1] = numbers[index]
            index = index - 1
    return numbers
