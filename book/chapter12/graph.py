class Graph(object):
    def __init__(self, Adj_list: list):
        self.len_Adj = len(Adj_list)
        self.Adj = self.create_Adj(Adj_list)
        self.visiting = [0 for _ in range(self.len_Adj)]
        self.visited = [False for _ in range(self.len_Adj)]
        self.time = 0
        self.timestamp = [[0, 0] for _ in range(self.len_Adj)]

    def create_Adj(self, Adj_list: list) -> list:
        M = [[0] * len(Adj_list) for _ in range(len(Adj_list))]
        for a_list, m_list in zip(Adj_list, M):
            for a_index in a_list:
                m_list[a_index] = 1

        return M

    def next_node(self, current_node: int) -> int:
        for i in range(self.visiting[current_node], self.len_Adj):
            if self.Adj[current_node][i] and not self.visited[i]:
                self.visiting[current_node] = i
                return i
        return None

    def depth_first_search(self, first_node: int) -> None:
        stack = []
        time = 1
        stack.append(first_node)
        self.visited[first_node] = True
        self.timestamp[first_node][0] = time

        while stack:
            current_node = stack[-1]
            next_node = self.next_node(current_node)
            time += 1

            if next_node is not None:
                stack.append(next_node)
                self.visited[next_node] = True
                self.timestamp[next_node][0] = time
            else:
                self.timestamp[stack.pop()][1] = time

    def depth_first_search_recur(self, node: int) -> None:
        self.visited[node] = True
        self.time += 1
        self.timestamp[node][0] = self.time

        for i, adj in enumerate(self.Adj[node]):
            if adj and not self.visited[i]:
                self.depth_first_search_recur(i)

        self.time += 1
        self.timestamp[node][1] = self.time

    def breadth_first_search(self, first_node: int) -> list:
        distance = [0 for _ in range(self.len_Adj)]
        in_queue = [False for _ in range(self.len_Adj)]
        queue = []

        queue.append(first_node)
        in_queue[first_node] = True
        while queue:
            current_node = queue.pop(0)
            for i, adj in enumerate(self.Adj[current_node]):
                if adj and not in_queue[i]:
                    queue.append(i)
                    in_queue[i] = True
                    distance[i] = distance[current_node] + 1

        return distance


def depth_first_search(adj_list: list, first_node: int) -> list:
    visited = [False for _ in range(len(adj_list))]
    visited[first_node] = True
    trail = []

    def _depth_first_search(current_node):
        visited[current_node] = True
        trail.append(current_node)

        for next_node in adj_list[current_node]:
            if not visited[next_node]:
                _depth_first_search(next_node)

        return trail

    return _depth_first_search(first_node)


def breadth_first_search(adj_list: list, first_node: int) -> list:
    queue = []
    visited = [False for _ in range(len(adj_list))]
    trail = []

    queue.append(first_node)
    visited[first_node] = True

    while queue:
        current_node = queue.pop(0)
        trail.append(current_node)

        for next_node in adj_list[current_node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

    return trail


if __name__ == "__main__":
    A = [
        [1, 2, 4],
        [0, 2, 3],
        [0, 1, 3, 4, 5, 6],
        [1, 2, 6],
        [0, 2],
        [2, 6],
        [2, 3, 5]
    ]

    # g = Graph(A)
    # g.depth_first_search(0)
    # print(f'stack {g.timestamp}')
    # g.depth_first_search_recur(0)
    # print(f'recur {g.timestamp}')
    # print(f'breadth {g.breadth_first_search(0)}')
    # print(depth_first_search(A, 0))
    print(breadth_first_search(A, 0))
