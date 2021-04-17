import sys

N = int(input())
R = []
for _ in range(N):
    R.append(int(input()))

min_value = R[0]
total_max_value = -sys.maxsize
for i in range(1, N):
    total_max_value = max(total_max_value, R[i] - min_value)
    min_value = min(min_value, R[i])

print(f'ans: {total_max_value}')
