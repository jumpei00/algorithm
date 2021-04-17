def breadth_first_search(graph: list, first_node: int):
    node_num = len(graph)
    node = first_node

    def _breadth_first_search(graph: list, node: int):
        queue = []
        distance = [None] * node_num

        queue.append(node)
        distance[node] = 0

        while queue:
            current_node = queue.pop(0)
            for adj_node, weight in graph[current_node]:
                if distance[adj_node] is None:
                    distance[adj_node] = distance[current_node] + weight
                    queue.append(adj_node)

        max_distance = max(distance)

        return distance.index(max_distance), max_distance

    pair = []
    for _ in range(2):
        node, distance = _breadth_first_search(graph, node)
        pair.append(node)

    return pair, distance


if __name__ == "__main__":
    graph = [[(1, 2)], [(0, 2), (3, 3), (2, 1)], [(1, 1)], [(1, 3)]]
    print(breadth_first_search(graph, 1))
