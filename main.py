
class Graph(object):

    def __init__(self, graph_dict=None):
        """ Иницилизирует граф, если нет словаря, то создается пустой граф
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ Возвращает список вершин графа """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ Возвращает вершины графа """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ если вершина vertex отсутствует в словаре, то в граф добавляется новая вершина
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ Добавляет ребро
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ генерирует ребра
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def delete_vertex(self, vertex):
        """ Удаляет вершину по ключу"""
        r = self.__graph_dict
        r.pop(vertex, 1000)
        return r

    def remove_edge(self, edge):
        """Удаление ребра"""
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)


        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].remove(vertex2)
        # if vertex2 in self.__graph_dict:
        #     self.__graph_dict[vertex2].remove(vertex1)



    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


# if __name__ == "__main__":
#     g = {"a": ["d"],
#          "b": ["c"],
#          "c": ["b", "c", "d", "e"],
#          "d": ["a", "c"],
#          "e": ["c"],
#          "f": []
#          }
#
#     graph = Graph(g)
#
#     print("Вершины графа:")
#     print(graph.vertices())
#
#     print("Ребра графа:")
#     print(graph.edges())
#
#     print("Добавили вершину: 'z")
#     graph.add_vertex("z")
#
#     print("Добавили вершину: 'x")
#     graph.add_vertex("x")
#
#     print("Вершины графа:")
#     print(graph.vertices())
#
#     print("Добавили ребро: 'a, z'")
#     graph.add_edge({"a", "z"})
#
#     print("Вершины графа:")
#     print(graph.vertices())
#
#     print("Ребра графа:")
#     print(graph.edges())
#
#     print('Добавили ребро {"x","y"} с новыми вершинами:')
#     graph.add_edge({"x", "y"})
#     print("Вершины графа:")
#     print(graph.vertices())
#     print("Ребра графа:")
#     print(graph.edges())
#
#     print("Удаляем вершину 'z'")
#     print(graph.delete_vertex('z'))
#     # print()
#     # graph.pop('z', 0)
#     print("Вершины графа:")
#     print(graph.vertices())
#
#     print("Ребра графа:")
#     print(graph.edges())
#
#     print("Удаление ребра {x, y}")
#     print(graph.remove_edge({"x", "y"}))
#     print("Ребра графа:")
#     print(graph.edges())
#     print("Вершины графа:")
#     print(graph.vertices())
