from typing import Any
import timeit as _timeit
import sys


def assert_results(function_result: Any, expected_value: Any) -> bool:
    match function_result:
        case str() | list() | bool() | int():
            print(f"Result   = {function_result}\n"
                  f"Expected = {expected_value}\n"
                  f"{function_result == expected_value = }\n")    
        
        case _:
            print(f"{type(function_result)} not implemented")
    
            
def time_it(func, *params: Any) -> None:
    print(f"{func.__name__} = {_timeit.timeit(lambda: func(*params)):.2f} us")