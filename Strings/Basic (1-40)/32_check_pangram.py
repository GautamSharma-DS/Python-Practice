# =========================================================================================
#                              QUESTION 32: CHECK PANGRAM
# =========================================================================================


# i). USING set()

s = "The quick brown fox jumps over the lazy dog"
alphabet = set("abcdefghijklmnopqrstuvwxyz")

print("set():", alphabet.issubset(set(s.lower())))


# ii). USING FOR LOOP

s = "The quick brown fox jumps over the lazy dog"
is_pangram = True

for ch in "abcdefghijklmnopqrstuvwxyz":
    if ch not in s.lower():
        is_pangram = False
        break

print("For loop:", is_pangram)


# iii). USING all()

s = "Pack my box with five dozen liquor jugs"
print("all():", all(ch in s.lower() for ch in "abcdefghijklmnopqrstuvwxyz"))


# iv). USING COUNT OF UNIQUE LETTERS

s = "The quick brown fox jumps over the lazy dog"
letters = set(ch for ch in s.lower() if ch.isalpha())

print("Unique letters:", len(letters) == 26)


# v). USING FUNCTION

def is_pangram(s):
    return set("abcdefghijklmnopqrstuvwxyz").issubset(set(s.lower()))


print("Function:", is_pangram("Sphinx of black quartz judge my vow"))


# vi). USING COUNT ARRAY

s = "The quick brown fox jumps over the lazy dog"
present = [False] * 26

for ch in s.lower():
    if "a" <= ch <= "z":
        present[ord(ch) - ord("a")] = True

print("Count array:", all(present))


# vii). USING string.ascii_lowercase

import string

s = "Pack my box with five dozen liquor jugs"
print("ascii_lowercase:", set(string.ascii_lowercase).issubset(s.lower()))


# viii). FIND MISSING LETTERS

s = "The quick brown fox"
missing = []

for ch in string.ascii_lowercase:
    if ch not in s.lower():
        missing.append(ch)

print("Missing letters:", missing)


# ix). PANGRAM AFTER REMOVING NON-ALPHABETS

s = "The quick brown fox jumps over the lazy dog!!! 123"
letters = set()

for ch in s.lower():
    if ch.isalpha():
        letters.add(ch)

print("Clean pangram:", len(letters) == 26)


# x). CHECK LIST OF SENTENCES

sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Python is easy"
]
answers = []

for sentence in sentences:
    answers.append(set(string.ascii_lowercase).issubset(sentence.lower()))

print("List of sentences:", answers)
