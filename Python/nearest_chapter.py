# Create a function that returns which chapter is nearest to the page you're on. If two chapters are equidistant, 
# return the chapter with the higher page number.

# https://edabit.com/challenge/ZeeWN5NdFa8ALJq5G


import testit
import math


def modified_bin_search_recursive(arr: list[int], start: int, end: int, val: int) -> int:
    if end - start == 1:
        return start if (val - arr[start]) < (arr[end] - val) else end
    
    center = math.ceil((end + start) / 2)
    if arr[center] > val:
        return modified_bin_search_recursive(arr, start, center, val)
    else:
        return modified_bin_search_recursive(arr, center, end, val)


def modified_bin_search_non_recursive(arr: list[int], val: int) -> int:
    start, end = 0, len(arr) - 1
    
    while (end - start != 1):
        center = math.ceil((end + start) / 2)
        if arr[center] > val:
            end = center
        else:
            start = center
            
    return start if (val - arr[start]) < (arr[end] - val) else end


def nearest_chapter(chapt: dict[str, int], page: int) -> str:
    rev_chapt = {idx: key for idx, [key, _] in enumerate(chapt.items())}
    nearest = modified_bin_search_recursive(list(chapt.values()), 0, len(chapt) - 1, page)
    return rev_chapt[nearest]


def nearest_chapter2(chapt: dict[str, int], page: int) -> str:
    rev_chapt = {idx: key for idx, [key, _] in enumerate(chapt.items())}
    nearest = modified_bin_search_non_recursive(list(chapt.values()), page)
    return rev_chapt[nearest]


def nearest_chapter3(chapt: dict[str, int], page: int) -> str:
    nearest = modified_bin_search_non_recursive(list(chapt.values()), page)
    for idx, [key, _] in enumerate(chapt.items()):
        if idx == nearest: return key
        
    return None


if __name__=="__main__":
    testit.assert_results(nearest_chapter({"Chapter 1" : 1, "Chapter 2" : 15,"Chapter 3" : 37}, 10), "Chapter 2")
    testit.assert_results(nearest_chapter({"New Beginnings" : 1,"Strange Developments" : 62,"The End?" : 194,"The True Ending" : 460}, 200), "The End?")
    testit.assert_results(nearest_chapter({"Chapter 1a" : 1,"Chapter 1b" : 5}, 3), "Chapter 1b")
    testit.assert_results(nearest_chapter({"Chapter 1a" : 1,"Chapter 1b" : 5,"Chapter 1c" : 50,"Chapter 1d" : 100}, 75), "Chapter 1d")
    testit.assert_results(nearest_chapter({"Chapter 1a" : 1,"Chapter 1b" : 5,"Chapter 1c" : 50,"Chapter 1d" : 100,"Chapter 1e" : 200}, 150), "Chapter 1e")
    testit.assert_results(nearest_chapter({"Chapter 1a" : 1,"Chapter 1b" : 5,"Chapter 1c" : 50,"Chapter 1d" : 100,"Chapter 1e" : 200}, 74), "Chapter 1c")
    testit.assert_results(nearest_chapter({"Chapter 1a" : 1,"Chapter 1b" : 5,"Chapter 1c" : 50,"Chapter 1d" : 100,"Chapter 1e" : 200,"Chapter 1f" : 400}, 300), "Chapter 1f")
    
    book = {"Chapter 1a" : 1,"Chapter 1b" : 5,"Chapter 1c" : 50,"Chapter 1d" : 100,
            "Chapter 1e" : 200,"Chapter 1f" : 400, "Chapter 1g" : 800, "Chapter 1h" : 1600, 
            "Chapter 1i" : 1650, "Chapter 1j" : 2000, "Chapter 1k" : 2100, "Chapter 1l" : 2330,
            "Chapter 1m" : 2400, "Chapter 1n" : 2500, "Chapter 1o" : 2700, "Chapter 1p" : 2800,
            "Chapter 1q" : 2900, "Chapter 1r" : 3000, "Chapter 1s" : 3050, "Chapter 1t" : 3100,
            "Chapter 1u" : 4000, "Chapter 1v" : 8000, "Chapter 1x" : 16000, "Chapter 1w" : 32000,
            "Chapter 1z" : 64000}
    page = 16001
    
    testit.time_it(nearest_chapter, book, page)
    testit.time_it(nearest_chapter2, book, page)
    testit.time_it(nearest_chapter3, book, page)