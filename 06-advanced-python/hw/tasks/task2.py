"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""
from collections import deque


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        return GraphIterator(self)


class GraphIterator:
    def __init__(self, graph):
        self.E = graph.E
        self.prev_elems = []
        self.next_elems = deque()
        self.next_elems += [tuple(self.E.keys())[0]]

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_elems:
            top = self.next_elems.popleft()
            if top not in self.prev_elems:
                for element in self.E[top]:
                    if (element not in self.prev_elems
                        and element not in self.next_elems):
                        self.next_elems += element
                self.prev_elems.append(top)
                return top
        else:
            raise StopIteration()

          
if __name__ == '__main__':
    E = {'A': ['B'], 'B': ['C'], 'C': ['H', 'N'], 'D': ['A'], 'H': ['D'], 'N': []}
    graph = Graph(E)
    for vertice in graph:
        print(vertice)
