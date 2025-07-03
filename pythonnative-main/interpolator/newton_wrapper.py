import ctypes
import numpy as np
import os
import sys

# definiowanie lokalizacji pliku z kodem natywnym
libname = "libnewton.so" if sys.platform != "win32" else "newton.dll"
libpath = os.path.join(os.path.dirname(__file__), "..", "interpolator/lib", libname)
lib = ctypes.CDLL(libpath)

# zczytanie typow argumentow funkcji divided_diff
lib.divided_diff.argtypes = [ctypes.POINTER(ctypes.c_double),
                             ctypes.POINTER(ctypes.c_double),
                             ctypes.POINTER(ctypes.c_double),
                             ctypes.c_int]

# zaczytanie typow argumentow funkcji newton_interpolation
lib.newton_interpolation.argtypes = [ctypes.POINTER(ctypes.c_double),
                                     ctypes.POINTER(ctypes.c_double),
                                     ctypes.c_int,
                                     ctypes.c_double]
# zaczytanie zmiennej result
lib.newton_interpolation.restype = ctypes.c_double


def interpolate(x, y, values):
    n = len(x)
    x_arr = (ctypes.c_double * n)(*x)
    y_arr = (ctypes.c_double * n)(*y)
    a_arr = (ctypes.c_double * n)()

    # wywolanie funkcji divided_diff z kodu natywnego
    lib.divided_diff(x_arr, y_arr, a_arr, n)

    results = []
    for val in values:

        #wywolanie funkcji newton_interpolation z kodu natywnego
        result = lib.newton_interpolation(x_arr, a_arr, n, ctypes.c_double(val))
        results.append(result)
    return results
