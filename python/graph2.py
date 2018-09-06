# -*- coding: utf-8 -*-
from collections import defaultdict, deque
import math

from heap import MinHeap


class Graph(defaultdict):
    def __init__(self, **kwargs):
        super(Graph, self).__init__(set)
        for vertex, neighbors in kwargs.items():
            for neighbor in neighbors:
                self[vertex].add(neighbor)

    @property
    def edges(self):
        return tuple(
            (vertex, neighbor)
            for vertex in sorted(self)
            for neighbor in sorted(self[vertex])
        )

    @property
    def vertices(self):
        return tuple(sorted(self))

    def __str__(self):
        return 'vertices: {}\nedges: {}'.format(
            ' '.join(str(v) for v in self.vertices),
            ' '.join('%s->%s' % e for e in self.edges)
        )

    def depth_first(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for vertex in self[start] - visited:
            self.depth_first(vertex, visited)
        return visited

    def depth_first_paths(self, start, goal, path=None):
        if path is None:
            path = [start]
        if start == goal:
            yield path
        for _next in self[start] - set(path):
            for p in self.depth_first_paths(_next, goal, path + [_next]):
                yield p

    def breadth_first(self, start):
        visited = set()
        queue = deque(start)
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(self[vertex] - visited)
        return visited

    def breadth_first_paths(self, start, goal):
        queue = deque([(start, [start])])
        while queue:
            vertex, path = queue.popleft()
            for _next in self[vertex] - set(path):
                if _next == goal:
                    yield path + [_next]
                else:
                    queue.append((_next, path + [_next]))

    def dijkstra(self, start, goal):
        visited = {}
        heap = MinHeap((0, start, [start]))
        while heap:
            distance, vertex, path = heap.pop()
            if vertex in visited:
                continue
            visited[vertex] = distance, path
            if vertex == goal:
                break
            for neighbor in self[vertex]:
                heap.push((distance + 1, neighbor, path + [neighbor]))
        return visited[goal]

    def a_star(self, start, goal):
        def heuristic(node1, node2):
            return 1
        visited = set()
        g_score = dict((v, 0 if v == start else None) for v in self)
        f_score = dict((v, heuristic(start, goal) if v == start else None) for v in self)
        heap = MinHeap((f_score[start], start, [start]))
        while heap:
            score, vertex, path = heap.pop()
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in self[vertex]:
                if neighbor in visited:
                    continue
                heap.push((score + heuristic(neighbor, goal), neighbor, path + [neighbor]))

    def warshall(self, start, goal):
        dist = defaultdict(dict)
        for u in self:
            for v in self:
                dist[u][v] = [0 if u == v else math.inf, (u, v)]
        for a, b in self.edges:
            dist[a][b][0] = 1
        for k in self:
            for i in self:
                for j in self:
                    d = dist[i][k][0] + dist[k][j][0]
                    if dist[i][j][0] > d:
                        dist[i][j] = [d, dist[i][k][1][:-1] + dist[k][j][1]]
        return dist[start][goal]


# GRAPH = Graph(a=['c'], b=['c', 'e'], c=['a', 'b', 'd', 'e'], d=['c'], e=['c', 'b'], f=[])
GRAPH = Graph(a=['b', 'c'], b=['a', 'd', 'e'], c=['a', 'f'], d=['b'], e=['b', 'f'], f=['c', 'e'])

print(GRAPH)
print('depth_first', GRAPH.depth_first('a'))
print('depth_first_paths', list(GRAPH.depth_first_paths('a', 'e')))
print('breadth_first', GRAPH.breadth_first('a'))
print('breadth_first_paths', list(GRAPH.breadth_first_paths('a', 'e')))
print('dijkstra', GRAPH.dijkstra('a', 'e'))
# print('a_star', GRAPH.a_star('a', 'e'))
print('warshall', GRAPH.warshall('a', 'e'))
