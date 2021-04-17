class Node(object):
    def __init__(self, value: float) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: float) -> None:
        def _insert(node: Node, value: float):
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)

            return node

        self.root = _insert(self.root, value)

    def remove(self, value: float) -> None:
        def _remove(node: Node, value: float):
            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                minvalue_in_right_node = self.min_value(node.right)
                node.value = minvalue_in_right_node
                node.right = _remove(node.right, minvalue_in_right_node)

            return node

        self.root = _remove(self.root, value)

    def min_value(self, node: Node) -> float:
        if node.left is None:
            return node.value
        else:
            return self.min_value(node.left)

    def find(self, left: int, right: int) -> list:
        ans = []

        def _find(node: Node, left: int, right: int):
            if left <= node.value <= right:
                ans.append(node.value)

            if node.left and left <= node.value:
                _find(node.left, left, right)
            if node.right and node.value <= right:
                _find(node.right, left, right)

        _find(self.root, left, right)
        return ans

    def preorder(self) -> None:
        def _preorder(node: Node):
            if node is None:
                return
            _preorder(node.left)
            print(node.value, end=' ')
            _preorder(node.right)
        _preorder(self.root)
        print()


def point_ajust(v: list, h: list) -> list:
    label_points = []

    for point in v:
        point[0].append(0)
        point[1].append(3)
        label_points.append(point[0])
        label_points.append(point[1])

    for point in h:
        point[0].append(1)
        point[1].append(2)
        label_points.append(point[0])
        label_points.append(point[1])

    label_points.sort(key=lambda ele: (ele[1], ele[2]))

    return label_points


def manhattan_geometry(v: list, h: list) -> int:
    points = point_ajust(v, h)
    label = {
        'bottom': 0,
        'left': 1,
        'right': 2,
        'top': 3
    }

    bst = BinarySearchTree()
    cross_point = []
    count = 0
    for i in range(len(points)):
        if points[i][2] == label['bottom']:
            bst.insert(points[i][0])
        elif points[i][2] == label['top']:
            bst.remove(points[i][0])
        elif points[i][2] == label['left']:
            for point in bst.find(points[i][0], points[i + 1][0]):
                cross_point.append([point, points[i][1]])
                count += 1

    return cross_point, count


if __name__ == "__main__":
    v = [([2, 2], [2, 5]), ([4, 1], [4, 4]),
         ([6, 1], [6, 3]), ([6, 5], [6, 7])]
    h = [([1, 3], [5, 3]), ([5, 2], [7, 2])]
    print(manhattan_geometry(v, h))
