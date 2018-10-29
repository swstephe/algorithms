# -*- coding: utf-8 -*-
import math
import random


def is_prime0(n):
    if n <= 4:
        return n in (2, 3)
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def is_prime1(n):
    if n <= 4:
        return n in (2, 3)
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def fermat(n, k=15):
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


def miller(n, k=4):
    if n <= 4:
        return n in (2, 3)
    d = n - 1
    while d % 2 == 0:
        d >>= 1
    for i in range(k):
        if not miller_test(d, n):
            return False
    return True
