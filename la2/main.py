



"""Список смежности"""
g = [
    [2, 4],
    [],
    [1],
    [2],
    [1, 3],
    [0, 4]
]
"""Счетчик полустепеней"""
counter = 0
"""Кол-во вершина графа"""
n = 4

print("Введите вершину, для которой будем считать степень полузахода")
index = input()
index = int(index)
for i in range(n+2):
    for m in g[i]:
        if i != index:
            if m == index:
                counter = counter + 1

print('Полустепень захода в вершину ', index, '= ', counter)