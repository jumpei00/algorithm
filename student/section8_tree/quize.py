import heapq
from collections import Counter


def top_n_heap(words: list, n: int):
    counter = Counter(words)
    c = [(-value, key) for key, value in counter.items()]
    heapq.heapify(c)

    r = [heapq.heappop(c)[1] for _ in range(n)]
    return r


if __name__ == "__main__":
    w = ['python', 'c', 'java', 'go', 'python', 'c', 'go', 'python']
    print(top_n_heap(w, 3))
