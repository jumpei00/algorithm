import sys


def articulation_point(graph: list, first_node: int):
    node_num = len(graph)
    visited = [False] * node_num
    order = [0] * node_num
    lowlink = [sys.maxsize] * node_num

    is_articulation_node = [False] * node_num

    def _articulation_point(current_node: int, parent_node: int, node: int):
        order[current_node] = lowlink[current_node] = node
        visited[current_node] = True

        indegree_count = 0

        for adj_node in graph[current_node]:
            if not visited[adj_node]:
                indegree_count += 1

                node = _articulation_point(adj_node, current_node, node + 1)
                lowlink[current_node] = min(
                    lowlink[current_node], lowlink[adj_node])

                if parent_node >= 0 and order[current_node] <= lowlink[adj_node]:
                    is_articulation_node[current_node] = True

            # ここに当てはまるものは後退辺となる
            elif adj_node != parent_node:
                lowlink[current_node] = min(
                    lowlink[current_node], order[adj_node])

        if parent_node == -1 and indegree_count >= 2:
            is_articulation_node[current_node] = True

        return node

    _articulation_point(first_node, -1, 1)

    print(order, lowlink)
    return is_articulation_node


if __name__ == "__main__":
    g = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2, 4, 5],
         [3], [3, 6, 7], [5, 7], [5, 6]]

    r = articulation_point(g, 3)
    print(r)
    for i, node in enumerate(r):
        if node:
            print(i, end=' ')
