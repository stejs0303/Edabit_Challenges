# Create a function that determines whether each seat can "see" the front-stage. 
# A number can "see" the front-stage if it is strictly greater than the number before it.

# https://edabit.com/challenge/xbjDMxzpFcsAWKp97

from _assert import assert_results


def can_see_stage(seats: list[list[int]]) -> bool:
    if len(seats) <= 1: return True
    for front_row, back_row in zip(seats[0:len(seats)-1], seats[1:len(seats)]):
        for front_seat, back_seat in zip(front_row, back_row):
            if front_seat >= back_seat: return False
    
    return True


if __name__=="__main__":
    assert_results(can_see_stage([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), True)
    assert_results(can_see_stage([[1, 2, 2], [1, 2, 3], [4, 4, 4]]), False)
    assert_results(can_see_stage([[1, 1, 2], [5, 2, 3], [4, 4, 4]]), False)
    assert_results(can_see_stage([[1, 1, 2], [5, 2, 3], [6, 4, 4]]), True)
    assert_results(can_see_stage([[0, 0, 0], [1, 1, 1], [2, 2, 2]]), True)
    assert_results(can_see_stage([[2, 0, 0], [1, 1, 1], [2, 2, 2]]), False)
    assert_results(can_see_stage([[1, 0, 0], [1, 1, 1], [2, 2, 2]]), False)
    assert_results(can_see_stage([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 2, 2], [5, 5, 5, 5, 4, 4], [6, 6, 7, 6, 5, 5]]), True)
    assert_results(can_see_stage([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 2, 2], [5, 5, 5, 10, 4, 4], [6, 6, 7, 6, 5, 5]]), False)