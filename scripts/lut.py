#!/usr/bin/env python

import os

for word in range(0, 0xFFFF+1):
    re = (float(word & 0xFF) - 127.5) / 128.0
    im = (float(word >> 8) - 127.5) / 128.0

    if os.environ["ENDIAN"] == "big":
        re, im = im, re

    print("Complex32 {{ re: {:f}, im: {:f} }},".format(re, im))
