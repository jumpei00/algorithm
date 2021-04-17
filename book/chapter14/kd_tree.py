class Node(object):
    def __init__(self, point: tuple):
        self.point = point
        self.left = None
        self.right = None


class KDTree(object):
    def __init__(self):
        self.root = None

    def make_tree(self, points: list):
        def _make_tree(points: list, depth=0):
            if not points:
                return None

            dimention = len(points[0])
            axis = depth % dimention

            points.sort(key=lambda point: point[axis])

            mid_index = len(points) // 2
            node = Node(points[mid_index])
            node.left = _make_tree(points[:mid_index], depth + 1)
            node.right = _make_tree(points[mid_index + 1:], depth + 1)

            return node

        self.root = _make_tree(points)

    def find_in_scope(self, scope: list):
        def _find_in_scope(node: Node, scope: list, depth=0):
            # scope -> [(x_low, x_high), (y_low, y_high), (z_low, z_high), ....]

            dimention = len(scope)
            axis = depth % dimention

            for i in range(dimention):
                low = scope[i][0]
                high = scope[i][1]
                if not (low <= node.point[i] <= high):
                    break
            else:
                print(node.point, end=' ')

            if node.left and scope[axis][0] <= node.point[axis]:
                _find_in_scope(node.left, scope, depth + 1)
            if node.right and node.point[axis] <= scope[axis][1]:
                _find_in_scope(node.right, scope, depth + 1)

        _find_in_scope(self.root, scope)
        print()

    def inorder(self):
        def _inorder(node: Node):
            if node is None:
                return
            _inorder(node.left)
            print(node.point, end=' ')
            _inorder(node.right)
        _inorder(self.root)
        print()


if __name__ == "__main__":
    points = [(0, 9), (1, 4), (2, 2), (6, 7), (3, 1),
              (5, 3), (9, 8), (10, 14), (11, 12),
              (14, 13), (7, 15), (13, 10)]
    kdtree = KDTree()
    kdtree.make_tree(points)
    print(kdtree.root.point)
    kdtree.inorder()
    kdtree.find_in_scope([(6, 13), (6, 13)])
