class Node(object):
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class OneDimentionTree(object):
    def __init__(self):
        self.root = None

    def make_tree(self, point_list: list):
        point_list.sort()

        def _make_tree(point_list: list):
            if not point_list:
                return None

            mid_index = len(point_list) // 2

            node = Node(point_list[mid_index])
            node.left = _make_tree(point_list[:mid_index])
            node.right = _make_tree(point_list[mid_index + 1:])

            return node

        self.root = _make_tree(point_list)

    def find_in_scope(self, low: int, high: int):
        if low > high:
            return

        def _find_in_scope(node: Node, low: int, high: int):
            if low <= node.value <= high:
                print(node.value, end=' ')

            if node.left and low <= node.value:
                _find_in_scope(node.left, low, high)

            if node.right and node.value <= high:
                _find_in_scope(node.right, low, high)

        _find_in_scope(self.root, low, high)
        print()

    def inorder(self):
        def _inorder(node: Node):
            if node is None:
                return
            _inorder(node.left)
            print(node.value, end=' ')
            _inorder(node.right)
        _inorder(self.root)
        print()

    def preorder(self):
        def _preorder(node: Node):
            if node is None:
                return
            print(node.value, end=' ')
            _preorder(node.left)
            _preorder(node.right)
        _preorder(self.root)
        print()


if __name__ == "__main__":
    points = [5, 3, 8, 7, 10, 4, 2, 9, 6, 1]
    one_D_tree = OneDimentionTree()
    one_D_tree.make_tree(points)
    one_D_tree.inorder()
    one_D_tree.preorder()
    one_D_tree.find_in_scope(8, 10)
