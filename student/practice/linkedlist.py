class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data)

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        previous_node = None
        current_node = self.head

        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        while current_node:
            if current_node.data == data:
                previous_node.next = current_node.next
                current_node = None
                return
            previous_node = current_node
            current_node = current_node.next

    def reverse_iter(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def reverse_recur(self):
        def _reverse_recur(previous_node, current_node):
            if current_node is None:
                return previous_node
            next_node = current_node.next
            current_node.next = previous_node
            return _reverse_recur(current_node, next_node)

        self.head = _reverse_recur(None, self.head)


if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.append(1)
    linkedlist.append(5)
    linkedlist.append(3)
    linkedlist.insert(4)
    linkedlist.print()
    linkedlist.reverse_recur()
    linkedlist.print()
