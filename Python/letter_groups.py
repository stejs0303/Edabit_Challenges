# Recursion: N-Length Letter Groups
# Write a function that returns an array of strings populated from the slices of 
# n-length characters of the given word (a slice after another while n-length applies onto the word).

# https://edabit.com/challenge/TcKZnbdgx7q6LLoFR

import testit


def collect(word: str, length: int) -> list[str]:
    if len(word) < length: return []
    res = [f"{word[0:length]}"]
    res.extend(collect(word[length:], length))
    return sorted(res)


if __name__=="__main__":
    str_vector = [
      "intercontinentalisationalism", "strengths", "pneumonoultramicroscopicsilicovolcanoconiosis",
      "lexicographically", "anesthesiologists", "subdermatoglyphic", "sesquipedalianism",
      "recollection", "pseudopseudohypoparathyroidism", "floccinaucinihilipilification",
      "antidisestablishmentarianism", "supercalifragilisticexpialidocious", "incomprehensibilities",
      "astrophysicists", "honorificabilitudinitatibus", "unimaginatively", "euouae", "tsktsk",
      "uncopyrightable" 
    ]
    num_vector =	[ 6, 3, 15, 4, 6, 6, 6, 3, 7, 2, 5, 3, 9, 4, 12, 8, 7, 6, 11 ]
    res_vector = [
      ["ationa", "interc", "ntalis", "ontine"], ["eng", "str", "ths"],
      ["croscopicsilico", "pneumonoultrami", "volcanoconiosis"],
      ["aphi", "call", "cogr", "lexi"], ["anesth", "esiolo"], ["matogl", "subder"],
      ["pedali", "sesqui"], ["ect", "ion", "oll", "rec"], ["hyroidi", "poparat", "pseudop", "seudohy"],
      ["at", "ci", "fl", "ic", "if", "ih", "il", "il", "in", "io", "ip", "na", "oc", "uc"],
      ["ablis", "antid", "arian", "hment", "isest"],
      ["ali", "ali", "doc", "erc", "fra", "gil", "ice", "iou", "ist", "sup", "xpi"],
      ["ensibilit", "incompreh"], ["astr", "ophy", "sici"], ["honorificabi", "litudinitati"],
      ["unimagin"], [], ["tsktsk"], ["uncopyright"]
    ]
    for i, x in enumerate(str_vector): testit.assert_results(collect(x, num_vector[i]), res_vector[i])