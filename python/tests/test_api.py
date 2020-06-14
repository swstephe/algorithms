# -*- coding: utf8 -*-
import random
from api.crypto.enc import hex, base64, utils

# from api.crypto.hmac import sha256


def test_nibbles():
    assert bytes(utils.nibbles(b'\x01\x23\x45\x67\x89\xab\xcd\xef')) == \
        b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    assert bytes(utils.nibbles(b'\x01')) == b'\x00\01'


def test_splits():
    assert list(utils.splits('abcdefghijklm', 2)) == \
        ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'm']
    assert list(utils.splits('abcdefghijklm', 3)) == \
        ['abc', 'def', 'ghi', 'jkl', 'm']


def test_triplets():
    assert list(utils.triplets(b'\x01\x02\x03\x04\x05\x06\x07')) == \
        [0x010203, 0x040506, 0x07]


def test_quarters():
    assert list(utils.quarters(
        (0x3f << 18) | (0x00 << 12) | (0x18 << 6) | 0x3b
    )) == [0x3f, 0x00, 0x18, 0x3b]


def test_word_array():
    wa = bytearray(random.getrandbits(8) for _ in range(12))
    assert hex.decode(hex.encode(wa)) == wa
    # assert base64.parse(base64.stringify(wa)).words == wa.words


# def test_hmac_sha256():
#     assert bytes.fromhex('b613679a0814d9ec772f95d778c35fc5ff1697c493715653c6c712144292c5ad') == \
#         sha256('', '')
#     assert bytes.fromhex('f7bc83f430538424b13298e6aa6fb143ef4d59a14946175997479dbc2d1a3cd8') == \
#         sha256("key", "The quick brown fox jumps over the lazy dog")
