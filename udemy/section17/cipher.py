import string


def caesar_cipher(text: str, shift: int) -> str:
    result = ''
    alphabet = string.ascii_uppercase
    len_alphabet = len(alphabet)

    for char in text:
        if char.isupper():
            alphabet = string.ascii_uppercase
        elif char.islower():
            alphabet = string.ascii_lowercase
        else:
            result += char
            continue
        index = (alphabet.index(char) + shift) % len_alphabet
        result += alphabet[index]

    return result


def caesar_cipher_v2(text: str, shift: int) -> str:
    result = ''
    len_alphabet = ord('Z') - ord('A') + 1

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - ord('A')) %
                          len_alphabet + ord('A'))
        elif char.islower():
            result += chr((ord(char) + shift - ord('a')) %
                          len_alphabet + ord('a'))
        else:
            result += char

    return result


def caesar_cipher_hach(text: str):
    len_alphabet = len(string.ascii_lowercase)

    for candidate_shift in range(len_alphabet):
        decript = ''
        for char in text:
            if char.isupper():
                alphabet = string.ascii_uppercase
            elif char.islower():
                alphabet = string.ascii_lowercase
            else:
                decript += char
                continue

            index = alphabet.index(char) - candidate_shift
            if index < 0:
                index += len_alphabet
            decript += alphabet[index]

        yield candidate_shift, decript


def caesar_cipher_hach_v2(text: str):
    len_alphabet = ord('Z') - ord('A') + 1

    for candidate_shift in range(len_alphabet):
        decript = ''
        for char in text:
            if char.isupper():
                index = ord(char) - candidate_shift
                if index < ord('A'):
                    index += len_alphabet
                decript += chr(index)
            elif char.islower():
                index = ord(char) - candidate_shift
                if index < ord('a'):
                    index += len_alphabet
                decript += chr(index)
            else:
                decript += char

        yield candidate_shift, decript


def generate_key(message: str, keyword: str) -> str:
    key = keyword
    i = 0
    len_keyword = len(keyword)

    while len(message) != len(key):
        key += keyword[i % len_keyword]
        i += 1
    return key


def vigenere_cipher(message: str, keyword: str) -> str:
    alphabet = string.ascii_uppercase
    result = ''
    for char, key in zip(message, keyword):
        if char.isalpha():
            index = (alphabet.index(char) + alphabet.index(key)) % 26
            result += alphabet[index]
        else:
            result += char

    return result


def vigenere_decript(cipher_text: str, keyword: str) -> str:
    alphabet = string.ascii_uppercase
    result = ''
    for char, key in zip(cipher_text, keyword):
        if char.isalpha():
            index = (alphabet.index(char) - alphabet.index(key) + 26) % 26
            result += alphabet[index]
        else:
            result += char

    return result


if __name__ == "__main__":
    char = 'TODAY IS MONDAY YAKINIKU'
    # e = caesar_cipher(char, 5)
    # for c, d in caesar_cipher_hach_v2(e):
    #     print(f'{c}: {d}')
    key = 'CAT'
    e = vigenere_cipher(char, generate_key(char, key))
    print(e)
    d = vigenere_decript(e, generate_key(e, key))
    print(d)
