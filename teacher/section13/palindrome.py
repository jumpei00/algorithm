def is_palindrome(string: str) -> bool:
    if not string:
        return False

    start, end = 0, len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

    return True


def find_palindrome(string: str, left: int, right: int):
    while 0 <= left and right <= len(string) - 1:
        if string[left] != string[right]:
            break
        yield string[left:right + 1]
        left -= 1
        right += 1


def find_all_palindrome(string: str):
    len_string = len(string)
    if not len_string:
        yield
    if len_string == 1:
        yield string

    for i in range(1, len_string - 1):
        yield from find_palindrome(string, i - 1, i + 1)
        yield from find_palindrome(string, i - 1, i)


if __name__ == "__main__":
    s = 'abcracecarbda'
    print(find_all_palindrome(s))
