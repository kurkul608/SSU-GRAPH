"""Алгоритм Флойда"""
"""Вывести кратчайшие пути из вершин u1 и u2 до v."""
"""W - вес ребер """
W =[
    [0, 4, 10, 2],
    [4, 0, 7, 7],
    [10, 7, 0, 11],
    [2, 11, 9, 0]
]
"""n - кол-во вершин"""
n = 4
print('Введите u1, u2, v')
u1, u2, v = map(int, input().split())
A = [[W[i][j] for j in range(n)] for i in range(n)]
B = [[W[i][j] for j in range(n)] for i in range(n)]

"""Данная реализация не подходит нам, тк могут быть отрицательные циклы"""
for k in range(n):
    for i in range(n):
        for j in range(n):
            B[i][j] = min(B[i][j], B[i][k] + B[k][j])




"""A - наикратчайшие пути для каждой из вершин"""
INF = 10 **10
Prev = [[None for j in range(n)] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if A[i][k] < INF and A[k][j] < INF and A[i][k] + A[k][j] < A[i][j]:
                A[i][j] = A[i][k] + A[k][j]
                Prev[i][j] = Prev[k][j]

Path = []
while j is not None:
    Path.append(j)
    j = Prev[i][j]
Path = Path[::-1]

print(Path)
print(A)
print(B)
for i in range(n):
    print(Prev[i])
for i in range(n):
    for j in range(n):
        if i == u1:
            if j == v:
                print('Кратчайший путь из ', i, ' в ', j, ' = ', A[i][j])
        if i == u2:
            if j == v:
                print('Кратчайший путь из ', i, ' в ', j, ' = ', A[i][j])
