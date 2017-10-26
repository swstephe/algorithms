# -*- coding: utf-8 -*-
import math
import random


def is_prime0(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_prime1(n):
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def fermat(n, k):
    if n <= 4:
        return n in (2, 3)
    for i in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True


def miller_test(d, n):

    a = random.randint(2, n - 1)
    x = pow(a, d, n)
    if x in (1, n - 1):
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


MILLER_SEEDS = (
    (1373653, (2, 3)),
    (9080191, (31, 73)),
    (4759123141, (2, 7, 61)),
    (1122004669633, (2, 13, 23, 1662803)),
    (2152302898747, (2, 3, 5, 7, 11)),
    (3474749660383, (2, 3, 5, 7, 11, 13)),
    (341550071728321, (2, 3, 5, 7, 11, 13, 17))
)


def witness(n, s, d, a):
    x = pow(a, d, n)
    for _ in xrange(s):
        y = x*x % n
        if y == 1 and x != 1 and x != n - 1:
            return False
        x = y
    return x == 1


def miller(n):
    if n <= 1:
        return False
    if any(n % i == 0 for i in (2, 3)):
        return n in (2, 3)
    d = n / 2
    s = 1
    while not (d & 1):
        d /= 2
        s += 1
    for limit, seeds in MILLER_SEEDS:
        if n < limit:
            return all(witness(n, s, d, seed) for seed in seeds)
    raise RuntimeError("can't determine test seeds")
