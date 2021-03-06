import sys


class MiniHeap(object):
    def __init__(self):
        self.heap = [-1 * sys.maxsize]
        self.size = 0

    def parent_index(self, index):
        return index // 2

    def left_index(self, index):
        return index * 2

    def right_index(self, index):
        return (index * 2) + 1

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapfy_up(self, index):
        while self.parent_index(index) > 0:
            if self.heap[index] < self.heap[self.parent_index(index)]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def push(self, value):
        self.heap.append(value)
        self.size += 1
        self.heapfy_up(self.size)

    def pop(self):
        if self.size == 0:
            return

        last_value = self.heap.pop()
        self.size -= 1
        if self.size == 0:
            return

        self.heap[1] = last_value
        self.heapfy_down(1)

    def heapfy_down(self, index):
        while index < self.size:
            min_index = self.min_value_index(index)
            if self.heap[index] > self.heap[min_index]:
                self.swap(index, min_index)
            index = min_index

    def min_value_index(self, index):
        if self.right_index(index) > self.size:
            return self.left_index(index)
        if self.heap[self.left_index(index)] < self.heap[self.right_index(index)]:
            return self.left_index(index)
        else:
            return self.right_index(index)


if __name__ == "__main__":
    heap = MiniHeap()
    heap.push(5)
    heap.push(6)
    heap.push(2)
    heap.push(9)
    heap.push(13)
    heap.push(11)
    heap.push(1)
    print(heap.heap)
    heap.pop()
    print(heap.heap)
