# Write a function that selects all words that have all the same vowels 
# (in any order and/or number) as the first word, including the first word.

# https://edabit.com/challenge/uwFHSRewNpmBNvbME

import testit


vowels = ['a', 'e', 'i', 'o', 'u']
def same_vowel_group(words: list[str]) -> list[str]:
    match = set(char for char in words[0] if char in vowels)
    return [word for word in words if set(char for char in word if char in vowels) == match]


def same_vowel_group2(words: list[str]) -> list[str]:
    return [word for word in words if set(char for char in word if char in ['a', 'e', 'i', 'o', 'u']) == set(char for char in words[0] if char in ['a', 'e', 'i', 'o', 'u'])]


if __name__=="__main__":
    testit.assert_results(same_vowel_group(["hoops", "chuff", "bot", "bottom"]), ["hoops", "bot", "bottom"])
    testit.assert_results(same_vowel_group(["crop", "nomnom", "bolo", "yodeller"]), ["crop", "nomnom", "bolo"])
    testit.assert_results(same_vowel_group(["semantic", "aimless", "beautiful", "meatless icecream"]), ["semantic", "aimless", "meatless icecream"])
    testit.assert_results(same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]), ["many"])
    testit.assert_results(same_vowel_group(["toe", "ocelot", "maniac"]), ["toe", "ocelot"])
    testit.assert_results(same_vowel_group(["a", "apple", "flat", "map", "shark"]), ["a", "flat", "map", "shark"])
    testit.assert_results(same_vowel_group(["a", "aa", "ab", "abc", "aaac", "abe"]), ["a", "aa", "ab", "abc", "aaac"])
    
    testit.time_it(same_vowel_group, ["semantic", "aimless", "beautiful", "meatless icecream"])
    testit.time_it(same_vowel_group2, ["semantic", "aimless", "beautiful", "meatless icecream"])