def all_perms(elements: list):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


if __name__ == "__main__":
    nums = [1, 2, 3]
    for p in all_perms(nums):
        print(p)
