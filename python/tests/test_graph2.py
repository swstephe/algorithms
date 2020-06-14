# -*- coding: utf-8 -*-
from graph2 import Graph


def test_one():
    graph = Graph(a='bc', b='ade', c='af', d='b', e='bf', f='ce')
    assert graph.vertices == ('a', 'b', 'c', 'd', 'e', 'f')
    assert graph.edges == (
        ('a', 'b'),
        ('a', 'c'),
        ('b', 'a'),
        ('b', 'd'),
        ('b', 'e'),
        ('c', 'a'),
        ('c', 'f'),
        ('d', 'b'),
        ('e', 'b'),
        ('e', 'f'),
        ('f', 'c'),
        ('f', 'e')
    )
    assert graph.depth_first('a') == {'a', 'b', 'c', 'd', 'e', 'f'}
    assert tuple(sorted(graph.depth_first_paths('a', 'e'))) == (
        ['a', 'b', 'e'],
        ['a', 'c', 'f', 'e']
    )
    assert graph.breadth_first('a') == {'a', 'b', 'c', 'd', 'e', 'f'}
    assert tuple(sorted(graph.breadth_first_paths('a', 'e'))) == (
        ['a', 'b', 'e'],
        ['a', 'c', 'f', 'e']
    )
    assert graph.dijkstra('a', 'e') == (2, ['a', 'b', 'e'])
    assert graph.a_star('a', 'e') == (2, ['a', 'b', 'e'])
    assert graph.greedy_best_first('a', 'e') == ['a', 'b', 'e']
    assert graph.warshall('a', 'e') == [2, ('a', 'b', 'e')]


def test_two():
    g = (
        (0, 4, 0, 0, 0, 0, 0, 8, 0),    # 0
        (4, 0, 8, 0, 0, 0, 0, 11, 0),   # 1
        (0, 8, 0, 7, 0, 4, 0, 0, 2),    # 2
        (0, 0, 7, 0, 9, 14, 0, 0, 0),   # 3
        (0, 0, 0, 9, 0, 10, 0, 0, 0),   # 4
        (0, 0, 4, 14, 10, 0, 2, 0, 0),  # 5
        (0, 0, 0, 0, 0, 2, 0, 1, 6),    # 6
        (8, 11, 0, 0, 0, 0, 1, 0, 7),   # 7
        (0, 0, 2, 0, 0, 0, 6, 7, 0)     # 8
    )
    rows = len(g)
    cols = len(g[0])
    assert rows == cols
    graph = Graph()
    for row in range(rows):
        graph[row] = set(col for col in range(cols) if g[row][col] != 0)
    assert len(graph.vertices) == rows
    assert len(graph.edges) == sum(
        len(list(col for col in range(cols) if g[row][col] != 0))
        for row in range(rows)
    )

    def heuristic(a, b):
        return g[a][b]

    assert graph.dijkstra(0, 0, heuristic)[0] == 0
    assert graph.dijkstra(0, 1, heuristic)[0] == 4
    assert graph.dijkstra(0, 2, heuristic)[0] == 12
    assert graph.dijkstra(0, 3, heuristic)[0] == 19
    assert graph.dijkstra(0, 4, heuristic)[0] == 21
    assert graph.dijkstra(0, 5, heuristic)[0] == 11
    assert graph.dijkstra(0, 6, heuristic)[0] == 9
    assert graph.dijkstra(0, 7, heuristic)[0] == 8
    assert graph.dijkstra(0, 8, heuristic)[0] == 14
