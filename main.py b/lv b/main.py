"""Алгоритм Флойда"""

"""W - вес ребер """
W =[
    [4, 10, 2],
    [4, 7, 7],
    [10, 7, 11]
    # [2, 11, 9]
]
"""n - кол-во вершин"""
n = 3
A = [[W[i][j] for j in range(n)] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            A[i][j] = min(A[i][j], A[i][k] + A[k][j])
"""A - наикратчайшие пути для каждой из вершин"""
print(A)
for i in range(n):
    for j in range(n):
        if i != j:
            print('Кратчайший путь из ', i, ' в ', j, ' = ',  A[i][j])