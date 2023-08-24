# Given a series of lists, with each individual list containing the time of 
# the alarm set and the sleep duration, return what time to sleep.

# https://edabit.com/challenge/e5XZ82bAk2rBo9EfS

import _assert

def bed_time(*times: tuple[list[str]]) -> list[str]:
    res = []
    for wake_up, sleep_dur in times:
        wh, wm = wake_up.split(":")
        sh, sm = sleep_dur.split(":")
        
        inc, bm = divmod((int(wm) - int(sm)), 60)
        bh = (int(wh) - int(sh) + inc) % 24
        
        res.append(f"{bh:0>2}:{bm:0>2}")
    
    return res


if __name__=="__main__":
    _assert.assert_results(bed_time(['07:50', '07:50']), ['00:00'])
    _assert.assert_results(bed_time(['06:15', '10:00'], ['08:00', '10:00'], ['09:30', '10:00']), ['20:15', '22:00', '23:30'])
    _assert.assert_results(bed_time(['05:45', '04:00'], ['07:10', '04:30']), ['01:45', '02:40'])
