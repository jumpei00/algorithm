def validate_format(chars):
    brackets = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for char in chars:
        if char in brackets.keys():
            stack.append(brackets[char])
        if char in brackets.values():
            if not stack:
                return False
            if char != stack.pop():
                return False

    if stack:
        return False
    return True


if __name__ == "__main__":
    json1 = "{'key1': 'value1', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}"
    json2 = "{'key1': ['value1', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}"
    print(validate_format(json1))
