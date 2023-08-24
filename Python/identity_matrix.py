# Create a function that takes an integer n and returns the identity matrix of n x n dimensions. 
# For this challenge, if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. 
# It does not matter if the mirror image is left-right or top-bottom.

# https://edabit.com/challenge/QN4RMpAnktNvMCWwg

import numpy as np
import _assert


def id_mtrx(size: int) -> str|list|list[list[int]]:
    if type(size) not in [int, float]: return "ERROR"
    if size == 0: return list()
    
    start = size + 1 if size < 0 else 0
    end   = size if size > 0 else 1 
    return [[1 if np.abs(y) == x else 0 for x in range(np.abs(size))] for y in range(start, end)]

    
if __name__=="__main__":
    _assert.assert_results(id_mtrx(1), [[1]])
    _assert.assert_results(id_mtrx(2), [[1, 0], [0, 1]])
    _assert.assert_results(id_mtrx(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    _assert.assert_results(id_mtrx(4), [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    _assert.assert_results(id_mtrx(-6), [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], 
                                         [0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]])
    _assert.assert_results(id_mtrx("edabit"), "ERROR")