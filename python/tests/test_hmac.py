# -*- coding: utf8 -*-
import hashlib
import hmac
from api.crypto.hmac import sha256


TEST_CASES = (
    (b'', b''),
)


def test_hmac():
    for k, m in TEST_CASES:
        assert sha256(k, m) == hmac.new(k, m, digestmod=hashlib.sha256).digest()
