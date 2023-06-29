#!/usr/bin/env python

# sp800_22_serial_test.py
# 
# Copyright (C) 2017 David Johnston
# This program is distributed under the terms of the GNU General Public License.
# 
# This file is part of sp800_22_tests.
# 
# sp800_22_tests is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# sp800_22_tests is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with sp800_22_tests.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import math
#from scipy.special import gamma, gammainc, gammaincc
from gamma_functions import *
#from scipy.special import gamma, gammainc, gammaincc

def change(n,m):
    if len(n) < m:
        r = '0'*(m-len(n)) + n
    else:
        r = n
    return r

def poker(bits):
    n = len(bits)
    M = 4
    N = int(math.floor(n / M))

    line = []
    for i in range(N):
        block = bits[i * (M):((i + 1) * (M))]
        block = list(map(str, block))
        s="".join(block)
        line.append(s)

    key = 2**M
    res = [0]*key
    for j in range(key):
        r = bin(j).replace('0b', '')
        r = change(r,M)
        res[j] = line.count(r)
    #print(res)
    res_sum = 0
    for m in range(key):
        res_sum += res[m] ** 2

    v = float(2**M)/float(N) * res_sum -N
    print(v)
    p = gammainc((2**M - 1)/ 2.0, v/2.0)
    #print(p)
    success = (p >= 0.01)
    return success, p, None



