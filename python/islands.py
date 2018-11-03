# -*- coding: utf8 -*-


class Graph(object):
    def __init__(self, graph):
        self.graph = graph
        self.rows = len(graph)
        self.cols = len(graph[0])

    def __str__(self):
        return 'Graph(%d, %d)' % (self.rows, self.cols)

    def depth_first_search(self, r, c, visited):
        visited[r][c] = True
        for r1, c1 in (
            (r0, c0)
            for r0 in range(max(r - 1, 0), min(r + 2, self.rows))
            for c0 in range(max(c - 1, 0), min(c + 2, self.cols))
            if (r != r0 or c != c0) and not visited[r0][c0] and self.graph[r0][c0] == 1
        ):
            self.depth_first_search(r1, c1, visited)

    def count_islands(self):
        visited = list(list(False for _ in range(self.cols)) for _ in range(self.rows))
        count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if not visited[r][c] and self.graph[r][c] == 1:
                    self.depth_first_search(r, c, visited)
                    count += 1
        return count
