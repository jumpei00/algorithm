class DisjointSet(object):
    def __init__(self, num: int):
        self.elements, self.rank = self.make_set(num)

    def make_set(self, num: int):
        elements = []
        rank = []
        for i in range(num):
            elements.append(i)
            rank.append(0)

        return elements, rank

    def find_set(self, element: int) -> int:
        if self.elements[element] == element:
            return element
        else:
            self.elements[element] = self.find_set(self.elements[element])
            return self.elements[element]

    def union(self, x: int, y: int):
        parent_x = self.find_set(x)
        parent_y = self.find_set(y)
        if self.rank[parent_x] > self.rank[parent_y]:
            self.elements[parent_y] = parent_x
        elif self.rank[parent_x] < self.rank[parent_y]:
            self.elements[parent_x] = parent_y
        elif parent_x != parent_y:
            self.elements[parent_x] = parent_y
            self.rank[parent_y] += 1

    def is_same(self, x: int, y: int) -> bool:
        return self.find_set(x) == self.find_set(y)


if __name__ == "__main__":
    ds = DisjointSet(10)
    ds.union(0, 1)
    ds.union(0, 2)
    ds.union(8, 9)
    ds.union(7, 9)
    ds.union(1, 9)
    print(ds.elements)
    print(ds.rank)
