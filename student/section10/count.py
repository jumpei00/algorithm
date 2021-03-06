from collections import Counter, defaultdict
import operator


def max_counter(string: str):
    string = string.lower()
    ans = []
    for s in string:
        if not s.isspace():
            ans.append((s, string.count(s)))
    print(max(ans, key=operator.itemgetter(1)))


def max_counter_v2(string: str):
    string = string.lower()
    d = Counter()
    for s in string:
        if not s.isspace():
            d[s] += 1
    max_key = max(d, key=d.get)
    print((max_key, d[max_key]))


def max_counter_v3(string: str):
    string = string.lower()
    d = defaultdict(int)
    for s in string:
        if not s.isspace():
            d[s] += 1
    max_key = max(d, key=d.get)
    print((max_key, d[max_key]))


if __name__ == "__main__":
    string = 'This is a pen. This is an apple. Applepen.'
    max_counter(string)
    max_counter_v2(string)
    max_counter_v3(string)
