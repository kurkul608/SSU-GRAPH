"""Алгоритм Дейкстра"""
"""Определить множество вершин орграфа, расстояние от которых до заданной вершины не более N."""

w =[
    [4, 10, 2],
    [4, 7, 7],
    [10, 7, 11]
    # [2, 11, 9]
]
"""n - кол-во вершин"""
n = 3
print('Введите начальную вершину и ограничение')
start, N = map(int, input().split())

INF = 10 ** 10
dist = [INF] * n
dist[start] = 0
used = [False] * n
min_dist = 0
min_vertex = start
while min_dist < INF:
    i = min_vertex
    used[i] = True
    for j in range(n):
        if dist[i] + w[i][j] < dist[j]:
            dist[j] = dist[i] + w[i][j]
            min_dist = INF
for j in range(n):
    if not used[j] and dist[j] < min_dist:
        min_dist = dist[j]
        min_vertex = j

for i in range(n):
    if i != start:
        if dist[i] <= N:
            print('Длина до вершины ', i, ' = ', dist[i])