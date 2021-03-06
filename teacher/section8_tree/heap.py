import sys


class MiniHeap(object):
    def __init__(self):
        self.heap = [-1 * sys.maxsize]
        self.current_size = 0

    def parent_index(self, index):
        return index // 2

    def left_child_index(self, index):
        return index * 2

    def right_child_index(self, index):
        return (index * 2) + 1

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index):
        while self.parent_index(index) > 0:
            if self.heap[index] < self.heap[self.parent_index(index)]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def heapify_down(self, index):
        while self.left_child_index(index) <= self.current_size:
            mini_child_index = self.mini_child_index(index)
            if self.heap[index] > self.heap[mini_child_index]:
                self.swap(index, mini_child_index)
            index = mini_child_index

    def mini_child_index(self, index):
        if self.right_child_index(index) > self.current_size:
            return self.left_child_index(index)
        else:
            if self.heap[self.left_child_index(index)] < self.heap[self.right_child_index(index)]:
                return self.left_child_index(index)
            else:
                return self.right_child_index(index)

    def push(self, value):
        self.heap.append(value)
        self.current_size += 1
        self.heapify_up(self.current_size)

    def pop(self):
        if len(self.heap) == 1:
            return

        root = self.heap[1]
        data = self.heap.pop()
        self.current_size -= 1

        if len(self.heap) == 1:
            return root

        self.heap[1] = data
        self.heapify_down(1)

        return root


if __name__ == "__main__":
    mini_heap = MiniHeap()
    mini_heap.push(5)
    mini_heap.push(6)
    mini_heap.push(2)
    mini_heap.push(9)
    mini_heap.push(13)
    mini_heap.push(11)
    mini_heap.push(1)
    print(mini_heap.heap)
    print(mini_heap.pop())
    print(mini_heap.heap)
