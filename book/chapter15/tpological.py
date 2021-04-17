class TopologocalSort(object):
    def __init__(self, g: list):
        self.g = g
        self.node_num = len(g)

    def breadth(self):
        indegree = [0] * self.node_num
        for edges in self.g:
            for edge in edges:
                indegree[edge] += 1

        sort_ans = []
        queue = []

        for node in range(self.node_num):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.pop(0)
            sort_ans.append(node)

            for adj_node in self.g[node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)

        return sort_ans

    def depth(self):
        visited = [False for _ in range(self.node_num)]
        sort_ans = []

        def _depth(node):
            visited[node] = True
            for adj_node in self.g[node]:
                if not visited[adj_node]:
                    _depth(adj_node)
            sort_ans.append(node)

        for node in range(self.node_num):
            if not visited[node]:
                _depth(node)

        sort_ans.reverse()
        return sort_ans


if __name__ == "__main__":
    g = [[1], [2], [], [1, 4], [5], [2]]
    topo = TopologocalSort(g)
    # print(topo.breadth())
    print(topo.depth())
