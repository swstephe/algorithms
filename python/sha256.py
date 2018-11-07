# -*- coding: utf8 -*-
from functools import reduce
import math

H = (
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
)
K = (
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
)

SHA_BLOCK_SIZE = 64
SHA_DIGEST_SIZE = 32


def word(x):
    return x & 0xffffffff


def rotr(x, y):
    return word((word(x) >> (y & 31)) | (x << (32 - (y & 31))))


def ch(x, y, z):
    return z ^ (x & (y ^ z))


def maj(x, y, z):
    return ((x | y) & z) | (x & y)


def sigma0(x):
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)


def sigma1(x):
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)


def sig0(x):
    return rotr(x, 7) ^ rotr(x, 18) ^ (word(x) >> 3)


def sig1(x):
    return rotr(x, 17) ^ rotr(x, 19) ^ (word(x) >> 10)


def from_words(_words):
    for w in _words:
        for i in reversed(range(4)):
            yield (w >> (i*8)) & 0xff


def to_words(_bytes):
    for i in range(0, len(_bytes), 4):
        yield reduce(lambda a, b: a << 8 | b, _bytes[i:i + 4], 0)


def sha256(message=b''):
    if isinstance(message, str):
        message = bytes(message, 'utf-8')
    count = len(message)
    L = (count + 1)/4 + 2
    N = int(math.ceil(L / 16))
    message += b'\x80' + bytes(N*SHA_BLOCK_SIZE - count)
    M = [
        list(to_words(message[i:i + SHA_BLOCK_SIZE]))
        for i in range(0, N*SHA_BLOCK_SIZE, SHA_BLOCK_SIZE)
    ]
    if len(M[-1]) < 16:
        M[-1] += [0] * (16 - len(M[-1]))
    M[-1][14] = count >> 29
    M[-1][15] = word(count << 3)
    #print('M', M)

    W = [0] * SHA_BLOCK_SIZE
    _H = H[:]
    for i in range(N):
        for t in range(16):
            W[t] = M[i][t]
        for t in range(16, SHA_BLOCK_SIZE):
            W[t] = word(sig1(W[t - 2]) + W[t - 7] + sig0(W[t - 15]) + W[t - 16])

        a, b, c, d, e, f, g, h = _H[:]
        for k, w in zip(K, W):
            t1 = h + sigma1(e) + ch(e, f, g) + k + w
            t2 = sigma0(a) + maj(a, b, c)
            a, b, c, d, e, f, g, h = word(t1 + t2), a, b, c, word(d + t1), e, f, g
        _H = tuple(word(x + y) for x, y in zip(_H, (a, b, c, d, e, f, g, h)))
    return bytes(from_words(_H))


def hmac(key, message=b''):
    print('hmac(%r,%r)' % (key, message))
    if isinstance(key, str):
        key = bytes(key, 'utf-8')
    if isinstance(message, str):
        message = bytes(message, 'utf-8')
    if len(key) > SHA_BLOCK_SIZE:
        key = key[:SHA_BLOCK_SIZE]
    if len(key) < SHA_BLOCK_SIZE:
        key += bytes(SHA_BLOCK_SIZE - len(key))
    print('key', key.hex())
    o_key_pad = bytes(0x5c ^ k for k in key)
    print('o_key_pad', o_key_pad.hex())
    i_key_pad = bytes(0x36 ^ k for k in key)
    print('i_key_pad', i_key_pad.hex())
    first = i_key_pad + message
    print('first', first.hex())
    res1 = sha256(first)
    print('res1', res1.hex())
    second = o_key_pad + res1
    print('second', second.hex())
    result = sha256(second)
    print('result', result.hex())
    return result
