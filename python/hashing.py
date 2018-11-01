# -*- coding: utf-8 -*-
import math
import primes

def reduce(func, seq, init):
    value = init
    for item in seq:
        value = func(value, item)
    return value


FNV_BASIS = 'chongo <Landon Curt Noll> /\../\\'
UINT_MAX = (1 << 32) - 1
ADLER_MOD = 0xfff1
TERMS = (0, 1, 2, 4, 5, 7, 8, 10, 11, 12, 16, 22, 23, 26)
CRC32_POLY = reduce(lambda a, t: a | 1 << (31 - t), TERMS, 0)
CRC32_TAB = tuple(
    reduce(lambda a, _: (a >> 1) ^ CRC32_POLY if a & 1 else a >> 1, range(8), i)
    for i in range(1 << 8)
)


def adler32(buf):
    lo, hi = reduce(
        lambda a, b: ((a[0] + b) % ADLER_MOD, (a[0] + a[1] + b) % ADLER_MOD),
        (ord(b) for b in buf),
        (1, 0)
    )
    return hi << 16 | lo


def crc32(buf, crc=0):
    return ~reduce(lambda a, b: (a >> 8) ^ CRC32_TAB[(a ^ ord(b)) & 0xff], buf, crc ^ UINT_MAX) & UINT_MAX


def python_hash(buf):
    x = reduce(lambda a, b: ((1000003*a) ^ ord(b)) & UINT_MAX, buf, ord(buf[0]) << 7 if buf else 0) ^ len(buf)
    return -2 if x == -1 else x


def fnv0(buf, prime, bits):
    return reduce(lambda a, b: (a*prime) ^ ord(b), buf, 0) & ((1 << bits) - 1)


def fnv_basis(prime, bits):
    return fnv0(FNV_BASIS, prime, bits)


def fnv_prime(s):
    assert 4 < s < 11
    bits = [i for i in range(0xf, 0xf2) if sum((i >> p) & 1 for p in range(8)) in (4, 5)]
    t = (5 + (1 << s)) / 12
    print('t', 8*t)
    value = (1 << (8*t)) + 0x100000000
    print('value', value)
    for b in bits:
        p = value + b
        if not primes.is_prime1(p):
            continue
        if p % ((1 << 40) - (1 << 24) - 1) <= 0x1000180:
            continue
        print('prime', value, hex(b), value + b)
        return value + b
    # prime = (1 << t) + (1 << 8) + b


def fnv1a(buf, prime, basis):
    return reduce(lambda a, b: (a ^ ord(b))*prime, (ord(c) for c in buf), basis) & UINT_MAX


def fnv32(buf):
    return fnv1a(buf, 0x811c9dc5, 16777619)
