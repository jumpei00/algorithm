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

            if node.value > value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)

            return node

        _insert(self.root, value)

    def inorder(self):
        def _inorder(node):
            if node is None:
                return
            _inorder(node.left)
            print(node.value, end=' ')
            _inorder(node.right)
        _inorder(self.root)
        print()

    def search(self, value):
        def _search(node, value):
            if node is None:
                return False

            if node.value == value:
                return True
            elif node.value > value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)

    def min_value_node(self, node):
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node

    def remove(self, value):
        def _remove(node, value):
            if node is None:
                return None

            if node.value > value:
                node.left = _remove(node.left, value)
            elif node.value < value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    temp = self.min_value_node(node.right)
                    node.value = temp.value
                    node.right = _remove(node.right, temp.value)

            return node

        _remove(self.root, value)


if __name__ == "__main__":
    binary_search = BinarySearchTree()
    binary_search.insert(3)
    binary_search.insert(6)
    binary_search.insert(5)
    binary_search.insert(7)
    binary_search.insert(1)
    binary_search.insert(10)
    binary_search.insert(2)
    binary_search.inorder()
    print(binary_search.search(5))
    binary_search.remove(5)
    binary_search.inorder()
