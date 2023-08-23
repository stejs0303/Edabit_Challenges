from typing import Any

def assert_results(function_result: Any, expected_value: Any) -> bool:
    match function_result:
        case str() | list() | bool() | int():
            print(f"Result   = {function_result}\n"
                  f"Expected = {expected_value}\n"
                  f"{function_result == expected_value = }\n")    
        
        case _:
            print(f"{type(function_result)} not implemented")