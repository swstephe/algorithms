# -*- coding: utf8 -*-
from islands import Graph


def test0():
    g = Graph((
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0)
    ))
    assert g.rows == 5
    assert g.cols == 5
    assert g.count_islands() == 0


def test1():
    g = Graph(((0,),))
    assert g.rows == 1
    assert g.cols == 1
    assert g.count_islands() == 0
    g = Graph(((1,),))
    assert g.rows == 1
    assert g.cols == 1
    assert g.count_islands() == 1


def test1a():
    g = Graph((
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0)
    ))
    assert g.rows == 5
    assert g.cols == 5
    assert g.count_islands() == 1


def test1b():
    g = Graph((
        (1, 1, 0, 0, 0),
        (1, 1, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0)
    ))
    assert g.rows == 5
    assert g.cols == 5
    assert g.count_islands() == 1


def test1c():
    g = Graph((
        (1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1)
    ))
    assert g.rows == 5
    assert g.cols == 5
    assert g.count_islands() == 1


def test1d():
    g = Graph((
        (0, 0, 0, 0, 0),
        (0, 1, 1, 1, 0),
        (0, 1, 0, 1, 0),
        (0, 1, 1, 1, 0),
        (0, 0, 0, 0, 0)
    ))
    assert g.rows == 5
    assert g.cols == 5
    assert g.count_islands() == 1


def test2():
    g = Graph((
        (0, 0, 0, 0, 0),
        (1, 1, 0, 1, 1),
        (0, 1, 0, 1, 0),
        (1, 1, 0, 1, 1),
        (0, 0, 0, 0, 0)
    ))
    assert g.rows == 5
    assert g.cols == 5
    assert g.count_islands() == 2


def test5():
    g = Graph((
        (1, 1, 0, 0, 0),
        (0, 1, 0, 0, 1),
        (1, 0, 0, 1, 1),
        (0, 0, 0, 0, 0),
        (1, 0, 1, 0, 1)
    ))
    assert g.rows == 5
    assert g.cols == 5
    assert g.count_islands() == 5
