# -*- coding: utf8 -*-
import random
from nose.tools import *
from api.crypto.enc import hex
from binascii import unhexlify, hexlify


def random_bytes(n):
    return bytes(random.randint(0x00, 0xff) for _ in range(n))


def test_power_of_2():
    for p in range(15):
        _orig = random_bytes(2**p)
        _enc = hex.encode(_orig)
        eq_(hexlify(_orig).decode('ascii'), _enc)
        _dec = hex.decode(_enc)
        eq_(unhexlify(_enc), _dec)
        eq_(_orig, _dec)


def test_power_of_2_plus_1():
    for p in range(15):
        _orig = random_bytes(2**p + 1)
        _enc = hex.encode(_orig)
        eq_(hexlify(_orig).decode('ascii'), _enc)
        _dec = hex.decode(_enc)
        eq_(unhexlify(_enc), _dec)
        eq_(_orig, _dec)
