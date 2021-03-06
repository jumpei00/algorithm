class Node(object):
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    @property
    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        new_node.prev = last_node
        return

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return

    def remove(self, data):
        # Nodeがない場合(self.headがNone)
        # Nodeが途中にある場合(self.headのnextとprevが共に存在する)
        # Nodeが最後にある場合(self.headのnextがNoneでprevが存在する)
        # Nodeが見つからなかった場合(最終的にNone)
        # →これらはwhileで回すことで場合分け可能

        # Nodeが1つしかない場合(self.headのnextとprevが共にNone)
        # Nodeが最初にある場合(self.headのnextは存在していてprevがNone)
        # →これらは最初に処理する

        # whileで回して場合分けを全部いっぺんに行うこともできるが、わかりづらい？
        current_node = self.head
        # Nodeが最初にある場合の処理
        if current_node and current_node.data == data:
            # 1つしかない場合
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            else:
                self.head = current_node.next
                self.head.prev = None
                self.current_node = None
                return

        # 該当部分のNodeまで処理を進める
        while current_node and current_node.data != data:
            current_node = current_node.next

        # データがない場合とデータが存在しない場合
        if current_node is None:
            return

        # データが最後にある場合
        if current_node.next is None:
            current_node.prev.next = None
            current_node = None
            return
        # データが途中にあって、nextもprevも存在する場合
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

        # None -> None -> None　　の場合
        # None -> NODE_1 -> None　の場合
        # この2つをカバーしている
        if previous_node:
            self.head = previous_node.prev

    def reverse_recur(self):
        def _reverse_recur(current_node):
            # 先頭のNODEがNoneだった場合の処理
            if not current_node:
                return None

            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node

            # 最後まで処理が終了した場合の処理
            if current_node.prev is None:
                return current_node

            return _reverse_recur(current_node.prev)

        self.head = _reverse_recur(self.head)

    def buble_sort(self):
        end_node = None
        start_node = self.head

        while start_node != end_node:
            previous_node = start_node
            current_node = start_node.next

            while current_node != end_node:
                if previous_node.data > current_node.data:
                    previous_node.data, current_node.data = \
                        current_node.data, previous_node.data
                previous_node = current_node
                current_node = current_node.next

            end_node = previous_node

    def sort(self):
        current_node = self.head
        # データがない場合の処理
        if current_node is None:
            return

        while current_node:
            next_node = current_node.next
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = \
                        next_node.data, current_node.data
                next_node = next_node.next
            current_node = current_node.next


if __name__ == "__main__":
    d = DoublyLinkedList()
    d.append(1)
    d.append(5)
    d.append(2)
    d.append(9)
    # d.reverse_iter()
    # d.reverse_recur()
    d.sort()
    d.print
