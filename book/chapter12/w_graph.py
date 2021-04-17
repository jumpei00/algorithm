import sys
import heapq


class Graph(object):
    def __init__(self, adj: list):
        self.adj = adj

    def adj_to_adjlist(self, adj: list) -> list:
        adj_list = []
        for node_list in adj:
            r = []
            for node, weight in enumerate(node_list):
                if weight:
                    r.append((node, weight))
            adj_list.append(r)

        return adj_list

    def prim(self, first_node: int):
        len_adj = len(self.adj)
        mst_edge = [sys.maxsize for _ in range(len_adj)]
        parent = [-1 for _ in range(len_adj)]
        visited = [False for _ in range(len_adj)]

        mst_edge[first_node] = 0
        while True:
            # 最小コストのNodeに移動する(これはMSTにNodeを追加することを意味している)
            min_cost = sys.maxsize
            for node in range(len_adj):
                if not visited[node] and mst_edge[node] < min_cost:
                    current_node = node
                    min_cost = mst_edge[node]

            if min_cost == sys.maxsize:
                break

            visited[current_node] = True

            # 今いるNodeに隣接しているNodeの最短コストを計算する
            for node in range(len_adj):
                if self.adj[current_node][node] and not visited[node]:
                    if mst_edge[node] > self.adj[current_node][node]:
                        mst_edge[node] = self.adj[current_node][node]
                        parent[node] = current_node

        return mst_edge, parent

    def prim_priority_queue(self, first_node: int) -> list:
        len_adj = len(self.adj)
        adj_list = self.adj_to_adjlist(self.adj)

        visited = [False] * len_adj
        mst_edge = [sys.maxsize] * len_adj

        mst_edge[first_node] = 0
        heap = [(mst_edge[first_node], first_node)]

        while heap:
            current_node = heapq.heappop(heap)[1]
            visited[current_node] = True

            for node, weight in adj_list[current_node]:
                if not visited[node] and mst_edge[node] > weight:
                    mst_edge[node] = weight
                    heapq.heappush(heap, (weight, node))

        return mst_edge

    def dijkstra(self, first_node: int):
        len_adj = len(self.adj)
        mst_edge = [sys.maxsize for _ in range(len_adj)]
        parent = [-1 for _ in range(len_adj)]
        visited = [False for _ in range(len_adj)]

        mst_edge[first_node] = 0
        while True:
            # 最小コストのNodeに移動する(これはMSTにNodeを追加することを意味している)
            min_cost = sys.maxsize
            for node in range(len_adj):
                if not visited[node] and mst_edge[node] < min_cost:
                    current_node = node
                    min_cost = mst_edge[node]

            if min_cost == sys.maxsize:
                break

            visited[current_node] = True

            # 今いるNodeに隣接しているNodeの最短コストを計算する
            for node in range(len_adj):
                if self.adj[current_node][node] and not visited[node]:
                    # 今まで通ってきた経路と今記録されているコストを比較する
                    if mst_edge[node] > self.adj[current_node][node] + mst_edge[current_node]:
                        mst_edge[node] = self.adj[current_node][node] + \
                            mst_edge[current_node]
                        parent[node] = current_node

        return mst_edge, parent

    def dijkstra_priority_queue(self, first_node: int) -> list:
        len_adj = len(self.adj)
        adj_list = self.adj_to_adjlist(self.adj)

        visited = [False] * len_adj
        distance = [sys.maxsize] * len_adj

        distance[first_node] = 0
        heap = [(distance[first_node], first_node)]

        while heap:
            current_node = heapq.heappop(heap)[1]
            visited[current_node] = True

            for node, weight in adj_list[current_node]:
                if not visited[node] and distance[node] > distance[current_node] + weight:
                    distance[node] = distance[current_node] + weight
                    heapq.heappush(heap, (distance[node], node))

        return distance


def adj_to_adjlist(adj: list) -> list:
    adj_list = []
    for node_list in adj:
        r = []
        for node, weight in enumerate(node_list):
            if weight:
                r.append((node, weight))
        adj_list.append(r)

    return adj_list


def prim(adj_list: list, first_node: int) -> list:
    visited = [False] * len(adj_list)
    edge = [sys.maxsize] * len(adj_list)
    heap = []

    heapq.heappush(heap, (0, first_node))
    edge[first_node] = 0
    while heap:
        cost, current_node = heapq.heappop(heap)
        visited[current_node] = True
        for next_node, weight in adj_list[current_node]:
            if not visited[next_node] and edge[next_node] > weight:
                edge[next_node] = weight
                heapq.heappush(heap, (weight, next_node))

    return edge


def dijkstra(adj_list: list, first_node: int) -> list:
    visited = [False] * len(adj_list)
    distance = [sys.maxsize] * len(adj_list)
    heap = []

    heapq.heappush(heap, (0, first_node))
    distance[first_node] = 0

    while heap:
        current_dis, current_node = heapq.heappop(heap)
        visited[current_node] = True

        for next_node, weight in adj_list[current_node]:
            if not visited[next_node] and distance[next_node] > current_dis + weight:
                distance[next_node] = current_dis + weight
                heapq.heappush(heap, (distance[next_node], next_node))

    return distance


if __name__ == "__main__":
    adj = [
        [0, 10, 3, 0, 18, 11, 0],
        [10, 0, 5, 1, 0, 0, 0],
        [3, 5, 0, 2, 0, 7, 5],
        [0, 1, 2, 0, 0, 0, 2],
        [18, 0, 0, 0, 0, 1, 0],
        [11, 0, 7, 0, 1, 0, 2],
        [0, 0, 5, 2, 0, 2, 0]
    ]
    print(dijkstra(adj_to_adjlist(adj), 0))

    # g = Graph(adj)
    # print(g.prim(0))
    # print(g.dijkstra(0))
    # print(g.prim_priority_queue(0))
    # print(g.dijkstra_priority_queue(0))
