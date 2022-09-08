#!/usr/bin/env python

# run with loading intel-tbb/*  module and without it
# version of intel-tbb is specific to each python3.*
# To see specs for numba use: numba -s

import numpy as np
import numba
numba.config.THREADING_LAYER = 'safe'

@numba.jit(nopython=True, parallel=True)
def add(a, b):
    for i in numba.prange(len(a)):
        a[i] += b[i]

a = np.ones(4)
b = np.ones(4)
add(a, b)
print(a)
