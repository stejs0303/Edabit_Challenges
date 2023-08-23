# The Atbash cipher is an encryption method in which each letter of a word is 
# replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

# https://edabit.com/challenge/MGALfBAXhXqqdFyqo

from _assert import assert_results


def atbash(text: str) -> str:
    res = ""
    for char in text:
        if not char.isalpha(): res += char; continue
        base = 64 + 32 * (char.islower())
        normalized = ord(char) - base
        res += chr(base + 27 - normalized)
        
    return res


if __name__=="__main__":
    assert_results(atbash("Hello world!"), "Svool dliow!")
    assert_results(atbash("abcdefghijklmnopqrstuvwxyz"), "zyxwvutsrqponmlkjihgfedcba")
    assert_results(atbash("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ZYXWVUTSRQPONMLKJIHGFEDCBA")
    assert_results(atbash("The word 'atbash' derives from the the first and last 2 letters of the Hebrew alphabet."), 
                   "Gsv dliw 'zgyzhs' wvirevh uiln gsv gsv urihg zmw ozhg 2 ovggvih lu gsv Svyivd zokszyvg.")
    assert_results(atbash("Vmxibkgrlm zmw wvxibkgrlm ziv rwvmgrxzo uli gsv Zgyzhs xrksvi."),
                   "Encryption and decryption are identical for the Atbash cipher.")