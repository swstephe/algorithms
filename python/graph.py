# -*- coding: utf-8 -*-

GRAPH = {
    'a': ['c'],
    'b': ['c', 'e'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['c'],
    'e': ['c', 'b'],
    'f': [],
}


def generate_edges(graph):
    for node in graph:
        for neighbor in graph[node]:
            yield node, neighbor


print(list(generate_edges(GRAPH)))
