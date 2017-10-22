

def find_max(_list):
    return reduce((lambda x, a: x if x > a else a), _list, 0)


def find_max2(_list):
    if len(_list) == 1:
        return _list[0]
    v = find_max2(_list[1:])
    return _list[0] if _list[0] > v else v


assert find_max([1, 2, 3, 4, 3, 2, 1, 7, 8, 6, 2]) == 8
assert find_max2([1, 2, 3, 4, 3, 2, 1, 7, 8, 6, 2]) == 8
