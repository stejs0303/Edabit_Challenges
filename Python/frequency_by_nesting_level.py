# Create a function that takes in a nested list and an element and returns the frequency of that element by nested level.

# https://edabit.com/challenge/Yp8crKmgxZ3HiSBAZ


import testit
from collections import Counter

def get_count(lst: list, el: int, depth: int = 0) -> Counter[int, int]:
    out, counter = Counter(), 0
    for val in lst:
        if type(val) == list:
            out.update(get_count(val, el, depth + 1))
        elif val == el:
            counter += 1
    out[depth] += counter
    return out
        

def freq_count(lst: list, el: int) -> list[list[int]]:
    return sorted([[key, value] for key, value in get_count(lst, el, 0).items()], key= lambda x: x[0])

    
if __name__=="__main__":
    testit.assert_results(freq_count([1, 1, 1, 1], 1), [[0, 4]])
    testit.assert_results(freq_count([1, 1, 2, 2], 1), [[0, 2]])
    testit.assert_results(freq_count([1, 1, 2, [1]], 1), [[0, 2], [1, 1]])
    testit.assert_results(freq_count([1, 1, 2, [[1]]], 1), [[0, 2], [1, 0], [2, 1]])
    testit.assert_results(freq_count([[[1]]], 1), [[0, 0], [1, 0], [2, 1]])
    testit.assert_results(freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1), [[0, 1], [1, 2], [2, 3]])
    testit.assert_results(freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5), [[0, 3], [1, 4], [2, 0]])
    testit.assert_results(freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2), [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]])