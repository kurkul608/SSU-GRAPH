"""Построить орграф, являющийся дополнением данного орграфа."""

g = [
    [2, 3],
    [5, 3],
    [1],
    [5, 2],
    [1, 3, 4]
]

n = 4

""""""
print("Список смежности доп графа")
for i in range(n+1):
    if len(g[i]) > 1:
        print(g[i][len(g[i]) - 1])