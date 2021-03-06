def symmetric(tuples):
    nums_hash = {}
    ans = []
    for key, value in tuples:
        if nums_hash.get(value) == key:
            ans.append((key, value))
        else:
            nums_hash[key] = value

    return ans


if __name__ == "__main__":
    nums = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    print(symmetric(nums))
