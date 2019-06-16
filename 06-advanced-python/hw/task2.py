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
        self.prev_elems = []
        self.next_elems = deque()
        self.next_elems += [tuple(self.E.keys())[0]]
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
        


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertice in graph:
    print(vertice)
