class Node(object):
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

    def reverse_print(self):
        current_node = self.head
        if current_node is None:
            print(None)
            return

        while current_node.next:
            current_node = current_node.next

        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.prev
        print()

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def remove(self, data):
        current_node = self.head

        if current_node and current_node.data == data:
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            else:
                current_node.next.prev = None
                self.head = current_node.next
                current_node = None

        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            return

        if current_node.next is None:
            current_node.prev.next = None
            current_node = None
            return
        else:
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            current_node = None
            return

    def reverse_iter(self):
        previous_node = None
        current_node = self.head

        while current_node:
            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node

            current_node = current_node.prev

        if previous_node:
            self.head = previous_node.prev

    def reverse_recur(self):
        def _reverse_recur(current_node):
            if current_node is None:
                return None

            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node

            next_node = current_node.prev
            if next_node is None:
                return current_node

            return _reverse_recur(next_node)

        self.head = _reverse_recur(self.head)


if __name__ == "__main__":
    d = DoublyLinkedList()
    d.append(1)
    d.append(3)
    d.append(5)
    d.insert(0)
    d.append(7)
    d.append(9)
    d.print()
    d.reverse_print()
    d.remove(7)
    d.print()
    d.reverse_print()
    d.reverse_recur()
    d.print()
    d.reverse_print()
