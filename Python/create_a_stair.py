# Write a function which takes an integer steps and returns a string representing 
# an upward stair with steps representing the number of the steps in the stair. 
# Each step will be represented by combinations of underscore(s), newline(s), and vertical line(s).

# https://edabit.com/challenge/ZF9e922XuRaMu43Wp

import _assert


def stair(step: int) -> str:
    if step == 0: return "_|"
    return f"{'  '*step}_|\n"


def stairs(steps: int) -> str:
    if steps == 0: return "___"
    return f"{'  '*steps}_\n" + "".join((stair(step) for step in range(steps - 1, -1, -1)))
    
    
def stairs2(steps: int) -> str:
    if steps == 0: return "___"
    # Top stair + rest of the stairs
    return f"{'  '*steps}_\n" + "".join((f"{'  '*step}_|\n" if step != 0 else "_|" for step in range(steps - 1, -1, -1)))


if __name__=="__main__":
    _assert.assert_results(stairs2(0), "___")
    _assert.assert_results(stairs2(1), '  _\n_|')
    _assert.assert_results(stairs2(2), '    _\n  _|\n_|')
    _assert.assert_results(stairs2(3), '      _\n    _|\n  _|\n_|')
    _assert.assert_results(stairs2(5), '          _\n        _|\n      _|\n    _|\n  _|\n_|')
    _assert.assert_results(stairs2(10), '                    _\n                  _|\n                _|\n              _|\n            _|\n          _|\n        _|\n      _|\n    _|\n  _|\n_|')
    _assert.assert_results(stairs2(50), '                                                                                                    _\n                                                                                                  _|\n                                                                                                _|\n                                                                                              _|\n                                                                                            _|\n                                                                                          _|\n                                                                                        _|\n                                                                                      _|\n                                                                                    _|\n                                                                                  _|\n                                                                                _|\n                                                                              _|\n                                                                            _|\n                                                                          _|\n                                                                        _|\n                                                                      _|\n                                                                    _|\n                                                                  _|\n                                                                _|\n                                                              _|\n                                                            _|\n                                                          _|\n                                                        _|\n                                                      _|\n                                                    _|\n                                                  _|\n                                                _|\n                                              _|\n                                            _|\n                                          _|\n                                        _|\n                                      _|\n                                    _|\n                                  _|\n                                _|\n                              _|\n                            _|\n                          _|\n                        _|\n                      _|\n                    _|\n                  _|\n                _|\n              _|\n            _|\n          _|\n        _|\n      _|\n    _|\n  _|\n_|')
    
    _assert.time_it(stairs, 10)
    _assert.time_it(stairs2, 10)
    