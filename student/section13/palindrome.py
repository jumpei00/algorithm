def is_palindrome(string: str) -> bool:
    if not string or len(string) == 1:
        return True

    if string[0] == string[-1]:
        return is_palindrome(string[1:len(string) - 1])
    else:
        return False


# ex) this function don't evaluate 'abba'
def find_palindrome(string: str):
    result = []
    len_string = len(string)
    for i in range(len_string):
        left = i - 1
        right = i + 1
        while 0 <= left and right <= len_string - 1:
            if string[left] != string[right]:
                break
            result.append(string[left:right + 1])
            left -= 1
            right += 1
    return result


def is_palindrome_v2(string: str):
    if not string:
        return False

    start, end = 0, len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

    return True


def find_palindrome_v2(string: str, left: int, right: int):
    while 0 <= left and right <= len(string) - 1:
        if string[left] != string[right]:
            break
        yield string[left:right + 1]
        left -= 1
        right += 1


def find_all_palindrome_v2(string: str):
    for i in range(len(string)):
        # aba
        yield from find_palindrome_v2(string, i - 1, i + 1)
        # abba -> OK
        # abca -> NG
        yield from find_palindrome_v2(string, i - 1, i)


if __name__ == "__main__":
    s = 'abcracecarbda'
    # print(s == ''.join(reversed(s)))
    # print(s == s[::-1])
    # print(is_palindrome(s))
    # for r in find_all_palindrome_v2(s):
    #     print(r)
