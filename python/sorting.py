# -*- coding: utf8 -*-


def selection(data):
    if len(data) < 2:
        return data
    for start in range(len(data) - 1):
        pos = start
        for i in range(start + 1, len(data)):
            if data[i] < data[pos]:
                pos = i
        data[start], data[pos] = data[pos], data[start]
    return data


def insertion(data):
    if len(data) < 2:
        return data
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if data[j - 1] < data[j]:
                break
            data[j], data[j - 1] = data[j - 1], data[j]
    return data


def partition(data, lo, hi):
    pivot = data[hi]
    i = lo - 1
    for j in range(lo, hi):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    if data[hi] < data[i + 1]:
        data[i + 1], data[hi] = data[hi], data[i + 1]
    return i + 1


def quicksort(data, lo=0, hi=None):
    if hi - lo < 1:
        return data
    if hi is None:
        hi = len(data) - 1
    if lo < hi:
        p = partition(data, lo, hi)
        quicksort(data, lo, p - 1)
        quicksort(data, p + 1, hi)
    return data


def mergesort(data):
    if len(data) <= 1:
        return data
    mid = len(data) / 2
    left = mergesort(data[0:mid])
    right = mergesort(data[mid:])
    del data[:]
    while left and right:
        data.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    if left:
        data.extend(left)
    if right:
        data.extend(right)
    return data
