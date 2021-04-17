class Stack(object):
    def __init__(self):
        self.full_size = 4
        self.stack = []

    def push(self, num):
        if len(self.stack) <= self.full_size:
            self.stack.append(num)
        else:
            print('stack is full')

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print('stack is empty')

    def is_empty(self):
        return not self.stack

    def is_full(self):
        return len(self.stack) == self.full_size


class Queue(object):
    def __init__(self):
        self.full_size = 4
        self.queue = []

    def enqueue(self, num):
        if len(self.queue) <= self.full_size:
            self.queue.append(num)
        else:
            print('queue is full')

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            print('queue is empty')

    def is_empty(self):
        return not self.queue

    def is_full(self):
        return len(self.queue) == self.full_size


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack.is_full())
    print(stack.pop())

    queue = Queue()
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    print(queue.is_full())
    print(queue.dequeue())
