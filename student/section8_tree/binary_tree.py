class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node, value):
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)

            return node

        self.root = _insert(self.root, value)

    def inorder(self):
        def _inorder(node):
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)

    def search(self, value):
        def _search(node, value):
            if node is None:
                return False

            if node.value == value:
                return True
            elif node.value > value:
                return _search(node.left, value)
            elif node.value < value:
                return _search(node.right, value)

        return _search(self.root, value)

    def remove(self, value):
        def _remove(node, value):
            if node.value > value:
                node.left = _remove(node.left, value)
            elif node.value < value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # 両方のNodeに値がある場合
                # 該当のものを今のnodeのvalueに設定してから
                # 設定した値を再び削除しにいく
                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)

            return node

        self.root = _remove(self.root, value)

    def min_value(self, node):
        current = node
        while current.left:
            current = current.left
        return current


if __name__ == "__main__":
    binary_tree = BinarySearchTree()
    binary_tree.insert(3)
    binary_tree.insert(6)
    binary_tree.insert(5)
    binary_tree.insert(7)
    binary_tree.insert(1)
    binary_tree.insert(10)
    binary_tree.insert(2)
    binary_tree.inorder()
    print(binary_tree.search(7))
    binary_tree.remove(6)
    binary_tree.inorder()
