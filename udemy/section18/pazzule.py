from typing import List
import random
import heapq
import sys


def hanoi(disk: int, src: str, dest: str, rest: str):
    r = []

    def _hanoi(disk: int, src: str, dest: str, rest: str):
        if disk < 1:
            return

        _hanoi(disk - 1, src=src, dest=rest, rest=dest)
        r.append((disk, src, dest))
        _hanoi(disk - 1, src=rest, dest=dest, rest=src)

    _hanoi(disk, src, dest, rest)
    return r


def pascal(depth: int):
    element_num = 2 * depth - 1
    triangle = [[0] * element_num for _ in range(depth)]
    mid = depth - 1

    for line in range(len(triangle)):
        if line == 0:
            triangle[line][mid] = 1
            continue

        for i in range(mid + 1):
            left = mid - i
            right = mid + i

            if left - 1 < 0 and element_num - 1 < right + 1:
                triangle[line][left] = triangle[line - 1][left + 1]
                triangle[line][right] = triangle[line - 1][right - 1]
                continue

            triangle[line][left] = \
                triangle[line - 1][left - 1] + triangle[line - 1][left + 1]
            triangle[line][right] = \
                triangle[line - 1][right - 1] + triangle[line - 1][right + 1]

    return triangle


def triangle_display(triangle: List[List[int]]):
    for line in triangle:
        for num in line:
            if num == 0:
                print(' ', end=' ')
            else:
                print(num, end=' ')
        print()


def generate_pascal_triangle(depth: int) -> List[List[int]]:
    data = [[1] * (i + 1) for i in range(depth)]

    for line in range(2, depth):
        for i in range(1, line):
            data[line][i] = data[line - 1][i - 1] + data[line - 1][i]

    return data


def print_pascal(data: List[int]) -> None:
    max_digit = len(str(max(data[-1])))
    width = max_digit + (max_digit % 2) + 2
    for index, line in enumerate(data):
        nums = ''.join([str(i).center(width, ' ') for i in line])
        print((' ' * int(width / 2)) * (len(data) - index), nums)


def generate_triangle(depth: int, max_num: int):
    return [[random.randint(0, max_num) for _ in range(i)] for i in range(1, depth + 1)]


def min_path_of_triangle(triangle: List[List[int]]) -> int:
    depth = len(triangle)
    distance = [[sys.maxsize for _ in range(i)] for i in range(1, depth + 1)]
    visited = [[False for _ in range(i)] for i in range(1, depth + 1)]

    distance[0][0] = triangle[0][0]
    visited[0][0] = True

    heap = []
    # (distance, line, index)
    heapq.heappush(heap, (distance[0][0], 0, 0))

    while heap:
        dis, line, index = heapq.heappop(heap)
        visited[line][index] = True

        if line == depth - 1:
            continue

        for i in range(2):
            next_dis = dis + triangle[line + 1][index + i]
            if not visited[line + 1][index + i] and distance[line + 1][index + i] > next_dis:
                distance[line + 1][index + i] = next_dis
                heapq.heappush(heap, (next_dis, line + 1, index + i))

    return distance


def sum_min_path(triangle):
    tree_sum = triangle[:]
    j, len_triangle = 1, len(triangle)
    if not len_triangle:
        return

    while j < len_triangle:
        line = triangle[j]
        line_path_sum = []
        for i, value in enumerate(line):
            if i == 0:
                sum_value = line[i] + tree_sum[j - 1][0]
            elif i == len(line) - 1:
                sum_value = line[i] + tree_sum[j - 1][i - 1]
            else:
                min_path = min(tree_sum[j - 1][i - 1], tree_sum[j - 1][i])
                sum_value = line[i] + min_path
            line_path_sum.append(sum_value)
        tree_sum[j] = line_path_sum
        j += 1

    return min(tree_sum[-1])


if __name__ == "__main__":
    triangle = generate_triangle(5, 10)
    print_pascal(triangle)
    d = min_path_of_triangle(triangle)
    print(d)
    print(f'min path: {min(d[-1])}')
