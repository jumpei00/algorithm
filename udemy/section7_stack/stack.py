class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()


if __name__ == "__main__":
    stack = Stack()
    print(stack.stack)
    stack.push(1)
    print(stack.stack)
    print(stack.pop())
    print(stack.stack)
    print(stack.pop())
    print(stack.stack)
