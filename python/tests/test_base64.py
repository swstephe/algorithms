# -*- coding: utf8 -*-
import random
from nose.tools import *
from api.crypto.enc import base64
from base64 import b64encode, b64decode


def random_bytes(n):
    return bytes(random.randint(0x00, 0xff) for _ in range(n))


def test_power_of_2():
    for p in range(15):
        _orig = random_bytes(2**p)
        _enc = base64.encode(_orig)
        eq_(b64encode(_orig).decode('ascii'), _enc)
        _dec = base64.decode(_enc)
        eq_(b64decode(_enc), _dec)
        eq_(_orig, _dec)


def test_power_of_2_plus_1():
    for p in range(15):
        _orig = random_bytes(2**p + 1)
        _enc = base64.encode(_orig)
        eq_(b64encode(_orig).decode('ascii'), _enc)
        _dec = base64.decode(_enc)
        eq_(b64decode(_enc), _dec)
        eq_(_orig, _dec)
