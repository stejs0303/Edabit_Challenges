# Create a function that returns the simplified version of a fraction.

# https://edabit.com/challenge/vQgmyjcjMoMu9YGGW

import _assert
import fractions


def simplify_using_fractions(txt: str) -> str:
    return str(fractions.Fraction(txt))
    

def binary_gcd(a: int, b: int) -> int:
    if a == 0: return b
    if b == 0: return a
    
    shift = 0
    while ((a | b) & 1) == 0: 
        a >>= 1; b >>= 1; shift += 1

    while (a & 1) == 0:
        a >>= 1

    while b != 0:
        while (b & 1) == 0: b >>= 1
        if a > b: a, b = b, a
        b -= a

    return a << shift


def simplify_using_binary_gcd(txt: str) -> str:
    dividend, divisor = txt.split("/")
    dividend, divisor = int(dividend), int(divisor)
    gcd = binary_gcd(dividend, divisor)
    
    dividend /= gcd
    divisor /= gcd
    
    return f"{int(dividend)}/{int(divisor)}" if (dividend / divisor) % 1 != 0 else f"{int(dividend / divisor)}"


if __name__=="__main__":
    _assert.assert_results(simplify_using_binary_gcd("5/7"), "5/7")
    _assert.assert_results(simplify_using_binary_gcd("4/6"), "2/3")
    _assert.assert_results(simplify_using_binary_gcd("11/10"), "11/10")
    _assert.assert_results(simplify_using_binary_gcd("8/4"), "2")
    _assert.assert_results(simplify_using_binary_gcd("7/4"), "7/4")
    _assert.assert_results(simplify_using_binary_gcd("6/4"), "3/2")
    _assert.assert_results(simplify_using_binary_gcd("300/200"), "3/2")
    _assert.assert_results(simplify_using_binary_gcd("50/25"), "2")
    _assert.assert_results(simplify_using_binary_gcd("5/45"), "1/9")
    
    _assert.time_it(simplify_using_fractions, "21/33")
    _assert.time_it(simplify_using_binary_gcd, "21/33")