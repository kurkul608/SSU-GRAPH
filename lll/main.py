"""Краскал"""



print('Введите количество вершин и ребер')
N, M = map(int, input().split())
Edges = []
for i in range(M):
    print('начальную вершину ребра, конечную, вес ребра', i)
    start, end, weight = map(int, input().split())
    Edges.append([weight, start, end])
Edges.sort()
Comp = [i for i in range(N)]
Ans = 0
print('Ребра минимального каркаса:')
for weight, start, end in Edges:
    if Comp[start] != Comp[end]:
        Ans += weight
        a = Comp[start]
        b = Comp[end]
        print("[", start, ', ', end, ']')
        for i in range(N):
            if Comp[i] == b:
                Comp[i] = a


print('Вес минимального каркаса: ', Ans)