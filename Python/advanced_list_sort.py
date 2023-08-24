# Create a function that takes a list of numbers or strings and returns 
# a list with the items from the original list stored into sublists. 
# Items of the same value should be in the same sublist.

# https://edabit.com/challenge/6vSZmN66xhMRDX8YT

import _assert
from collections import Counter


def advanced_sort(data: list[int|str]) -> list[list[int|str]]:
    return [[value] * count for value, count in Counter(data).items()]

    
if __name__=="__main__":
    _assert.assert_results(advanced_sort([1,2,1,2]) , [[1,1],[2,2]])
    _assert.assert_results(advanced_sort([2,1,2,1]) , [[2,2],[1,1]])
    _assert.assert_results(advanced_sort([3,2,1,3,2,1]) , [[3,3],[2,2],[1,1]])
    _assert.assert_results(advanced_sort([5,5,4,3,4,4]) , [[5,5],[4,4,4],[3]])
    _assert.assert_results(advanced_sort([80,80,4,60,60,3]),[[80,80],[4],[60,60],[3]])
    _assert.assert_results(advanced_sort(['c','c','b','c','b',1,1]),[['c','c','c'],['b','b'],[1,1]])
    _assert.assert_results(advanced_sort([1234, 1235, 1234, 1235, 1236, 1235]),[[1234, 1234],[1235, 1235, 1235],[1236]])
    _assert.assert_results(advanced_sort(['1234', '1235', '1234', '1235', '1236', '1235']),[['1234', '1234'],['1235', '1235', '1235'],['1236']])
    