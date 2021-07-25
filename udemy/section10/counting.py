"""
Input: 'This is a pen. This is an apple. Applepen.'
"""
from typing import Tuple
from collections import defaultdict, Counter


def max_strings_count(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = defaultdict(int)

    for s in strings:
        if not s.isspace():
            d[s] += 1

    max_k = max(d, key=d.get)
    return (max_k, d[max_k])


def max_strings_count_v2(strings: str) -> Tuple[str, int]:
    c = Counter(strings)
    return c.most_common(2)[1]


if __name__ == "__main__":
    s = 'This is a pen. This is an apple. Applepen.'
    print(max_strings_count(s))
    print(max_strings_count_v2(s))
