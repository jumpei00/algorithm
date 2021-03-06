import sys


class MiniHeap(object):
    def __init__(self):
        self.heap = [-1 * sys.maxsize]
        self.heap_size = 0

    def parent_index(self, index):
        return index // 2

    def left_index(self, index):
        return index * 2

    def right_index(self, index):
        return (index * 2) + 1

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def push(self, data):
        if hasattr(data, '__iter__'):
            for value in data:
                self.heap.append(value)
                self.heap_size += 1
                self.heapfy_up(self.heap_size)
        else:
            self.heap.append(data)
            self.heap_size += 1
            self.heapfy_up(self.heap_size)

    def pop(self):
        # 最初からheapに値がない場合
        if self.heap_size == 0:
            return

        last_data = self.heap.pop()
        self.heap_size -= 1
        # popした後にheapに値が無くなった場合
        if self.heap_size == 0:
            return

        self.heap[1] = last_data
        self.heapfy_down(1)

    def heapfy_up(self, index):
        while self.parent_index(index) > 0:
            if self.heap[index] < self.heap[self.parent_index(index)]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def heapfy_down(self, index):
        while self.left_index(index) <= self.heap_size:
            mini_index = self.mini_index(index)
            if self.heap[index] > self.heap[mini_index]:
                self.swap(index, mini_index)
            index = mini_index

    def mini_index(self, index):
        if self.right_index(index) > self.heap_size:
            return self.left_index(index)
        else:
            if self.heap[self.left_index(index)] < self.heap[self.right_index(index)]:
                return self.left_index(index)
            else:
                return self.right_index(index)


if __name__ == "__main__":
    data = [5, 6, 2, 9, 13, 11, 1]
    h = MiniHeap()
    h.push(data)
    print(h.heap)
    h.pop()
    print(h.heap)
