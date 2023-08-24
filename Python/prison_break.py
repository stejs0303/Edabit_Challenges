# A prison can be represented as a list of cells. Each cell contains exactly one prisoner. 
# A 1 represents an unlocked cell and a 0 represents a locked cell.

# https://edabit.com/challenge/SHdu4GwBQehhDm4xT

import testit 

def freed_prisoners(prison: list[bool]) -> int:
    if len(prison) > 0 and prison[0] == 0: 
        return 0
    
    lf, freed = True, 0
    for cell in prison: 
        if cell != lf: continue
        freed += 1
        lf = not lf
    
    return freed
    
    
if __name__=="__main__":
    testit.assert_results(freed_prisoners([1, 1, 0, 0, 0, 1, 0]), 4)
    testit.assert_results(freed_prisoners([1, 0, 0, 0, 0, 0, 0]), 2) 
    testit.assert_results(freed_prisoners([1, 1, 1, 0, 0, 0]), 2) 
    testit.assert_results(freed_prisoners([1, 0, 1, 0, 1, 0]), 6) 
    testit.assert_results(freed_prisoners([1, 1, 1]), 1)
    testit.assert_results(freed_prisoners([0, 0, 0]), 0)
    testit.assert_results(freed_prisoners([0, 1, 1, 1]), 0)