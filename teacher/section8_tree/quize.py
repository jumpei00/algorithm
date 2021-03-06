import heapq
from collections import Counter


def top_n_with_heap(words, n):
    counter_word = Counter(words)
    data = [(-counter_word[word], word) for word in counter_word]
    heapq.heapify(data)
    return [heapq.heappop(data)[1] for _ in range(3)]


if __name__ == "__main__":
    words = ['python', 'c', 'java', 'go', 'python', 'c', 'go', 'python']
    print(top_n_with_heap(words, 3))

    # numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    # heap_data = []
    # heapq.heapify(numbers)
    # print(numbers)
    # print(heapq.nlargest(3, numbers))
    # print(heapq.nsmallest(3, numbers))

    # for num in numbers:
    #     heapq.heappush(heap_data, num)

    # print(heap_data)

    # while heap_data:
    #     print(heapq.heappop(heap_data))
