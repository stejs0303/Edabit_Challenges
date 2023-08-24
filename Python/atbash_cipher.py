# The Atbash cipher is an encryption method in which each letter of a word is 
# replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

# https://edabit.com/challenge/MGALfBAXhXqqdFyqo

import testit


def atbash(text: str) -> str:
    res = ""
    for char in text:
        if not char.isalpha(): res += char; continue
        base = 64 + 32 * (char.islower())
        normalized = ord(char) - base
        res += chr(base + 27 - normalized)
        
    return res


if __name__=="__main__":
    testit.assert_results(atbash("Hello world!"), "Svool dliow!")
    testit.assert_results(atbash("abcdefghijklmnopqrstuvwxyz"), "zyxwvutsrqponmlkjihgfedcba")
    testit.assert_results(atbash("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ZYXWVUTSRQPONMLKJIHGFEDCBA")
    testit.assert_results(atbash("The word 'atbash' derives from the the first and last 2 letters of the Hebrew alphabet."), 
                   "Gsv dliw 'zgyzhs' wvirevh uiln gsv gsv urihg zmw ozhg 2 ovggvih lu gsv Svyivd zokszyvg.")
    testit.assert_results(atbash("Vmxibkgrlm zmw wvxibkgrlm ziv rwvmgrxzo uli gsv Zgyzhs xrksvi."),
                   "Encryption and decryption are identical for the Atbash cipher.")