# Write a function that groups a string into parentheses clusters. Each cluster should be balanced.

# https://edabit.com/challenge/Fpymv2HieqEd7ptAq

import testit


def split(seq: str) -> list[str]:
    res, counter, prev_end = [], 0, 0
    for clstr_end, char in enumerate(seq, 1):
        if char == '(': counter += 1
        if char == ')': counter -= 1
        if counter == 0: 
            res.append(seq[prev_end:clstr_end]) 
            prev_end = clstr_end
        
    return res


if __name__=="__main__":
    testit.assert_results(split("()()()"), ["()", "()", "()"])
    testit.assert_results(split(""), [])
    testit.assert_results(split("()()(())"), ["()", "()", "(())"])
    testit.assert_results(split("(())(())"), ["(())", "(())"])
    testit.assert_results(split("((()))"), ["((()))"])
    testit.assert_results(split("()(((((((((())))))))))"), ["()", "(((((((((())))))))))"])
    testit.assert_results(split("((())()(()))(()(())())(()())"), ["((())()(()))", "(()(())())", "(()())"])
    testit.assert_results(split("((()))(())()()(()())"), ["((()))", "(())", "()", "()", "(()())"])
    testit.assert_results(split("((())())(()(()()))"), ["((())())", "(()(()()))"])
    testit.assert_results(split("(()(()()))()(((()))()(()))(()((()))(())())"), 
                   ["(()(()()))", "()", "(((()))()(()))", "(()((()))(())())"])
    
    testit.time_it(split, "(()(()()))()(((()))()(()))(()((()))(())())")