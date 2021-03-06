class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    @property
    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        print('######')

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node

        last_node.next_node = new_node

    def insert(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def remove(self, data):
        current_node = self.head
        # 先頭のcurrentはpreviousがNoneなので先に処理する
        if current_node and current_node.data == data:
            self.head = current_node.next_node
            current_node = None
            return

        # 上のifとこのwhileに該当しないものはnodeがない(None)か
        # 該当するものがない(nodeを最後まで見た)のどちらかとなる
        previous_node = None
        while current_node:
            if current_node.data == data:
                previous_node.next_node = current_node.next_node
                current_node = None
                return

            previous_node = current_node
            current_node = current_node.next_node

    def reverse_iter(self):
        previous_node = None
        current_node = self.head
        while current_node:
            # temp用
            next_node = current_node.next_node
            # 今のnodeのnextをpreviousにして逆向きにする
            current_node.next_node = previous_node

            # 次のnodeをセッティング
            previous_node = current_node
            current_node = next_node

        # 現在、current_nodeはNone、previous_nodeは先頭のnodeになっている
        self.head = previous_node

    def reverse_recur(self):
        def _reverse_recur(previous_node, current_node):
            if not current_node:
                return previous_node

            next_node = current_node.next_node
            current_node.next_node = previous_node

            previous_node = current_node
            current_node = next_node

            return _reverse_recur(previous_node, current_node)

        self.head = _reverse_recur(None, self.head)

    def reverse_even(self):
        previous_node = None
        current_node = self.head

        while current_node:
            if current_node.data % 2 == 0:
                even_current = current_node
                even_last = even_current.next_node
                while even_last and even_last.data % 2 == 0:
                    # temp用
                    next_node = even_last.next_node

                    # 最後のnodeの向きを1つ前のnodeに変える
                    even_last.next_node = even_current
                    # even_currentとeven_lastを1つ進める
                    even_current = even_last
                    even_last = next_node

                current_node.next_node = even_last

                # 先頭nodeだった場合はpreviousがNoneなので別に処理
                if previous_node is None:
                    self.head = even_current
                else:
                    previous_node.next_node = even_current

                # even_lastがNoneならば最後まで探索したので終了
                if even_last is None:
                    return

                previous_node = even_last
                current_node = even_last.next_node

            else:
                previous_node = current_node
                current_node = current_node.next_node

    def reverse_even_v2(self):
        def _reverse_even_v2(head, previous_node):
            # Nodeが最後まで行った場合の処理
            if head is None:
                return None

            current_node = head
            # 今のNodeが偶数であればnextの方向を逆向きにする処理を開始する
            while current_node and current_node.data % 2 == 0:
                next_node = current_node.next_node
                current_node.next_node = previous_node
                previous_node = current_node
                current_node = next_node

            # (偶数の処理が完了したあとはheadとcurrent_nodeの位置が
            # 異なっていることが前提であるが)
            # もしheadとcurrent_nodeの位置が異なっていた場合はheadのnextを
            # current_nodeにしてあげる必要がある(現段階ではhead.nextは1つ前のNodeを指している)
            # その後でprevious_nodeを返すとheadの1つ前のNodeのnextがprevious_nodeを指すことになり
            # 逆向きの処理が簡潔する
            # しかし、まだ続きのNodeがあるかもしれないので、ここから再び探索を開始させる
            if current_node != head:
                head.next_node = current_node
                _reverse_even_v2(current_node, None)
                return previous_node
            # これで偶数の処理は完了したが、奇数が続く場合の処理を書く必要がある
            # 奇数の場合は、特に処理をせず次のNodeを見に行けば良い
            # その場合、奇数Nodeの次は何になるか？と処理を進めることで「奇数→偶数」の時でも
            # 最終的にNodeが上手くつながるのでBest！(その場合はhead.nextはprevious_node(最後の偶数node)となる)
            # 奇数が続いてそのまま終了した時は、奇数が連続して欲しいのでheadを返してあげる
            else:
                head.next_node = _reverse_even_v2(head.next_node, head)
                return head

        self.head = _reverse_even_v2(self.head, None)


if __name__ == "__main__":
    li = LinkedList()
    li.append(1)
    li.append(4)
    li.append(6)
    li.append(8)
    li.append(11)
    li.append(13)
    li.append(4)
    li.append(6)
    li.append(8)
    li.append(11)
    li.reverse_even_v2()
    li.reverse_even()
    li.print
