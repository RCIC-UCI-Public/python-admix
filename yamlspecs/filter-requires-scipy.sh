#!/bin/bash
# The PIP version of scipy has some weird git-version of libquadmath encoded, this 
# filter just edits that so that the system libquadmath package fulfills requirements
/usr/lib/rpm/find-requires $* | sed -e 's/libquadmath-[0-9a-zA-Z-]*.so.0[\.0]*/libquadmath.so.0/' |  sed -e 's/libgfortran-[0-9a-zA-Z-]*.so.5[\.0]*/libgfortran.so.5/' | sort | uniq

