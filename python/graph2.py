# -*- coding: utf-8 -*-
from collections import defaultdict, deque
import math

from heap2 import MinHeap


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

    def greedy_best_first(self, start, goal, heuristic=lambda a, b: 1):
        key_func = lambda x: heuristic(x, goal)
        visited = {}
        queue = deque([(start, [start])])
        while queue:
            vertex, path = queue.popleft()
            if vertex in visited:
                continue
            visited[vertex] = path
            if vertex == goal:
                break
            for neighbor in sorted(self[vertex], key=key_func):
                queue.append((neighbor, path + [neighbor]))
        return visited[goal]

    def dijkstra(self, start, goal, heuristic=lambda a, b: 1):
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
                heap.push((
                    distance + heuristic(vertex, neighbor),
                    neighbor,
                    path + [neighbor]
                ))
        return visited[goal]

    def a_star(self, start, goal, heuristic=lambda a, b: 1):
        visited = {}
        heap = MinHeap((0, start, [start]))
        while heap:
            score, vertex, path = heap.pop()
            if vertex in visited:
                continue
            visited[vertex] = score, path
            if vertex == goal:
                break
            for neighbor in self[vertex]:
                heap.push((
                    score + heuristic(neighbor, goal),
                    neighbor,
                    path + [neighbor]
                ))
        return visited[goal]

    def warshall(self, start, goal):
        dist = {}
        for v1 in self:
            dist[v1] = {}
            for v2 in self:
                dist[v1][v2] = [0 if v1 == v2 else math.inf, (v1, v2)]
        for v1, v2 in self.edges:
            dist[v1][v2][0] = 1
        for v1 in self:
            for v2 in self:
                for v3 in self:
                    d = dist[v2][v1][0] + dist[v1][v3][0]
                    if dist[v2][v3][0] > d:
                        dist[v2][v3] = [d, dist[v2][v1][1][:-1] + dist[v1][v3][1]]
        return dist[start][goal]
