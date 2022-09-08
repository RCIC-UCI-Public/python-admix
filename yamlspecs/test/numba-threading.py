#!/usr/bin/env python

# run with loading intel-tbb/*  module and without it
# version of intel-tbb is specific to each python3.*
# To see specs for numba use: numba -s

from numba import config, njit, threading_layer
import numpy as np

# set the threading layer before any parallel target compilation
config.THREADING_LAYER = 'threadsafe'

@njit(parallel=True)
def foo(a, b):
    return a + b

x = np.arange(10.)
y = x.copy()

# this will force the compilation of the function, select a threading layer
# and then execute in parallel
foo(x, y)

# demonstrate the threading layer chosen
print("Threading layer chosen: %s" % threading_layer())
