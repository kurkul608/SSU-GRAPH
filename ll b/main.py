
"""Список смежности"""
g = [
    [1, 2],
    [0, 3],
    [0, 3],
    [2, 1]
]
"""Кол-во вершин, начинается с 0"""
n = 3

visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)
prev1 = [None] * (n + 1)
prev2 = [None] * (n + 1)
def dfs(start, visited, prev, g):
    visited[start] = True
    for u in g[start]:
        if not visited[u]:
            prev[u] = start
            dfs(u, visited, prev, g)



print('Введите u1, u2 и v')
u1, u2, v = map(int, input().split())


"""Найдем все пути из u1 в остальные вершины"""
dfs(u1, visited1, prev1, g)

"""Найдем все пути из u2  в остальные вершины """
dfs(u2, visited2, prev2, g)

if prev1[v] <= prev2[v]:
    print("Путь из u1 в v короче")
else:
    print("Путь из u2  в v короче")

