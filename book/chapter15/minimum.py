class DisjointSet(object):
    def __init__(self, node_num: int):
        self.node_num = node_num
        self.element, self.rank = self.make_set()

    def make_set(self) -> tuple:
        element, rank = [], []
        for i in range(self.node_num):
            element.append(i)
            rank.append(0)

        return element, rank

    def find_set(self, element: int) -> int:
        if self.element[element] != element:
            self.element[element] = self.find_set(self.element[element])
        return self.element[element]

    def union(self, first_ele: int, second_ele: int) -> None:
        parent_first_ele = self.find_set(first_ele)
        parent_second_ele = self.find_set(second_ele)

        if self.rank[parent_first_ele] > self.rank[parent_second_ele]:
            self.element[parent_second_ele] = parent_first_ele
        else:
            self.element[parent_first_ele] = parent_second_ele
            if self.rank[parent_first_ele] == self.rank[parent_second_ele]:
                self.rank[parent_second_ele] += 1


class Kruskal(object):
    def __init__(self, edges: list, node_num: int):
        self.disjointset = DisjointSet(node_num)
        self.edges = sorted(edges, key=lambda edge: edge[2])

    def execute(self):
        minimum_tree_edges = []
        sum_weight = 0

        for node, adj_node, weight in self.edges:
            if self.disjointset.find_set(node) != self.disjointset.find_set(adj_node):
                self.disjointset.union(node, adj_node)
                minimum_tree_edges.append((node, adj_node, weight))
                sum_weight += weight

        return minimum_tree_edges, sum_weight


if __name__ == "__main__":
    edges = [(0, 1, 1), (0, 2, 3), (1, 2, 1), (1, 3, 7), (2, 4, 1),
             (1, 4, 3), (3, 4, 1), (3, 5, 1), (4, 5, 6)]

    kruskal = Kruskal(edges, 6)
    print(kruskal.execute())
